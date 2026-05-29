"""
logic/exporter.py
-----------------
AI相談用データエクスポート。

フィルター済みDataFrameを受け取り、
特徴量 + 集計サマリー + 生データ(直近20+ベスト/ワースト5) +
用語集 + ゲームコンテキスト + プロンプト雛形を
1つのJSONファイルとして出力する。

Phase B以降: ゲームコンテキストは halo_knowledge パッケージに移動。
             対象データに関係するマップ/ルールだけを build_relevant_context で絞り込む。
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd

from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY
from src.logic.halo_knowledge import (
    ANALYSIS_CONTRACT,
    METRIC_LIMITATIONS,
    build_relevant_context,
)

# ==================================================
# matchesに含めるカラム
# 生データは直近20試合 + ベスト/ワースト5試合に絞る
# ==================================================

EXPORT_COLUMNS = [
    "match_id", "played_at", "playlist", "map_name", "rule_name",
    "result", "kills", "deaths", "assists",
    "kd_ratio", "kda", "accuracy",
    "damage_dealt", "damage_taken", "damage_diff",
    "k_rpi", "d_rpi", "lgai", "impact_score",
    "csr_pre", "csr_post", "csr_delta",
    "pw_control_rate", "engagement_density",
    "emmr_v2", "party_type",
    "session_id", "session_seq",
]

# ==================================================
# 用語集
# ==================================================

GLOSSARY: dict[str, str] = {
    "kd_ratio":           "K/D。キル数 / デス数。デス=0のときはキル数をそのまま使う",
    "kda":                "キル - デス + アシスト/3。試合の総合貢献度",
    "accuracy":           "命中率。命中数 / 発射数（0〜1の小数）",
    "damage_diff":        "与ダメージ - 被ダメージ。プラスが望ましい",
    "k_rpi":              "K-RPI（キル相対パフォーマンス指数）。TrueSkill2が予測した期待キル数に対する実績比率。1.0=期待通り、>1.0=期待超え、<1.0=期待以下",
    "d_rpi":              "D-RPI（デス相対パフォーマンス指数）。TrueSkill2が予測した期待デス数に対して実際に少なく死んだ比率。>1.0=期待より死ななかった（生存力が高い）",
    "lgai":               "LGAI（ロビー格差補正インパクト）。敵チームMMR - 自チームCSR。正=格上相手、負=格下相手",
    "impact_score":       "インパクトスコア。(K-RPI + D-RPI) / 2。TrueSkill2基準の総合パフォーマンス指標。1.0=平均",
    "emmr_v2":            "eMMR v2（推定MMR）。カルマンフィルタで平滑化した独自推定MMR。ノイズを除いたスキルトレンドを表す",
    "csr_delta":          "CSR増減。1試合でのCSR変動量",
    "party_type":         "パーティタイプ。ソロ/デュオ/トリオ/フルパ",
    "session_seq":        "セッション内試合番号。同一セッション（2時間以内の連続プレイ）内での何試合目か",
    "pw_control_rate":    "PWコントロール率。自チームPWキル / (自チーム + 敵チームPWキル)。0.5が均衡。ショックライフルが未計上のため過小評価になる点に注意",
    "engagement_density": "(キル + デス + アシスト) / 試合時間(分)。試合への関与の濃さ。ルール間比較に有用",
    "tsi":                "TSI（チームシュート依存度）。アシスト / (キル + アシスト)。高いほど連携キルが多い",
    "dtr":                "DTR（ダメージトレード比）。与ダメージ / 被ダメージ。1.0が均衡。差分より比率なのでルール間比較に強い",
    "dpm":                "DPM（分間ダメージ）。与ダメージ / 試合時間(分)。キルに繋がらなくとも前線への圧力を測る",
    "survival_index":     "生存指数（推定）。試合時間(秒) / (デス + 1)。1デスあたりの平均生存時間の近似",
    "k_rpi_std":          "K-RPIの標準偏差。小さいほど安定したキル貢献、大きいほど試合ごとの波がある",
}

# ==================================================
# プロンプト雛形
# 役割: 分析の進め方の推奨手順のみ。
# 制約は analysis_contract に一元化する。
# ==================================================

SUGGESTED_PROMPT = """\
このデータはHalo Infinite専用のローカル分析ツール「Flood-Lab」によって生成されたエクスポートファイルです。

以下の手順でコーチングフィードバックを行ってください。

