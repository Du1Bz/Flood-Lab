"""
logic/baseline.py
-----------------
F-5. CSR重み付きロビー平均ベースラインの計算。

自分がプレイした ranked_arena / ranked_slayer 試合の全プレイヤーデータを集計し、
CSRを重みとした加重平均を算出する。

【設計方針】
- MatchStats.Players     : 全プレイヤーの CoreStats（Kills/Deaths/Accuracy/Damage等）
- PlayerMatchStats.PlayerStats : 全プレイヤーの PreMatchCsr
- 2テーブルを MatchId で結合してプレイヤーレコードを作る
- 重み = PreMatchCsr（高ランク帯を強く参照）
- ルール別 + 全体の両方を出す

【利用できない情報】
- 他プレイヤーのオブジェクトスタッツ（CTF/Oddball等）はDBにない
  → CoreStatsのみ（Kills/Deaths/Assists/Accuracy/DamageDealt/DamageTaken/PowerWeaponKills）
"""

from __future__ import annotations

import json
import sqlite3
from typing import Any

import numpy as np
import pandas as pd


# ベースラインに含める指標と日本語ラベル
BASELINE_METRICS: dict[str, str] = {
    # CoreStats から直接計算
    "kd_ratio":             "K/D",
    "kda":                  "KDA",
    "accuracy":             "命中率",
    "damage_diff":          "ダメージ差",
    # 試合時間で正規化
    "dpm":                  "与ダメージ/分",
    "damage_taken_per_min": "被ダメージ/分",
    "kpm":                  "キル/分",
    # 派生指標
    "tsi":                  "チームシュート依存度（アシスト率）",
    "engagement_density":   "エンゲージメント密度",
    "pw_kill_rate":         "PWキル率（PWK/kills）",
}

# ベースライン計算不可の指標（理由付き）
BASELINE_UNAVAILABLE: dict[str, str] = {
    "k_rpi":           "TrueSkill2の expected_kills が他プレイヤー分はDBにないため計算不可",
    "d_rpi":           "TrueSkill2の expected_deaths が他プレイヤー分はDBにないため計算不可",
    "impact_score":    "k_rpi / d_rpi に依存するため計算不可",
    "pw_control_rate": "自チーム + 敵チームの合計PWキルが必要だが他プレイヤーのチーム情報が不完全なため計算不可",
    "obj_stats":       "他プレイヤーのオブジェクトスタッツ（flag_captures等）はDBにないため計算不可",
}

# 定義上ベースラインが固定値になる指標
BASELINE_FIXED: dict[str, Any] = {
    "win_rate": {
        "label_ja": "勝率",
        "value": 0.5,
        "note": "全プレイヤーの勝率は定義上0.5（均衡値）",
    },
    "k_rpi": {
        "label_ja": "K-RPI",
        "value": 1.0,
        "note": "1.0が期待値通り。>1.0=期待超え、<1.0=期待以下",
    },
    "d_rpi": {
        "label_ja": "D-RPI",
        "value": 1.0,
        "note": "1.0が期待値通り。>1.0=期待より死ななかった（生存力が高い）",
    },
    "impact_score": {
        "label_ja": "インパクトスコア",
        "value": 1.0,
        "note": "1.0が平均。(k_rpi + d_rpi) / 2",
    },
    "pw_control_rate": {
        "label_ja": "PWコントロール率",
        "value": 0.5,
        "note": "0.5が均衡（自チームと敵チームで半々）",
    },
    "dtr": {
        "label_ja": "ダメージトレード比",
        "value": 1.0,
        "note": "1.0が均衡（与ダメ = 被ダメ）。>1.0が望ましい",
    },
}

# ルール正規化マップ（database._normalize_rule と一致させる）
_RULE_NORM: dict[str, str] = {
    "ctf 3 captures": "CTF_3cap",
    "ctf 5 captures": "CTF_5cap",
    "capture the flag (3 captures)": "CTF_3cap",
    "capture the flag (5 captures)": "CTF_5cap",
    "slayer":          "Slayer",
    "king of the hill": "KOTH",
    "oddball":         "Oddball",
    "strongholds":     "Strongholds",
}


