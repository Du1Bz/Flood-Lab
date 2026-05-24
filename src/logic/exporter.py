"""
logic/exporter.py
-----------------
AI相談用データエクスポート。

フィルター済みDataFrameを受け取り、
生データ + 集計サマリー + 用語集 + プロンプト雛形を
1つのJSONファイルとして出力する。
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd

from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY

# ==================================================
# matchesに含めるカラム（中間計算値は省く）
# ==================================================

EXPORT_COLUMNS = [
    "match_id", "played_at", "playlist", "map_name", "rule_name",
    "result", "kills", "deaths", "assists",
    "kd_ratio", "kda", "accuracy",
    "damage_dealt", "damage_taken", "damage_diff",
    "k_rpi", "d_rpi", "lgai", "impact_score",
    "csr_pre", "csr_post", "csr_delta",
    "emmr_v2", "party_type",
    "session_id", "session_seq", "exclude_flag",
]

# ==================================================
# 用語集
# ==================================================

GLOSSARY: dict[str, str] = {
    "kd_ratio":     "K/D。キル数 / デス数。デス=0のときはキル数をそのまま使う",
    "kda":          "キル - デス + アシスト/3。試合の総合貢献度",
    "accuracy":     "命中率。命中数 / 発射数（0〜1の小数）",
    "damage_diff":  "与ダメージ - 被ダメージ。プラスが望ましい",
    "k_rpi":        "K-RPI（キル相対パフォーマンス指数）。TrueSkill2が予測した期待キル数に対する実績比率。1.0=期待通り、>1.0=期待超え、<1.0=期待以下",
    "d_rpi":        "D-RPI（デス相対パフォーマンス指数）。TrueSkill2が予測した期待デス数に対して実際に少なく死んだ比率。>1.0=期待より死ななかった（生存力が高い）",
    "lgai":         "LGAI（ロビー格差補正インパクト）。敵チームMMR - 自チームCSR。正の値=格上相手、負の値=格下相手",
    "impact_score": "インパクトスコア。(K-RPI + D-RPI) / 2。TrueSkill2基準の総合パフォーマンス指標。1.0=平均",
    "emmr_v2":      "eMMR v2（推定MMR）。カルマンフィルタで平滑化した独自推定MMR。ノイズを除いたスキルトレンドを表す",
    "csr_delta":    "CSR増減。1試合でのCSR変動量",
    "party_type":   "パーティタイプ。ソロ/デュオ/トリオ/フルパ",
    "session_seq":  "セッション内試合番号。同一セッション（2時間以内の連続プレイ）内での何試合目か",
    "exclude_flag": "除外フラグ。空文字=正常試合。short_match/incomplete/bot_match/low_shots/custom_non_rankedは統計除外対象",
    "playlist":     "区分。ranked_arena=ランクアリーナ, ranked_slayer=ランクスレイヤー, ranked_doubles=ランクダブルス, casual=カジュアル, custom=カスタムゲーム等",
}

# ==================================================
# プロンプト雛形
# ==================================================

SUGGESTED_PROMPT = (
    "以下はHalo Infiniteの試合データです。"
    "glossaryに各指標の定義があります。"
    "summaryの集計データとmatchesの生データをもとに、"
    "以下の観点からコーチングアドバイスをお願いします：\n"
    "1. 弱点マップ・苦手ルールの特定と改善ポイント\n"
    "2. TrueSkill2指標（K-RPI / D-RPI）から見たプレイスタイルの傾向\n"
    "3. パーティタイプ・セッション疲労など気になるパターン\n"
    "4. 直近の調子と伸びしろ"
)


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

    kills  = df["kills"].sum()
    deaths = df["deaths"].sum()

    return {
        "matches":       n,
        "win_rate":      _safe_round(df["result_flag"].mean(), 3),
        "kd_ratio":      _safe_round(kills / deaths if deaths > 0 else kills, 2),
        "kda_mean":      _safe_round(df["kda"].mean(), 2),
        "accuracy_mean": _safe_round(df["accuracy"].mean(), 3),
        "damage_diff_mean": _safe_round(df["damage_diff"].mean(), 0),
        "k_rpi_mean":    _safe_round(df["k_rpi"].mean(), 3),
        "d_rpi_mean":    _safe_round(df["d_rpi"].mean(), 3),
        "impact_mean":   _safe_round(df["impact_score"].mean(), 3),
        "csr_delta_sum": _safe_round(df["csr_delta"].sum(), 0),
    }


def _build_summary(df: pd.DataFrame) -> dict[str, Any]:
    """集計サマリー全体を構築する。"""
    summary: dict[str, Any] = {}

    # 全体
    summary["overall"] = _agg_group(df)

    # 区分別
    summary["by_playlist"] = {}
    for pl, grp in df.groupby("playlist"):
        label = PLAYLIST_DISPLAY.get(str(pl), str(pl))
        summary["by_playlist"][label] = _agg_group(grp)

    # マップ別（5試合以上）
    summary["by_map"] = {}
    for map_name, grp in df.groupby("map_name"):
        if len(grp) < 5:
            continue
        summary["by_map"][str(map_name)] = _agg_group(grp)

    # ルール別（3試合以上）
    summary["by_rule"] = {}
    for rule_name, grp in df.groupby("rule_name"):
        if len(grp) < 3:
            continue
        summary["by_rule"][str(rule_name)] = _agg_group(grp)

    # パーティタイプ別
    summary["by_party"] = {}
    for pt, grp in df.groupby("party_type"):
        summary["by_party"][str(pt)] = _agg_group(grp)

    # セッション疲労（試合番号ごとの平均KDA）
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

    # 直近20試合のトレンド
    last20 = df.tail(20)
    summary["recent_20"] = _agg_group(last20)

    return summary


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

    Args:
        df_filtered: ダッシュボードのフィルター済みDataFrame（除外フラグ済み）
        filter_info: フィルター条件の説明辞書
        my_xuid:     プレイヤーのXUID

    Returns:
        JSON文字列
    """
    # 統計対象（除外フラグなし）
    stat_df = df_filtered[df_filtered["exclude_flag"] == ""].copy()

    # メタ情報
    now_jst = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_range = ""
    if not stat_df.empty and "played_at" in stat_df.columns:
        dates = stat_df["played_at"].dt.tz_convert("Asia/Tokyo")
        date_range = f"{dates.min().strftime('%Y-%m-%d')} 〜 {dates.max().strftime('%Y-%m-%d')}"

    meta = {
        "generated_at":   now_jst,
        "player_xuid":    my_xuid,
        "export_matches": len(stat_df),
        "date_range":     date_range,
        "filter":         filter_info,
    }

    # 生データ（主要カラムのみ）
    cols = [c for c in EXPORT_COLUMNS if c in stat_df.columns]
    matches_df = stat_df[cols].copy()

    # played_at を JST 文字列に変換
    if "played_at" in matches_df.columns:
        matches_df["played_at"] = (
            matches_df["played_at"]
            .dt.tz_convert("Asia/Tokyo")
            .dt.strftime("%Y-%m-%d %H:%M")
        )

    # playlist / result を表示名に変換
    if "playlist" in matches_df.columns:
        matches_df["playlist"] = matches_df["playlist"].map(
            lambda x: PLAYLIST_DISPLAY.get(str(x), str(x))
        )
    if "result" in matches_df.columns:
        matches_df["result"] = matches_df["result"].map(
            lambda x: RESULT_DISPLAY.get(str(x), str(x))
        )

    # NaN を None に
    matches_records = json.loads(
        matches_df.to_json(orient="records", force_ascii=False)
    )

    # 出力
    export = {
        "meta":             meta,
        "suggested_prompt": SUGGESTED_PROMPT,
        "glossary":         GLOSSARY,
        "summary":          _build_summary(stat_df),
        "matches":          matches_records,
    }

    return json.dumps(export, ensure_ascii=False, indent=2)
