"""
logic/export_features.py
-------------------------
E-2. build_role_profile : ロール傾向スコアの計算
E-3. 追加特徴量の計算

シグナルを0/1でカウントして0〜1のスコアを算出する単純カウント方式。
サンプル数が少ない場合はスコアの信頼度を下げる。
"""

from __future__ import annotations
from typing import Any

import numpy as np
import pandas as pd


def _safe_round(val: Any, decimals: int = 3) -> Any:
    if val is None:
        return None
    try:
        f = float(val)
        return None if not np.isfinite(f) else round(f, decimals)
    except (TypeError, ValueError):
        return None


# ==================================================
# E-3. 追加特徴量
# ==================================================

def calc_assist_ratio(df: pd.DataFrame) -> float | None:
    """assists / (kills + assists)"""
    k = df["kills"].sum()
    a = df["assists"].sum()
    return _safe_round(a / (k + a), 3) if (k + a) > 0 else None


def calc_ego_challenge_risk(df: pd.DataFrame) -> str | None:
    """
    ego_challenge_risk_proxy: 無理な撃ち合いリスクの疑い。
    damage_taken_per_min 高 かつ d_rpi 低で判定。
    """
    dtp = df["damage_taken"].sum() / (df["duration_sec"].sum() / 60) \
        if "duration_sec" in df.columns and df["duration_sec"].sum() > 0 else None
    d_rpi = df["d_rpi"].mean() if "d_rpi" in df.columns else None

    if dtp is None or d_rpi is None:
        return None

    # 全体の damage_taken_per_min 中央値と比較するため固定閾値で近似
    # 高い = 200以上/分（目安）、d_rpi < 1.0
    high_dtp = dtp > 200
    low_drpi = d_rpi < 1.0

    if high_dtp and low_drpi:
        return "high"
    elif high_dtp or low_drpi:
        return "medium"
    else:
        return "low"


def calc_passivity_proxy(df: pd.DataFrame) -> str | None:
    """
    passivity_proxy: 生存はできているが圧が低い疑い。
    d_rpi 高 かつ k_rpi 低 かつ engagement_density 低で判定。
    """
    d_rpi = df["d_rpi"].mean() if "d_rpi" in df.columns else None
    k_rpi = df["k_rpi"].mean() if "k_rpi" in df.columns else None
    eng   = df["engagement_density"].mean() if "engagement_density" in df.columns else None

    if any(v is None for v in [d_rpi, k_rpi, eng]):
        return None

    signals = [
        d_rpi >= 1.1,
        k_rpi < 0.9,
        eng < df["engagement_density"].quantile(0.35) if len(df) >= 5 else eng < 4.5,
    ]
    count = sum(signals)
    if count >= 3:
        return "high"
    elif count == 2:
        return "medium"
    else:
        return "low"


def calc_objective_presence(df: pd.DataFrame) -> dict[str, Any]:
    """ルール別オブジェクト関与スコア（0〜1）"""
    result: dict[str, Any] = {}

    rule_obj_map = {
        "CTF":         ["flag_captures", "flag_grabs", "flag_returns", "flag_carriers_killed"],
        "Oddball":     ["oddball_skull_time_sec", "oddball_skull_grabs", "oddball_skulls_denied"],
        "KOTH":        ["zone_occupation_sec", "zone_def_kills", "zone_off_kills"],
        "Strongholds": ["zone_occupation_sec", "zone_captures", "zone_secures",
                        "zone_def_kills", "zone_off_kills"],
    }

    for rule, cols in rule_obj_map.items():
        grp = df[df["rule_name"] == rule]
        if len(grp) < 3:
            continue
        available = [c for c in cols if c in grp.columns and grp[c].notna().any()]
        if not available:
            continue
        # 各指標が上位50%以上なら1
        signals = []
        for col in available:
            median = grp[col].median()
            mean   = grp[col].mean()
            signals.append(1 if mean >= median else 0)
        result[rule] = _safe_round(sum(signals) / len(signals), 2)

    return result


# ==================================================
# E-2. build_role_profile（ロール傾向スコア）
# ==================================================

