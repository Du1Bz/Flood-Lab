"""
logic/insights.py
-----------------
インサイトエンジン（Lv.2 統計ベース）。

processor.py が生成した DataFrame を受け取り、
統計的に有意な異常・傾向を検出してインサイトリストを返す。

設計方針:
- 各検出関数は独立していて副作用なし
- 閾値はモジュール先頭の定数で管理（ハードコード・実運用で調整）
- 返り値は list[Insight]（辞書のリスト）
  各要素: {"category": str, "level": str, "title": str, "body": str}
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats as scipy_stats


# ==================================================
# 閾値定数（実運用で調整する）
# ==================================================

# パフォーマンス系
SLUMP_WINDOW        = 10    # 直近N戦
SLUMP_SIGMA         = 1.0   # 移動平均からの乖離閾値
LOSS_STREAK_MIN     = 5     # 連敗アラートの最小連敗数

# 弱点検出系
WEAKNESS_MIN_GAMES  = 10    # 最低試合数
WEAKNESS_CI         = 0.95  # 信頼区間

# TrueSkill2 系
KRPI_LOW_THRESHOLD  = 1.0   # K-RPI がこれを下回り続けると検出
KRPI_WINDOW         = 10
DRPI_HIGH           = 1.1
KRPI_LOW            = 0.9
TRUESKILL_MAJORITY  = 0.5   # 直近Nのうち何割以上で条件を満たすか

# ロビー系
LGAI_WINDOW         = 5     # 直近N戦すべて格上なら検出

# セッション疲労系
FATIGUE_CORR_THRESHOLD = -0.4   # KDAとセッション内試合番号の相関閾値
FATIGUE_MIN_SESSIONS   = 3      # 最低セッション数


# ==================================================
# Insight データクラス
# ==================================================

@dataclass
class Insight:
    category: str   # "performance" | "weakness" | "trueskill" | "lobby" | "fatigue"
    level: str      # "info" | "warning" | "alert"
    title: str
    body: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


# ==================================================
# ヘルパー
# ==================================================

def _wilson_lower(wins: int, n: int, ci: float = 0.95) -> float:
    """Wilson スコア区間の下限を返す。"""
    if n == 0:
        return 0.0
    z = scipy_stats.norm.ppf(1 - (1 - ci) / 2)
    p = wins / n
    denom = 1 + z ** 2 / n
    centre = p + z ** 2 / (2 * n)
    margin = z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2))
    return (centre - margin) / denom


def _overall_winrate(df: pd.DataFrame) -> float:
    return df["result_flag"].mean() if len(df) > 0 else 0.5


# ==================================================
# 検出関数群
# ==================================================

def detect_slump(df: pd.DataFrame) -> list[Insight]:
    """
    直近SLUMP_WINDOW戦のKDA / Accuracyが
    過去移動平均からSLUMP_SIGMA σ以上低下していれば検出。
    """
    insights: list[Insight] = []
    if len(df) < SLUMP_WINDOW * 2:
        return insights

    for col, label in [("kda", "KDA"), ("accuracy", "命中率")]:
        series = df[col].dropna()
        if len(series) < SLUMP_WINDOW * 2:
            continue

        recent  = series.iloc[-SLUMP_WINDOW:]
        history = series.iloc[:-SLUMP_WINDOW]

        hist_mean = history.mean()
        hist_std  = history.std()
        if hist_std == 0:
            continue

        recent_mean = recent.mean()
        z = (recent_mean - hist_mean) / hist_std

        if z < -SLUMP_SIGMA:
            insights.append(Insight(
                category="performance",
                level="warning",
                title=f"📉 {label}スランプの可能性",
                body=(
                    f"直近{SLUMP_WINDOW}試合の平均{label}（{recent_mean:.3f}）が"
                    f"過去平均（{hist_mean:.3f}）より"
                    f"{abs(z):.1f}σ低下しています。"
                ),
            ))

    return insights


def detect_loss_streak(df: pd.DataFrame) -> list[Insight]:
    """直近5セッション内でLOSS_STREAK_MIN連敗以上を検出。"""
    insights: list[Insight] = []
    if "session_id" not in df.columns:
        return insights

    # 直近5セッションのみ対象（全期間だと過去の記録が大量に出る）
    recent_sessions = sorted(df["session_id"].dropna().unique())[-5:]

    for sid in recent_sessions:
        group = df[df["session_id"] == sid].sort_values("session_seq")
        streak = 0
        max_streak = 0
        for flag in group["result_flag"]:
            if flag == 0:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 0
        if max_streak >= LOSS_STREAK_MIN:
            insights.append(Insight(
                category="performance",
                level="alert",
                title=f"🚨 セッション{sid}で{max_streak}連敗",
                body=(
                    f"セッション{sid}内で{max_streak}連敗が発生しています。"
                    "やめどきのサインかもしれません。"
                ),
            ))

    return insights


def detect_weak_maps(df: pd.DataFrame) -> list[Insight]:
    """
    マップ別勝率の95%信頼区間の上限が全体平均を下回り、
    かつWEAKNESS_MIN_GAMES試合以上あれば検出。
    """
    insights: list[Insight] = []
    overall_wr = _overall_winrate(df)

    for map_name, group in df.groupby("map_name"):
        n = len(group)
        if n < WEAKNESS_MIN_GAMES:
            continue
        wins = group["result_flag"].sum()
        wr   = wins / n
        lower = _wilson_lower(wins, n, WEAKNESS_CI)
        upper = 1 - _wilson_lower(n - wins, n, WEAKNESS_CI)

        if upper < overall_wr:
            insights.append(Insight(
                category="weakness",
                level="warning",
                title=f"🗺️ 苦手マップ: {map_name}",
                body=(
                    f"勝率 {wr:.1%}（{n}試合）、"
                    f"95%信頼区間 [{lower:.1%}, {upper:.1%}]。"
                    f"全体平均（{overall_wr:.1%}）を統計的に下回っています。"
                ),
            ))

    return insights


def detect_weak_rules(df: pd.DataFrame) -> list[Insight]:
    """ルール別KDAの95%信頼区間の上限が全体平均を下回れば検出。"""
    insights: list[Insight] = []
    overall_kda = df["kda"].mean()

    for rule_name, group in df.groupby("rule_name"):
        n = len(group)
        if n < WEAKNESS_MIN_GAMES:
            continue
        kda_vals = group["kda"].dropna()
        if len(kda_vals) < WEAKNESS_MIN_GAMES:
            continue

        mean = kda_vals.mean()
        se   = kda_vals.sem()
        if se == 0:
            continue

        t_crit = scipy_stats.t.ppf(1 - (1 - WEAKNESS_CI) / 2, df=len(kda_vals) - 1)
        upper  = mean + t_crit * se

        if upper < overall_kda:
            insights.append(Insight(
                category="weakness",
                level="warning",
                title=f"🎮 苦手ルール: {rule_name}",
                body=(
                    f"KDA平均 {mean:.2f}（{n}試合）、"
                    f"95%信頼区間の上限 {upper:.2f}。"
                    f"全体平均（{overall_kda:.2f}）を統計的に下回っています。"
                ),
            ))

    return insights


def detect_weak_party(df: pd.DataFrame) -> list[Insight]:
    """パーティタイプ別勝率の信頼区間が全体平均を下回れば検出。"""
    insights: list[Insight] = []
    overall_wr = _overall_winrate(df)

    for ptype, group in df.groupby("party_type"):
        n = len(group)
        if n < WEAKNESS_MIN_GAMES:
            continue
        wins  = group["result_flag"].sum()
        wr    = wins / n
        lower = _wilson_lower(wins, n, WEAKNESS_CI)
        upper = 1 - _wilson_lower(n - wins, n, WEAKNESS_CI)

        if upper < overall_wr:
            insights.append(Insight(
                category="weakness",
                level="warning",
                title=f"👥 {ptype}編成が弱点",
                body=(
                    f"勝率 {wr:.1%}（{n}試合）、"
                    f"95%信頼区間 [{lower:.1%}, {upper:.1%}]。"
                    f"全体平均（{overall_wr:.1%}）を統計的に下回っています。"
                ),
            ))

    return insights


def detect_krpi_low(df: pd.DataFrame) -> list[Insight]:
    """K-RPIが直近KRPI_WINDOW戦で連続して1.0未満なら検出。"""
    insights: list[Insight] = []
    krpi = df["k_rpi"].dropna()
    if len(krpi) < KRPI_WINDOW:
        return insights

    recent = krpi.iloc[-KRPI_WINDOW:]
    if (recent < KRPI_LOW_THRESHOLD).all():
        avg = recent.mean()
        insights.append(Insight(
            category="trueskill",
            level="warning",
            title="⚔️ キル不足パターン",
            body=(
                f"直近{KRPI_WINDOW}試合すべてでK-RPIが1.0未満"
                f"（平均 {avg:.3f}）。"
                "期待キル数を継続的に下回っています。"
                "ポジション・エンゲージのタイミングを見直してみてください。"
            ),
        ))

    return insights


def detect_survive_but_no_kills(df: pd.DataFrame) -> list[Insight]:
    """
    D-RPI > DRPI_HIGH かつ K-RPI < KRPI_LOW が
    直近KRPI_WINDOW戦の過半数なら検出。
    """
    insights: list[Insight] = []
    recent = df.tail(KRPI_WINDOW).copy()
    valid  = recent.dropna(subset=["k_rpi", "d_rpi"])
    if len(valid) < KRPI_WINDOW // 2:
        return insights

    mask = (valid["d_rpi"] > DRPI_HIGH) & (valid["k_rpi"] < KRPI_LOW)
    ratio = mask.mean()

    if ratio > TRUESKILL_MAJORITY:
        insights.append(Insight(
            category="trueskill",
            level="info",
            title="🛡️ 生存できているがキルが取れていない",
            body=(
                f"直近{KRPI_WINDOW}試合の {ratio:.0%} で "
                f"D-RPI > {DRPI_HIGH}（生存良好）かつ"
                f"K-RPI < {KRPI_LOW}（キル不足）のパターンが出ています。"
                "アグレッションを上げるタイミングを探ってみてください。"
            ),
        ))

    return insights


def detect_lobby_disadvantage(df: pd.DataFrame) -> list[Insight]:
    """直近LGAI_WINDOW戦すべてLGAI > 0（格上ロビー）なら検出。"""
    insights: list[Insight] = []
    lgai = df["lgai"].dropna()
    if len(lgai) < LGAI_WINDOW:
        return insights

    recent = lgai.iloc[-LGAI_WINDOW:]
    if (recent > 0).all():
        avg_lgai = recent.mean()
        insights.append(Insight(
            category="lobby",
            level="info",
            title="📊 格上ロビーが連続しています",
            body=(
                f"直近{LGAI_WINDOW}試合すべてで格上相手（LGAI > 0）。"
                f"平均LGAI: {avg_lgai:.0f}。"
                "勝率や指標が下がっていても実力不足とは限りません。"
            ),
        ))

    return insights


def detect_session_fatigue(df: pd.DataFrame) -> list[Insight]:
    """
    セッション内の試合番号とKDAの相関がFATIGUE_CORR_THRESHOLD未満の
    セッションがFATIGUE_MIN_SESSIONS以上あれば検出。
    """
    insights: list[Insight] = []
    if "session_id" not in df.columns or "session_seq" not in df.columns:
        return insights

    fatigue_sessions = 0
    breakpoints: list[int] = []

    for sid, group in df.groupby("session_id"):
        group = group.sort_values("session_seq")
        if len(group) < 4:
            continue
        valid = group.dropna(subset=["kda", "session_seq"])
        if len(valid) < 4:
            continue

        r, p = scipy_stats.pearsonr(valid["session_seq"], valid["kda"])
        if r < FATIGUE_CORR_THRESHOLD:
            fatigue_sessions += 1
            # KDAが全体平均を下回り始める試合番号を推定
            mean_kda = valid["kda"].mean()
            above = valid[valid["kda"] >= mean_kda]["session_seq"]
            if len(above) > 0:
                breakpoints.append(int(above.max()))

    if fatigue_sessions >= FATIGUE_MIN_SESSIONS:
        avg_bp = int(np.mean(breakpoints)) if breakpoints else "不明"
        insights.append(Insight(
            category="fatigue",
            level="warning",
            title="😴 セッション後半のパフォーマンス低下",
            body=(
                f"{fatigue_sessions}セッションで試合を重ねるごとにKDAが低下する傾向があります。"
                f"平均的に{avg_bp}試合目あたりからパフォーマンスが落ち始めています。"
                "早めの休憩がおすすめです。"
            ),
        ))

    return insights


# ==================================================
# メインエントリポイント
# ==================================================

def run_insights(df: pd.DataFrame) -> list[dict[str, str]]:
    """
    全インサイト検出を実行してリストで返す。
    除外フラグのないデータのみを対象とする。

    Returns:
        list[dict]: [{"category", "level", "title", "body"}, ...]
        level: "info" | "warning" | "alert"
    """
    stat_df = df[df["exclude_flag"] == ""].copy()
    if stat_df.empty:
        return []

    results: list[Insight] = []
    results += detect_slump(stat_df)
    results += detect_loss_streak(stat_df)
    results += detect_weak_maps(stat_df)
    results += detect_weak_rules(stat_df)
    results += detect_weak_party(stat_df)
    results += detect_krpi_low(stat_df)
    results += detect_survive_but_no_kills(stat_df)
    results += detect_lobby_disadvantage(stat_df)
    results += detect_session_fatigue(stat_df)

    return [i.to_dict() for i in results]