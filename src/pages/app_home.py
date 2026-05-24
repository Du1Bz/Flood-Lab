"""
pages/app_home.py
-----------------
ホームページ。今の状態を一目で把握する。

役割: 毎回起動時に開く。サマリー・カレンダーHM・インサイト・直近eMMR。
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.components.calendar_heatmap import render_calendar_heatmaps
from src.logic.insights import run_insights
from src.utils.display import PLAYLIST_DISPLAY
from src.utils.session import load_data, sidebar_refresh

sidebar_refresh()
df, cfg = load_data()

if df is None or df.empty:
    st.info("試合データが見つかりませんでした。OpenSpartan Workshop を起動してデータを同期してください。")
    st.stop()

st.title("🌊 Flood-Lab")
st.caption(f"プロファイル: {cfg.my_xuid}  |  DB: {cfg.db_path}")

# ==================================================
# サマリーカード
# ==================================================

rank_df = df[
    df["playlist"].isin(["ranked_arena","ranked_slayer","ranked_doubles","ranked_ffa","ranked_snipers"]) &
    (df["exclude_flag"] == "")
]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("総試合数（ランク）",   len(rank_df))
col2.metric("勝率",                 f"{rank_df['result_flag'].mean():.1%}" if len(rank_df) else "—")
col3.metric("平均K/D",              f"{rank_df['kd_ratio'].mean():.2f}"    if len(rank_df) else "—")
col4.metric("平均インパクトスコア", f"{rank_df['impact_score'].mean():.2f}" if rank_df["impact_score"].notna().any() else "—")
col5.metric("全試合数（全体）",     len(df))

st.divider()

# ==================================================
# カレンダーヒートマップ（直近8週）
# ==================================================

render_calendar_heatmaps(df)

st.divider()

# ==================================================
# 直近eMMR v2 推移（直近50試合）
# ==================================================

st.subheader("📈 直近 eMMR v2 推移")

stat_df = df[df["exclude_flag"] == ""]
emmr_df = stat_df[
    ~stat_df["playlist"].isin(["custom","casual","btb","pve","minigame"])
].dropna(subset=["emmr_v2"]).sort_values("played_at").tail(50).copy()
emmr_df["x"] = range(len(emmr_df))

if not emmr_df.empty:
    fig = go.Figure()
    cmap = {
        "ranked_arena":   "#636EFA",
        "ranked_slayer":  "#EF553B",
        "ranked_doubles": "#00CC96",
        "ranked_ffa":     "#FECB52",
        "ranked_snipers": "#B6E880",
    }
    for pl, grp in emmr_df.groupby("playlist"):
        fig.add_trace(go.Scatter(
            x=grp["x"], y=grp["emmr_v2"],
            mode="lines+markers",
            name=PLAYLIST_DISPLAY.get(pl, pl),
            line=dict(color=cmap.get(pl,"#aaa"), width=2),
            marker=dict(size=5),
        ))
    fig.update_layout(
        xaxis_title="試合番号（直近50試合）",
        yaxis_title="eMMR v2",
        height=300,
        margin=dict(t=10, b=10),
        legend=dict(orientation="h", y=1.05),
    )
    st.plotly_chart(fig, width="stretch")
else:
    st.info("eMMR v2 のデータがありません。")

st.divider()

# ==================================================
# インサイト（全期間対象）
# ==================================================

st.subheader("💡 インサイト")

with st.spinner("分析中..."):
    # 直近30試合のみを対象（全期間だと連敗記録が大量に出る）
    recent_df = stat_df.tail(30)
    insights = run_insights(recent_df)

if not insights:
    st.success("現在、特記すべきインサイトはありません。")
else:
    level_icons  = {"info": "ℹ️", "warning": "⚠️", "alert": "🚨"}
    level_colors = {"info": st.info, "warning": st.warning, "alert": st.error}
    for ins in insights:
        icon = level_icons.get(ins["level"], "•")
        level_colors.get(ins["level"], st.info)(
            f"**{icon} {ins['title']}**\n\n{ins['body']}"
        )