def build_role_profile(df: pd.DataFrame) -> dict[str, Any]:
    """
    E-2. ロール傾向スコアを計算して返す。

    各ロールのポジティブシグナルを満たした割合を0〜1のスコアとして算出。
    primary / secondary tendency を特定し、coaching_hints を付与する。
    """
    if df.empty or len(df) < 3:
        return {
            "note": "サンプル数不足のため推定不可（3試合以上必要）",
            "scores": {},
        }

    n = len(df)

    # ---- 基礎指標の計算 ----
    k_rpi_mean = df["k_rpi"].mean()
    d_rpi_mean = df["d_rpi"].mean()
    assist_ratio = calc_assist_ratio(df)
    eng_mean = df["engagement_density"].mean() if "engagement_density" in df.columns else None
    dpm_mean = df["damage_dealt_per_min"].mean() if "damage_dealt_per_min" in df.columns else None
    pw_mean  = df["pw_control_rate"].mean() if "pw_control_rate" in df.columns else None

    # damage_taken_per_min（duration_secがあれば計算）
    dtp_mean = None
    if "duration_sec" in df.columns and df["duration_sec"].sum() > 0:
        dtp_mean = df["damage_taken"].sum() / (df["duration_sec"].sum() / 60)

    obj_presence = calc_objective_presence(df)
    obj_score_mean = float(np.mean(list(obj_presence.values()))) if obj_presence else None

    # ---- ロール別シグナルカウント ----
    def _score(signals: list[bool | None]) -> float:
        valid = [s for s in signals if s is not None]
        return round(sum(valid) / len(valid), 2) if valid else 0.0

    scores: dict[str, float] = {}

    # slayer
    scores["slayer"] = _score([
        k_rpi_mean >= 1.0 if pd.notna(k_rpi_mean) else None,
        dpm_mean is not None and dpm_mean >= df["damage_dealt_per_min"].quantile(0.6) if "damage_dealt_per_min" in df.columns and len(df) >= 5 else None,
        k_rpi_mean >= 1.0 and d_rpi_mean >= 0.95 if pd.notna(k_rpi_mean) and pd.notna(d_rpi_mean) else None,
    ])

    # support
    scores["support"] = _score([
        assist_ratio is not None and assist_ratio >= 0.35,
        dpm_mean is not None and dpm_mean >= df["damage_dealt_per_min"].quantile(0.4) if "damage_dealt_per_min" in df.columns and len(df) >= 5 else None,
        d_rpi_mean >= 0.95 and d_rpi_mean <= 1.15 if pd.notna(d_rpi_mean) else None,
    ])

    # objective_player
    scores["objective_player"] = _score([
        obj_score_mean is not None and obj_score_mean >= 0.4,
        eng_mean is not None and eng_mean >= df["engagement_density"].quantile(0.4) if "engagement_density" in df.columns and len(df) >= 5 else None,
    ])

    # anchor
    scores["anchor"] = _score([
        d_rpi_mean >= 1.05 if pd.notna(d_rpi_mean) else None,
        df["deaths"].mean() <= df["deaths"].quantile(0.45) if len(df) >= 5 else None,
        df["damage_diff"].mean() >= 0 if "damage_diff" in df.columns else None,
    ])

    # entry
    scores["entry"] = _score([
        eng_mean is not None and eng_mean >= df["engagement_density"].quantile(0.55) if "engagement_density" in df.columns and len(df) >= 5 else None,
        dtp_mean is not None and dtp_mean >= 180,
        assist_ratio is not None and 0.2 <= assist_ratio <= 0.5,
    ])

    # power_item_controller
    scores["power_item_controller"] = _score([
        pw_mean is not None and pw_mean >= 0.55,
        pw_mean is not None and pw_mean >= 0.5,
    ])

    # ---- primary / secondary tendency ----
    sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary   = sorted_roles[0][0] if sorted_roles[0][1] > 0 else None
    secondary = sorted_roles[1][0] if len(sorted_roles) > 1 and sorted_roles[1][1] > 0 else None

    # ---- evidence（根拠シグナル）----
    evidence: dict[str, list[str]] = {}
    if primary == "slayer" and k_rpi_mean >= 1.0:
        evidence["slayer"] = [f"k_rpi_mean={_safe_round(k_rpi_mean,3)}（≥1.0）"]
    if primary == "support" or secondary == "support":
        if assist_ratio is not None:
            evidence["support"] = [f"assist_ratio={_safe_round(assist_ratio,3)}"]
    if obj_presence:
        evidence["objective_player"] = [f"{rule}: obj_presence={v}" for rule, v in obj_presence.items()]

    # ---- coaching_hints（E-5）----
    from src.logic.halo_knowledge.roles import ROLES
    coaching_hints: list[str] = []
    if primary and primary in ROLES:
        coaching_hints = ROLES[primary].get("coaching_hints", [])

    # ---- 信頼度 ----
    if n < 5:
        confidence = "low"
    elif n < 10:
        confidence = "medium"
    else:
        confidence = "high"

    return {
        "label_ja":          "ロール傾向",
        "sample_n":          n,
        "confidence":        confidence,
        "primary_tendency":  primary,
        "primary_label_ja":  ROLES[primary]["label_ja"] if primary and primary in ROLES else None,
        "secondary_tendency": secondary,
        "secondary_label_ja": ROLES[secondary]["label_ja"] if secondary and secondary in ROLES else None,
        "scores":            scores,
        "evidence":          evidence,
        "coaching_hints":    coaching_hints,
        "caution": (
            "ロールは固定職ではなくこの期間のデータから見た傾向。"
            "チーム構成・味方の役割・VC・位置情報は観測できないため断定しないこと。"
        ),
        # 追加特徴量（E-3）
        "ego_challenge_risk":  calc_ego_challenge_risk(df),
        "passivity_proxy":     calc_passivity_proxy(df),
        "assist_ratio":        _safe_round(assist_ratio, 3),
        "objective_presence":  obj_presence,
    }
