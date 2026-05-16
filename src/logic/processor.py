"""
logic/processor.py
------------------
database.py の raw DataFrame を受け取り、
parser / metrics のパイプラインを順番に適用して
分析用 DataFrame を返す。

データフロー:
  database.load_matches()
    → processor.build_match_df()   ← このファイル
      → parser.build_party_map()
      → parser.assign_sessions()
      → parser.add_flags()
      → metrics.add_basic_metrics()
      → metrics.add_csr_metrics()
      → metrics.add_avg_csr20()
      → metrics.add_emmr_v1()
      → metrics.add_trueskill_metrics()
      → metrics.add_emmr_v2()
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.logic import parser, metrics


def build_match_df(raw_df: pd.DataFrame, db_path: Path, my_xuid: str) -> pd.DataFrame:
    """
    raw DataFrame に全パイプラインを適用して分析用 DataFrame を返す。

    Args:
        raw_df:   database.load_matches() の戻り値
        db_path:  OpenSpartan DB のパス（パーティ検出に必要）
        my_xuid:  自分の XUID（"xuid(数字)" 形式）

    Returns:
        分析用 DataFrame（カラムは COLUMN_NAMES.md の内部カラム名に準拠）
    """
    if raw_df.empty:
        return raw_df

    df = raw_df.copy()

    # ① パーティ検出
    party_map = parser.build_party_map(df, db_path, my_xuid)
    df["party_size"] = df["match_id"].map(party_map).fillna(1).astype(int)

    # ② セッション分割
    df = parser.assign_sessions(df)

    # ③ 派生フラグ（party_type, is_solo, is_party）
    df = parser.add_flags(df)

    # ④ 基本レート系・時間正規化指標
    df = metrics.add_basic_metrics(df)

    # ⑤ CSR 増減
    df = metrics.add_csr_metrics(df)

    # ⑥ AvgCSR20（移動平均）
    df = metrics.add_avg_csr20(df)

    # ⑦ eMMR v1
    df = metrics.add_emmr_v1(df)

    # ⑧ TrueSkill2 系指標
    df = metrics.add_trueskill_metrics(df)

    # ⑨ eMMR v2（カルマンフィルタ）
    df = metrics.add_emmr_v2(df)

    return df
