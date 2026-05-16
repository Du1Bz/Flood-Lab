"""
logic/metrics.py
----------------
計算指標の追加。database.py が作った DataFrame を受け取り、列を追加して返す。

含まれる処理:
- 基本レート系: kd_ratio, kda, accuracy, damage_diff, etc.
- 時間正規化: kpm, dpm, damage_dealt_per_min, etc.
- TrueSkill2 系: k_rpi, d_rpi, lgai, impact_score
- eMMR v1: calc_emmr (AvgCSR20 ベース)
- eMMR v2: batch_calc_emmr_v2 (カルマンフィルタ)
"""

from __future__ import annotations

import math
from collections import defaultdict
from typing import Any

import numpy as np
import pandas as pd

from src.utils.helpers import safe_number


# ==================================================
# 基本レート系・時間正規化指標
# ==================================================

def add_basic_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """基本レート系・時間正規化指標を追加する。"""
    if df.empty:
        return df

    df = df.copy()

    # K/D（デス=0のときキル数をそのまま使う）
    df["kd_ratio"] = df.apply(
        lambda r: r["kills"] if r["deaths"] == 0 else r["kills"] / r["deaths"],
        axis=1,
    ).round(2)

    # KDA
    df["kda"] = (df["kills"] - df["deaths"] + df["assists"] / 3).round(2)

    # 命中率（0除算は None）
    df["accuracy"] = df.apply(
        lambda r: round(r["shots_hit"] / r["shots_fired"], 4)
        if r["shots_fired"] > 0 else None,
        axis=1,
    )

    # ダメージ差
    df["damage_diff"] = df["damage_dealt"] - df["damage_taken"]

    # キル効率・デス効率・パーフェクト率（0除算は None）
    df["kill_efficiency"] = df.apply(
        lambda r: round(r["damage_dealt"] / (r["kills"] + r["assists"] / 3), 1)
        if (r["kills"] + r["assists"] / 3) > 0 else None,
        axis=1,
    )
    df["death_efficiency"] = df.apply(
        lambda r: round(r["damage_taken"] / r["deaths"], 1)
        if r["deaths"] > 0 else None,
        axis=1,
    )
    df["perfect_rate"] = df.apply(
        lambda r: round(r["perfect_kills"] / r["kills"], 4)
        if r["kills"] > 0 else None,
        axis=1,
    )

    # 時間正規化（duration_sec=0 or None は None）
    dur_min = df["duration_sec"].apply(
        lambda s: s / 60 if s and s > 0 else None
    )
    df["kpm"]                  = (df["kills"]        / dur_min).round(3)
    df["dpm"]                  = (df["deaths"]       / dur_min).round(3)
    df["damage_dealt_per_min"] = (df["damage_dealt"] / dur_min).round(1)
    df["damage_taken_per_min"] = (df["damage_taken"] / dur_min).round(1)
    df["power_kill_density"]   = (df["power_kills"]  / dur_min).round(3)

    return df


# ==================================================
# TrueSkill2 系指標
# ==================================================

def add_trueskill_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """K-RPI・D-RPI・LGAI・インパクトスコア・生存貢献度を追加する。"""
    if df.empty:
        return df

    df = df.copy()

    # K-RPI（期待キルに対する実績の比率）
    df["k_rpi"] = df.apply(
        lambda r: round(r["kills"] / float(r["expected_kills"]), 3)
        if pd.notna(r.get("expected_kills")) and float(r["expected_kills"]) > 0 else None,
        axis=1,
    )

    # D-RPI（期待デスに対して実際に少なく死んだ比率）
    df["d_rpi"] = df.apply(
        lambda r: round(float(r["expected_deaths"]) / r["deaths"], 3)
        if pd.notna(r.get("expected_deaths")) and r["deaths"] > 0 else None,
        axis=1,
    )

    # LGAI（ロビー格差補正インパクト）
    df["lgai"] = df.apply(
        lambda r: round(float(r["enemy_mmr"]) - float(r["csr_pre"]), 1)
        if pd.notna(r.get("enemy_mmr")) and pd.notna(r.get("csr_pre")) else None,
        axis=1,
    )

    # インパクトスコア
    df["impact_score"] = df.apply(
        lambda r: round((r["k_rpi"] + r["d_rpi"]) / 2, 3)
        if pd.notna(r.get("k_rpi")) and pd.notna(r.get("d_rpi")) else None,
        axis=1,
    )

    # 生存貢献度
    df["survival_contribution"] = df.apply(
        lambda r: round(
            (float(r["expected_deaths"]) - r["deaths"]) * (float(r["enemy_mmr"]) / float(r["csr_pre"])), 2
        )
        if (pd.notna(r.get("expected_deaths"))
            and pd.notna(r.get("enemy_mmr"))
            and pd.notna(r.get("csr_pre")) and float(r["csr_pre"]) > 0) else None,
        axis=1,
    )

    return df


# ==================================================
# CSR 増減
# ==================================================

def add_csr_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """CSR 増減を追加する。"""
    if df.empty:
        return df

    df = df.copy()
    df["csr_delta"] = df.apply(
        lambda r: int(r["csr_post"] - r["csr_pre"])
        if pd.notna(r["csr_post"]) and pd.notna(r["csr_pre"]) else None,
        axis=1,
    )
    return df


# ==================================================
# AvgCSR20 の計算
# ==================================================