データ構成:
- analysis_contract: AIが破ってはいけない制約（必ず最初に確認すること）
- game_context: ゲームルールと各ルールの競技セオリー（対象データに関係するマップ/ルールのみ）
- metric_limitations: 各指標の既知の限界（断定前に必ず確認すること）
- glossary: 各指標の定義
- summary: 集計済みサマリー（全体・マップ別・ルール別・パーティ別・セッション疲労・直近20試合）
- features: 事前に計算した特徴量（プレイスタイル・傾向の要約）
  - win_loss_delta: 勝ち試合平均と負け試合平均の差
  - recent_vs_baseline: 直近20戦 vs それ以前の比較
- matches.recent_20: 直近20試合の生データ
- matches.best_5 / worst_5: KDA上位・下位5試合

推奨手順:
0. ユーザー向けのコーチング出力は日本語で書く。
   内部キーが英語でも、説明では日本語ラベルを優先する。
1. まず win_loss_delta を見て、勝敗に効いている指標を特定する。
2. 次に recent_vs_baseline を見て、最近の変化（改善/悪化）を確認する。
3. その後、ルール別・マップ別に原因を分ける。
4. game_context の relevant_rules と照合し、何ができていて何が足りないかを評価する。
5. sample_size（サンプル数）が少ない項目は仮説として扱う（claim_rules を参照）。
6. metric_limitations に書かれた制約を必ず考慮する。
7. 位置取り・VC・意図など DB にない情報は断定しない（analysis_contract 参照）。
8. 改善提案は最大3つに絞り、各提案に根拠指標を添える。\
"""

# ==================================================
# 集計サマリーの生成
# ==================================================

def _safe_round(val: Any, decimals: int = 3) -> Any:
    """NaN / inf を None に変換して丸める。"""
    if val is None:
        return None
    try:
        f = float(val)
        if not np.isfinite(f):
            return None
        return round(f, decimals)
    except (TypeError, ValueError):
        return None


def _agg_group(df: pd.DataFrame) -> dict[str, Any]:
    """DataFrameの集計サマリーを返す。"""
    n = len(df)
    if n == 0:
        return {}

    kills   = df["kills"].sum()
    deaths  = df["deaths"].sum()

    return {
        "matches":            n,
        "win_rate":           _safe_round(df["result_flag"].mean(), 3),
        "kd_ratio":           _safe_round(kills / deaths if deaths > 0 else kills, 2),
        "kda_mean":           _safe_round(df["kda"].mean(), 2),
        "accuracy_mean":      _safe_round(
            df["shots_hit"].sum() / df["shots_fired"].sum()
            if "shots_fired" in df.columns and df["shots_fired"].sum() > 0
            else df["accuracy"].mean(), 3
        ),
        "damage_diff_mean":   _safe_round(df["damage_diff"].mean(), 0),
        "k_rpi_mean":         _safe_round(df["k_rpi"].mean(), 3),
        "d_rpi_mean":         _safe_round(df["d_rpi"].mean(), 3),
        "impact_mean":        _safe_round(df["impact_score"].mean(), 3),
        "csr_delta_sum":      _safe_round(df["csr_delta"].sum(), 0),
        "pw_control_rate_mean": _safe_round(df["pw_control_rate"].mean(), 3)
            if "pw_control_rate" in df.columns else None,
        "engagement_density_mean": _safe_round(df["engagement_density"].mean(), 2)
            if "engagement_density" in df.columns else None,
    }


def _build_win_loss_delta(df: pd.DataFrame) -> dict[str, Any]:
    """
    A-2. win_loss_delta（勝敗差分）。
    勝ち試合平均 vs 負け試合平均の差を指標ごとに計算する。
    """
    win_df  = df[df["result_flag"] == 1]
    loss_df = df[df["result_flag"] == 0]

    def _tsi_mean(sub: pd.DataFrame) -> float | None:
        k = sub["kills"].sum()
        a = sub["assists"].sum()
        return _safe_round(a / (k + a), 3) if (k + a) > 0 else None

    compare_cols = [
        ("kda",                "KDA"),
        ("accuracy",           "命中率"),
        ("damage_diff",        "ダメージ差"),
        ("k_rpi",              "K-RPI"),
        ("d_rpi",              "D-RPI"),
        ("pw_control_rate",    "PWコントロール率（ショックライフル未計上）"),
        ("engagement_density", "エンゲージメント密度"),
    ]

    result: dict[str, Any] = {}
    for col, label in compare_cols:
        if col not in df.columns:
            continue
        w = _safe_round(win_df[col].mean(),  3) if len(win_df)  > 0 else None
        l = _safe_round(loss_df[col].mean(), 3) if len(loss_df) > 0 else None
        d = _safe_round(w - l, 3) if (w is not None and l is not None) else None
        result[col] = {"label": label, "win": w, "loss": l, "diff": d}

    result["tsi"] = {
        "label": "チームシュート依存度（TSI）",
        "win":   _tsi_mean(win_df),
        "loss":  _tsi_mean(loss_df),
        "diff":  _safe_round(
            (_tsi_mean(win_df) or 0) - (_tsi_mean(loss_df) or 0), 3
        ) if (_tsi_mean(win_df) is not None and _tsi_mean(loss_df) is not None) else None,
    }

    return result


def _build_recent_vs_baseline(df: pd.DataFrame, recent_n: int = 20) -> dict[str, Any]:
    """
    A-3. recent_vs_baseline（直近比較）。
    直近 recent_n 戦 vs それ以前の平均を比較する。
    """
    df_sorted = df.sort_values("played_at")
    recent = df_sorted.tail(recent_n)
    prior  = df_sorted.iloc[:-recent_n] if len(df_sorted) > recent_n else pd.DataFrame(columns=df.columns)

    compare_cols = [
        ("win_rate",           "勝率"),
        ("kd_ratio",           "K/D"),
        ("kda",                "KDA"),
        ("accuracy",           "命中率"),
        ("damage_diff",        "ダメージ差"),
        ("k_rpi",              "K-RPI"),
        ("d_rpi",              "D-RPI"),
        ("impact_score",       "インパクトスコア"),
        ("pw_control_rate",    "PWコントロール率"),
        ("engagement_density", "エンゲージメント密度"),
    ]

    def _col_mean(sub: pd.DataFrame, col: str) -> float | None:
        if col == "win_rate":
            return _safe_round(sub["result_flag"].mean(), 3) if "result_flag" in sub.columns and len(sub) > 0 else None
        if col == "kd_ratio":
            d = sub["deaths"].sum()
            k = sub["kills"].sum()
            return _safe_round(k / d if d > 0 else k, 2) if len(sub) > 0 else None
        if col not in sub.columns or len(sub) == 0:
            return None
        return _safe_round(sub[col].mean(), 3)

    result: dict[str, Any] = {
        "recent_n": len(recent),
        "prior_n":  len(prior),
        "note":     f"直近{len(recent)}戦 vs それ以前{len(prior)}戦の比較。prior_n が少ない場合は参考値。",
        "metrics":  {},
    }

    for col, label in compare_cols:
        r = _col_mean(recent, col)
        p = _col_mean(prior,  col) if len(prior) > 0 else None
        d = _safe_round(r - p, 3) if (r is not None and p is not None) else None
        result["metrics"][col] = {
            "label":  label,
            "recent": r,
            "prior":  p,
            "diff":   d,
        }

    return result


def _build_features(df: pd.DataFrame) -> dict[str, Any]:
    """
    AIに渡す事前計算済み特徴量。
    生データを渡す代わりにここで要約する。
    """
    if df.empty:
        return {}

    kills   = df["kills"]
    deaths  = df["deaths"]
    assists = df["assists"]

    total_ka = kills.sum() + assists.sum()
    tsi = _safe_round(assists.sum() / total_ka if total_ka > 0 else None, 3)

    dtr = _safe_round(
        df["damage_dealt"].sum() / df["damage_taken"].sum()
        if df["damage_taken"].sum() > 0 else None, 3
    )

    dpm = _safe_round(df["damage_dealt_per_min"].mean(), 1) \
        if "damage_dealt_per_min" in df.columns else None

    survival_index = _safe_round(
        (df["duration_sec"] / (deaths + 1)).mean(), 1
    ) if "duration_sec" in df.columns else None

    k_rpi_std = _safe_round(df["k_rpi"].std(), 3)

    perfect_rate_mean = _safe_round(df["perfect_rate"].mean(), 3) \
        if "perfect_rate" in df.columns else None

    eng_by_rule: dict[str, Any] = {}
    if "engagement_density" in df.columns:
        for rule, grp in df.groupby("rule_name"):
            eng_by_rule[str(rule)] = _safe_round(grp["engagement_density"].mean(), 2)

    solo_wr = party_wr = None
    if "is_solo" in df.columns:
        solo_df  = df[df["is_solo"] == True]
        party_df = df[df["is_solo"] == False]
        if len(solo_df) >= 3:
            solo_wr  = _safe_round(solo_df["result_flag"].mean(), 3)
        if len(party_df) >= 3:
            party_wr = _safe_round(party_df["result_flag"].mean(), 3)

    pw_win_corr = None
    if "pw_control_rate" in df.columns:
        pw_valid = df.dropna(subset=["pw_control_rate"])
        if len(pw_valid) >= 5:
            pw_win_corr = _safe_round(
                pw_valid["pw_control_rate"].corr(pw_valid["result_flag"]), 3
            )

    k_rpi_mean = df["k_rpi"].mean()
    d_rpi_mean = df["d_rpi"].mean()
    if pd.notna(k_rpi_mean) and pd.notna(d_rpi_mean):
        if k_rpi_mean >= 1.0 and d_rpi_mean >= 1.0:
            style = "balanced_aggressive（キル・生存ともに期待以上）"
        elif k_rpi_mean >= 1.0 and d_rpi_mean < 1.0:
            style = "aggressive（キルは取れるが死も多い）"
        elif k_rpi_mean < 1.0 and d_rpi_mean >= 1.0:
            style = "survival_focused（生存重視だがキルが少ない。Oddballでは守りすぎの可能性）"
        else:
            style = "underperforming（キル・生存ともに期待以下）"
    else:
        style = None

    OBJ_FEATURE_COLS: dict[str, list[str]] = {
        "CTF":         ["flag_captures", "flag_grabs", "flag_carrier_time_sec", "flag_carriers_killed"],
        "Oddball":     ["oddball_skull_time_sec", "oddball_skull_grabs", "oddball_skulls_denied"],
        "KOTH":        ["zone_occupation_sec", "zone_def_kills", "zone_off_kills"],
        "Strongholds": ["zone_occupation_sec", "zone_captures", "zone_secures",
                        "zone_def_kills", "zone_off_kills"],
    }
    obj_by_rule: dict[str, Any] = {}
    for rule_key, cols in OBJ_FEATURE_COLS.items():
        grp = df[df["rule_name"] == rule_key]
        if len(grp) < 3:
            continue
        obj_entry: dict[str, Any] = {"matches": len(grp)}
        for col in cols:
            if col in grp.columns and grp[col].notna().any():
                obj_entry[col + "_mean"] = _safe_round(grp[col].mean(), 2)
        obj_by_rule[rule_key] = obj_entry

    return {
        "tsi":                  tsi,
        "dtr":                  dtr,
        "dpm":                  dpm,
        "survival_index_sec":   survival_index,
        "k_rpi_std":            k_rpi_std,
        "perfect_rate_mean":    perfect_rate_mean,
        "style_classification": style,
        "solo_win_rate":        solo_wr,
        "party_win_rate":       party_wr,
        "pw_control_win_corr":  pw_win_corr,
        "engagement_by_rule":   eng_by_rule,
        "obj_stats_by_rule":    obj_by_rule,
        "win_loss_delta":       _build_win_loss_delta(df),
        "recent_vs_baseline":   _build_recent_vs_baseline(df),
    }


def _build_map_mode_matrix(df: pd.DataFrame) -> dict[str, Any]:
    """
    A-4. map_mode_matrix（マップ×ルール表）。
    map_name × rule_name ごとの勝率・KDA平均・試合数。
    """
    matrix: dict[str, Any] = {}

    for (map_name, rule_name), grp in df.groupby(["map_name", "rule_name"]):
        n = len(grp)
        key = f"{map_name} / {rule_name}"
        win_rate = _safe_round(grp["result_flag"].mean(), 3) if n > 0 else None
        kda_mean = _safe_round(grp["kda"].mean(), 2) if n > 0 else None

        if n < 3:
            confidence = "low"
        elif n < 5:
            confidence = "medium"
        else:
            confidence = "high"

        matrix[key] = {
            "map":        str(map_name),
            "rule":       str(rule_name),
            "matches":    n,
            "win_rate":   win_rate,
            "kda_mean":   kda_mean,
            "confidence": confidence,
        }

    return matrix


def _build_summary(df: pd.DataFrame) -> dict[str, Any]:
    """集計サマリー全体を構築する。"""
    summary: dict[str, Any] = {}

    summary["overall"]     = _agg_group(df)

    summary["by_playlist"] = {}
    for pl, grp in df.groupby("playlist"):
        label = PLAYLIST_DISPLAY.get(str(pl), str(pl))
        summary["by_playlist"][label] = _agg_group(grp)

    summary["by_map"] = {}
    for map_name, grp in df.groupby("map_name"):
        if len(grp) < 5:
            continue
        summary["by_map"][str(map_name)] = _agg_group(grp)

    OBJ_COLS: dict[str, list[str]] = {
        "Slayer":      [],
        "CTF":         ["flag_captures", "flag_grabs", "flag_returns", "flag_secures",
                        "flag_steals", "flag_carrier_time_sec", "flag_carriers_killed"],
        "Oddball":     ["oddball_skull_time_sec", "oddball_scoring_ticks",
                        "oddball_skull_grabs", "oddball_carrier_kills", "oddball_skulls_denied"],
        "KOTH":        ["zone_occupation_sec", "zone_scoring_ticks",
                        "zone_def_kills", "zone_off_kills"],
        "Strongholds": ["zone_occupation_sec", "zone_scoring_ticks", "zone_captures",
                        "zone_def_kills", "zone_off_kills", "zone_secures"],
    }

    summary["by_rule"] = {}
    for rule_name, grp in df.groupby("rule_name"):
        if len(grp) < 3:
            continue
        rule_data = _agg_group(grp)
        rule_key  = str(rule_name)
        obj_cols  = OBJ_COLS.get(rule_key, [])
        if obj_cols:
            obj_agg: dict[str, Any] = {}
            for col in obj_cols:
                if col in grp.columns and grp[col].notna().any():
                    obj_agg[col + "_mean"] = _safe_round(grp[col].mean(), 2)
            if obj_agg:
                rule_data["obj_stats"] = obj_agg
        summary["by_rule"][rule_key] = rule_data

    summary["by_party"] = {}
    for pt, grp in df.groupby("party_type"):
        summary["by_party"][str(pt)] = _agg_group(grp)

    if "session_seq" in df.columns:
        fatigue = (
            df.dropna(subset=["kda", "session_seq"])
            .groupby("session_seq")["kda"]
            .agg(mean="mean", count="count")
            .reset_index()
            .query("count >= 3")
        )
        summary["session_fatigue"] = {
            int(row["session_seq"]): _safe_round(row["mean"], 2)
            for _, row in fatigue.iterrows()
        }

    summary["recent_20"]        = _agg_group(df.tail(20))
    summary["map_mode_matrix"]  = _build_map_mode_matrix(df)

    return summary


def _build_matches_sample(df: pd.DataFrame, stat_df: pd.DataFrame) -> dict[str, Any]:
    """直近20試合 + KDAベスト5 + ワースト5 を返す。"""
    cols = [c for c in EXPORT_COLUMNS if c in stat_df.columns]

    def _to_records(sub: pd.DataFrame) -> list[dict]:
        sub = sub[cols].copy()
        if "played_at" in sub.columns:
            sub["played_at"] = (
                sub["played_at"].dt.tz_convert("Asia/Tokyo").dt.strftime("%Y-%m-%d %H:%M")
            )
        if "playlist" in sub.columns:
            sub["playlist"] = sub["playlist"].map(lambda x: PLAYLIST_DISPLAY.get(str(x), str(x)))
        if "result" in sub.columns:
            sub["result"] = sub["result"].map(lambda x: RESULT_DISPLAY.get(str(x), str(x)))
        return json.loads(sub.to_json(orient="records", force_ascii=False))

    recent_20 = stat_df.sort_values("played_at").tail(20)
    best_5    = stat_df.nlargest(5,  "kda")
    worst_5   = stat_df.nsmallest(5, "kda")

    return {
        "recent_20": _to_records(recent_20),
        "best_5":    _to_records(best_5),
        "worst_5":   _to_records(worst_5),
    }


# ==================================================
# メインエントリポイント
# ==================================================

def build_export(
    df_filtered: pd.DataFrame,
    filter_info: dict[str, str],
    my_xuid: str,
) -> str:
    """
    フィルター済みDataFrameからAI相談用JSONを生成して文字列で返す。
    """
    stat_df = df_filtered[df_filtered["exclude_flag"] == ""].copy()

    now_jst    = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_range = ""
    if not stat_df.empty and "played_at" in stat_df.columns:
        dates      = stat_df["played_at"].dt.tz_convert("Asia/Tokyo")
        date_range = f"{dates.min().strftime('%Y-%m-%d')} 〜 {dates.max().strftime('%Y-%m-%d')}"

    meta = {
        "generated_at":   now_jst,
        "player_xuid":    my_xuid,
        "export_matches": len(stat_df),
        "date_range":     date_range,
        "filter":         filter_info,
    }

    export = {
        "meta":               meta,
        "analysis_contract":  ANALYSIS_CONTRACT,
        "suggested_prompt":   SUGGESTED_PROMPT,
        "metric_limitations": METRIC_LIMITATIONS,
        "game_context":       build_relevant_context(stat_df),   # B-4: 絞り込み済み
        "glossary":           GLOSSARY,
        "features":           _build_features(stat_df),
        "summary":            _build_summary(stat_df),
        "matches":            _build_matches_sample(df_filtered, stat_df),
    }

    return json.dumps(export, ensure_ascii=False, indent=2)