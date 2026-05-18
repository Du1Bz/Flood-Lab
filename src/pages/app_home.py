"""
pages/app_home.py
-----------------
ホームページ（トップ）。データロードとサマリー表示。
"""

import streamlit as st
from src.utils.session import load_data, sidebar_refresh

sidebar_refresh()

df, cfg = load_data()

if df is None or df.empty:
    st.info("試合データが見つかりませんでした。OpenSpartan Workshop を起動してデータを同期してください。")
    st.stop()

st.title("🌊 Flood-Lab")
# st.caption(f"プロファイル: {cfg.my_xuid}  |  DB: {cfg.db_path}")

rank_df = df[
    df["playlist"].isin(["ranked_arena", "ranked_slayer"]) &
    (df["exclude_flag"] == "")
]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("総試合数（ランク）",   len(rank_df))
col2.metric("勝率",                 f"{rank_df['result_flag'].mean():.1%}" if len(rank_df) else "—")
col3.metric("平均K/D",              f"{rank_df['kd_ratio'].mean():.2f}"    if len(rank_df) else "—")
col4.metric("平均インパクトスコア", f"{rank_df['impact_score'].mean():.2f}" if rank_df["impact_score"].notna().any() else "—")
col5.metric("全試合数（全体）",     len(df))

st.divider()
from src.components.calendar_heatmap import render_calendar_heatmaps
render_calendar_heatmaps(df)