def _safe_round(val: Any, decimals: int = 3) -> Any:
    if val is None:
        return None
    try:
        f = float(val)
        return None if not np.isfinite(f) else round(f, decimals)
    except (TypeError, ValueError):
        return None


def _collect_lobby_records(
    con: sqlite3.Connection,
    match_ids: list[str],
    my_xuid: str,
) -> pd.DataFrame:
    """
    MatchStats と PlayerMatchStats を結合して全プレイヤーレコードを返す。

    Returns
    -------
    pd.DataFrame
        columns: xuid, csr, kills, deaths, assists, accuracy,
                 damage_dealt, damage_taken, damage_diff, pw_kills,
                 shots_fired, shots_hit, duration_sec, kd_ratio, kda, dpm, pw_kill_rate
    """
    if not match_ids:
        return pd.DataFrame()

    placeholders = ",".join(["?" for _ in match_ids])

    ms_df = pd.read_sql(
        f"SELECT MatchId, Players, MatchInfo FROM MatchStats WHERE MatchId IN ({placeholders})",
        con, params=tuple(match_ids),
    )
    ps_df = pd.read_sql(
        f"SELECT MatchId, PlayerStats FROM PlayerMatchStats WHERE MatchId IN ({placeholders})",
        con, params=tuple(match_ids),
    )

    # CSR辞書: {match_id: {xuid: csr}}
    csr_map: dict[str, dict[str, int]] = {}
    for _, row in ps_df.iterrows():
        mid = row["MatchId"]
        csr_map[mid] = {}
        try:
            for ps in json.loads(row["PlayerStats"]):
                pid = ps.get("Id", "")
                rr  = ps.get("Result", {}).get("RankRecap", {})
                pre = rr.get("PreMatchCsr", {}).get("Value", -1)
                if pre and pre > 0:
                    csr_map[mid][pid] = int(pre)
        except Exception:
            pass

    # duration辞書: {match_id: duration_sec}
    duration_map: dict[str, float] = {}
    for _, row in ms_df.iterrows():
        try:
            mi = json.loads(row["MatchInfo"])
            dur_str = mi.get("PlayableDuration", "PT0S")
            # PT4M43.094S → 秒に変換
            import re
            m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:([\d.]+)S)?", dur_str)
            if m:
                h, mn, s = m.groups(default="0")
                duration_map[row["MatchId"]] = float(h)*3600 + float(mn)*60 + float(s)
        except Exception:
            pass

    records = []
    for _, row in ms_df.iterrows():
        mid   = row["MatchId"]
        csrs  = csr_map.get(mid, {})
        dur   = duration_map.get(mid, 0)
        try:
            players = json.loads(row["Players"])
        except Exception:
            continue

        for p in players:
            pid = p.get("PlayerId", "")
            # 自分を除外
            if my_xuid in pid:
                continue
            pts = p.get("PlayerTeamStats", [])
            if not pts:
                continue
            cs = pts[0]["Stats"].get("CoreStats", {})
            csr = csrs.get(pid, -1)
            if csr <= 0:
                continue

            k   = int(cs.get("Kills", 0) or 0)
            d   = int(cs.get("Deaths", 0) or 0)
            a   = int(cs.get("Assists", 0) or 0)
            acc = float(cs.get("Accuracy", 0) or 0)
            # Accuracy は 0〜100 の場合と 0〜1 の場合がある
            if acc > 1:
                acc = acc / 100.0
            dmg_d = float(cs.get("DamageDealt", 0) or 0)
            dmg_t = float(cs.get("DamageTaken", 0) or 0)
            pwk   = int(cs.get("PowerWeaponKills", 0) or 0)
            sf    = int(cs.get("ShotsFired", 0) or 0)
            sh    = int(cs.get("ShotsHit", 0) or 0)

            dur_min = dur / 60.0 if dur > 0 else None

            kd   = k / max(d, 1)
            kda  = k - d + a / 3.0
            dpm  = dmg_d / dur_min if dur_min else None
            dtpm = dmg_t / dur_min if dur_min else None
            kpm  = k / dur_min if dur_min else None
            tsi  = a / (k + a) if (k + a) > 0 else 0.0
            eng  = (k + d + a) / dur_min if dur_min else None
            pw_rate = pwk / k if k > 0 else 0.0

            records.append({
                "match_id":             mid,
                "xuid":                 pid,
                "csr":                  csr,
                "kills":                k,
                "deaths":               d,
                "assists":              a,
                "accuracy":             acc,
                "damage_dealt":         dmg_d,
                "damage_taken":         dmg_t,
                "damage_diff":          dmg_d - dmg_t,
                "pw_kills":             pwk,
                "shots_fired":          sf,
                "shots_hit":            sh,
                "duration_sec":         dur,
                "kd_ratio":             kd,
                "kda":                  kda,
                "dpm":                  dpm,
                "damage_taken_per_min": dtpm,
                "kpm":                  kpm,
                "tsi":                  tsi,
                "engagement_density":   eng,
                "pw_kill_rate":         pw_rate,
            })

    return pd.DataFrame(records)