def add_avg_csr20(df: pd.DataFrame) -> pd.DataFrame:
    """
    プレイリストごとに直近20試合の試合前CSR移動平均を計算して追加する。
    df は played_at 昇順でソート済みであることを前提とする。
    """
    if df.empty:
        return df

    df = df.copy()
    avg_csr_list: list[float | None] = [None] * len(df)
    csr_history: dict[str, list[float]] = defaultdict(list)

    for i, row in df.iterrows():
        playlist = row.get("playlist")
        csr_pre  = row.get("csr_pre")
        if playlist and pd.notna(csr_pre):
            csr_history[playlist].append(float(csr_pre))
            window = csr_history[playlist][-20:]
            avg_csr_list[i] = round(sum(window) / len(window), 2)

    df["csr_avg20"] = avg_csr_list
    return df


# ==================================================
# eMMR v1
# ==================================================

def add_emmr_v1(df: pd.DataFrame) -> pd.DataFrame:
    """
    eMMR v1 を計算して emmr_post / emmr_pre / emmr_delta を追加する。

    式:
        eMMR = AvgCSR20 + 200 × ln((実K+1) / (期待K+1)) - Penalty
        Penalty = min((party_size-1)/3 × 50, 50)
    """
    if df.empty:
        return df

    df = df.copy()
    emmr_list: list[float | None] = []

    for _, row in df.iterrows():
        avg_csr      = row.get("csr_avg20")
        expected_k   = row.get("expected_kills")
        actual_k     = row.get("kills")
        party        = row.get("party_size") or 1

        if pd.isna(avg_csr) or pd.isna(expected_k) or pd.isna(actual_k):
            emmr_list.append(None)
            continue

        try:
            k_ratio = (float(actual_k) + 1) / (float(expected_k) + 1)
            emmr    = float(avg_csr) + 200 * math.log(k_ratio)
        except (ValueError, ZeroDivisionError):
            emmr_list.append(None)
            continue

        penalty = min((party - 1) / 3 * 50, 50)
        emmr_list.append(round(emmr - penalty, 2))

    df["emmr_post"]  = emmr_list
    # emmr_pre は前試合の emmr_post
    df["emmr_pre"]   = df["emmr_post"].shift(1)
    df["emmr_delta"] = (df["emmr_post"] - df["emmr_pre"]).round(2)
    return df


# ==================================================
# eMMR v2（カルマンフィルタ）
# ==================================================

def add_emmr_v2(df: pd.DataFrame) -> pd.DataFrame:
    """
    eMMR v2 をカルマンフィルタで計算して emmr_v2 / emmr_v2_sigma を追加する。
    df は played_at 昇順でソート済みであることを前提とする。
    """
    if df.empty:
        return df

    df = df.copy()

    DEFAULT_MU_MAP = {
        "ranked_arena":  900.0,
        "ranked_slayer": 1200.0,
    }
    GLOBAL_DEFAULT_MU = 1000.0

    df["emmr_v2"]       = np.nan
    df["emmr_v2_sigma"] = np.nan

    # k_ratio
    df["_k_ratio"] = (df["kills"].astype(float) + 1) / (
        df["expected_kills"].fillna(1).astype(float) + 1
    )

    for playlist, group in df.groupby("playlist"):
        group = group.sort_values("played_at")
        idxs  = group.index

        k_mean, k_std = group["_k_ratio"].mean(), group["_k_ratio"].std() or 1.0
        k_z = (group["_k_ratio"] - k_mean) / k_std

        dmg = group["damage_dealt"].astype(float)
        dmg_z = (dmg - dmg.mean()) / (dmg.std() or 1.0)

        ast = group["assists"].astype(float)
        ast_z = (ast - ast.mean()) / (ast.std() or 1.0)

        # 初期値
        first_valid = group["csr_pre"].dropna()
        mu       = float(first_valid.iloc[0]) if not first_valid.empty \
                   else DEFAULT_MU_MAP.get(str(playlist), GLOBAL_DEFAULT_MU)
        sigma_sq = 10000.0

        Q      = 400.0
        R_PERF = 20.0
        R_CSR  = 50.0

        for idx in idxs:
            row = group.loc[idx]

            # 予測ステップ
            mu_prior       = mu
            sigma_sq_prior = sigma_sq + Q

            # 更新1: 複合スタッツ
            perf_z    = k_z[idx] * 0.6 + dmg_z[idx] * 0.3 + ast_z[idx] * 0.1
            perf_delta = perf_z * 50.0

            party_count  = row.get("party_size") or 1
            party_penalty = (party_count - 1) * 8.0
            meas_perf = mu_prior + perf_delta - party_penalty

            k_gain_perf = sigma_sq_prior / (sigma_sq_prior + R_PERF)
            mu       = mu_prior + k_gain_perf * (meas_perf - mu_prior)
            sigma_sq = (1 - k_gain_perf) * sigma_sq_prior

            mu_prior, sigma_sq_prior = mu, sigma_sq

            # 更新2: CSR ストッパー
            csr = row.get("csr_post")
            if pd.notna(csr):
                k_gain_csr = sigma_sq_prior / (sigma_sq_prior + R_CSR)
                mu       = mu_prior + k_gain_csr * (float(csr) - mu_prior)
                sigma_sq = (1 - k_gain_csr) * sigma_sq_prior

            df.at[idx, "emmr_v2"]       = round(mu, 1)
            df.at[idx, "emmr_v2_sigma"] = round(np.sqrt(sigma_sq), 1)

    df.drop(columns=["_k_ratio"], inplace=True)
    return df