def _weighted_mean(series: pd.Series, weights: pd.Series) -> float | None:
    """CSR重み付き加重平均。"""
    valid = series.notna() & weights.notna() & (weights > 0)
    if valid.sum() == 0:
        return None
    s = series[valid]
    w = weights[valid]
    return float(np.average(s, weights=w))


def _calc_baseline_for_group(grp: pd.DataFrame) -> dict[str, Any]:
    """1グループ（全体 or ルール別）のベースラインを計算する。"""
    n = len(grp)
    if n < 5:
        return {"n": n, "note": "サンプル不足"}

    w = grp["csr"]
    result: dict[str, Any] = {
        "n":           n,
        "csr_mean":    _safe_round(grp["csr"].mean(), 0),
        "csr_median":  _safe_round(grp["csr"].median(), 0),
    }

    for col, label in BASELINE_METRICS.items():
        if col not in grp.columns:
            continue
        val = _weighted_mean(grp[col], w)
        result[col] = {
            "label_ja":      label,
            "weighted_mean": _safe_round(val, 3),
            "median":        _safe_round(grp[col].median(), 3),
        }

    return result


def build_baseline(
    con: sqlite3.Connection,
    match_ids: list[str],
    my_xuid: str,
    stat_df: pd.DataFrame,
) -> dict[str, Any]:
    """
    F-5. ロビー全プレイヤーのCSR重み付きベースラインを構築する。

    Parameters
    ----------
    con        : SQLite接続
    match_ids  : 対象試合IDリスト（自分の filter 済み試合）
    my_xuid    : 自分のXUID（自分を除外するため）
    stat_df    : 自分のDataFrame（rule_nameカラムで対応ルールを絞るため）

    Returns
    -------
    dict
        overall / by_rule のベースライン値
    """
    if not match_ids:
        return {"note": "試合データなし"}

    lobby = _collect_lobby_records(con, match_ids, my_xuid)

    if lobby.empty:
        return {"note": "ロビーデータ取得不可"}

    # MatchIdとrule_nameを結合するためにstat_dfから辞書を作る
    rule_map = dict(zip(stat_df["match_id"], stat_df["rule_name"]))
    lobby["rule_name"] = lobby["match_id"].map(rule_map)

    active_rules = stat_df["rule_name"].unique().tolist() if "rule_name" in stat_df.columns else []

    result: dict[str, Any] = {
        "label_ja": "ベースライン",
        "description_ja": (
            "自分がプレイした試合のロビー全プレイヤー（自分を除く）のスタッツを"
            "PreMatchCsrで重み付けした加重平均。"
            "高ランク帯のプレイヤーを強く参照する。"
        ),
        "caution": (
            "オブジェクトスタッツ（flag_captures等）は他プレイヤー分がDBにないため含まない。"
            "k_rpi / d_rpi / impact_score / pw_control_rate は fixed_baselines を参照。"
        ),
        # CSR重み付き計算値
        "lobby_weighted": _calc_baseline_for_group(lobby),
        # 定義上固定の基準値
        "fixed": BASELINE_FIXED,
        # 計算不可の説明
        "unavailable": BASELINE_UNAVAILABLE,
        "by_rule": {},
    }

    for rule in active_rules:
        grp = lobby[lobby["rule_name"] == rule]
        if len(grp) < 5:
            continue
        result["by_rule"][str(rule)] = _calc_baseline_for_group(grp)

    return result