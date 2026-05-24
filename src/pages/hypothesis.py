"""
pages/hypothesis.py
-------------------
仮説検証ページ。「なぜ勝てないのか」「なぜこの指標が低いのか」を検証する。

役割: 特定の疑問を持ったときに開いて仮説を検証する。
"""

from __future__ import annotations
from datetime import date, timedelta

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.logic.insights import run_insights
from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY
from src.utils.session import load_data, sidebar_refresh

st.set_page_config(page_title="仮説検証 | Flood-Lab", layout="wide")
sidebar_refresh()
df, _ = load_data()

if df is None or df.empty:
    st.warning("データをロードできませんでした。")
    st.stop()

df_stat = df[df["exclude_flag"] == ""].copy()

# ==================================================
# サイドバー: フィルター
# ==================================================

with st.sidebar:
    st.header("フィルター")
    period_mode = st.radio("期間", ["全期間", "直近N戦", "カスタム"], index=0)
    if period_mode == "直近N戦":
        n = st.slider("直近N戦", 20, 500, 100, step=10)
        df_filtered = df_stat.tail(n)
    elif period_mode == "カスタム":
        col_a, col_b = st.columns(2)
        date_from = col_a.date_input("開始日", value=date.today() - timedelta(days=30))
        date_to   = col_b.date_input("終了日", value=date.today())
        df_filtered = df_stat[
            (df_stat["played_at"].dt.date >= date_from) &
            (df_stat["played_at"].dt.date <= date_to)
        ]
    else:
        df_filtered = df_stat.copy()

    playlist_options = ["すべて"] + [PLAYLIST_DISPLAY.get(p,p) for p in sorted(df_filtered["playlist"].dropna().unique())]
    playlist_sel = st.selectbox("区分", playlist_options)
    if playlist_sel != "すべて":
        inv = {v: k for k, v in PLAYLIST_DISPLAY.items()}
        df_filtered = df_filtered[df_filtered["playlist"] == inv.get(playlist_sel, playlist_sel)]

    st.divider()
    st.caption(f"対象試合数: **{len(df_filtered)}**")

st.title("🔬 仮説検証")

if df_filtered.empty:
    st.info("該当する試合がありません。")
    st.stop()

# ==================================================
# ① KDA vs 命中率 散布図
# ==================================================

st.subheader("① KDA vs 命中率")
scatter_df = df_filtered.dropna(subset=["kda","accuracy"]).copy()
scatter_df["result_label"] = scatter_df["result"].map(RESULT_DISPLAY)
if not scatter_df.empty:
    fig = px.scatter(scatter_df, x="accuracy", y="kda", color="result_label",
        color_discrete_map={"勝ち":"#00CC96","負け":"#EF553B","引き分け":"#FFA15A","途中抜け":"#AAAAAA"},
        hover_data={"map_name":True,"rule_name":True,"played_at":True},
        labels={"accuracy":"命中率","kda":"KDA","result_label":"勝敗"},
        opacity=0.7, height=400)
    fig.update_traces(marker=dict(size=7))
    fig.update_xaxes(tickformat=".0%")
    fig.update_layout(margin=dict(t=20,b=20))
    st.plotly_chart(fig, width="stretch")

st.divider()

# ==================================================
# ② 仮説: 「丁寧なショットは正義か？」
# ==================================================

st.subheader("② 仮説: 丁寧なショットは正義か？")
st.caption("命中率とD-RPI（生存能力）の相関を検証する。丁寧に当てるほど死なないか？")

hyp_df = df_filtered.copy()
hyp_df["result_str"]   = hyp_df["result_flag"].map({1: "Win", 0: "Loss"})
hyp_df["accuracy_pct"] = hyp_df["accuracy"] * 100

c1, c2 = st.columns(2)

with c1:
    st.markdown("**命中率 vs D-RPI（傾向線付き）**")
    fig = px.scatter(hyp_df.dropna(subset=["accuracy_pct","d_rpi"]),
        x="accuracy_pct", y="d_rpi", color="result_str",
        color_discrete_map={"Win":"#1D9E75","Loss":"#D85A30"},
        labels={"accuracy_pct":"命中率 (%)","d_rpi":"D-RPI（生存能力）"},
        hover_data=["map_name","kills","deaths"],
        trendline="ols", height=380)
    fig.add_hline(y=1.0, line_dash="dash", line_color="#888888", annotation_text="期待デス基準")
    fig.update_layout(margin=dict(t=20,b=20))
    st.plotly_chart(fig, width="stretch")
    st.info("傾向線が右肩上がり → 命中率が上がるほど死なない、が立証されます。")

with c2:
    st.markdown("**勝敗別 命中率の分布**")
    fig = px.box(hyp_df.dropna(subset=["accuracy_pct"]),
        x="result_str", y="accuracy_pct", color="result_str",
        color_discrete_map={"Win":"#1D9E75","Loss":"#D85A30"},
        labels={"result_str":"試合結果","accuracy_pct":"命中率 (%)"},
        points="all", height=380)
    fig.update_layout(showlegend=False, margin=dict(t=20,b=20))
    st.plotly_chart(fig, width="stretch")

    win_med  = hyp_df[hyp_df["result_flag"]==1]["accuracy_pct"].median()
    loss_med = hyp_df[hyp_df["result_flag"]==0]["accuracy_pct"].median()
    if pd.notna(win_med) and pd.notna(loss_med):
        diff = win_med - loss_med
        if diff > 0:
            st.success(f"🔥 勝利時の命中率中央値（{win_med:.1f}%）は敗北時より {diff:.1f}% 高い。")
        else:
            st.warning(f"🤔 勝利時（{win_med:.1f}%）と敗北時（{loss_med:.1f}%）で命中率に差がない。別の原因を探ろう。")

st.divider()

# ==================================================
# ③ インサイト（統計ベース）
# ==================================================

st.subheader("③ 統計インサイト")
st.caption("移動平均・信頼区間ベースで検出した傾向。フィルターに連動します。")

with st.spinner("分析中..."):
    insights = run_insights(df_filtered)

if not insights:
    st.success("この期間に特記すべきインサイトはありません。")
else:
    level_icons  = {"info":"ℹ️","warning":"⚠️","alert":"🚨"}
    level_colors = {"info":st.info,"warning":st.warning,"alert":st.error}
    for ins in insights:
        icon = level_icons.get(ins["level"],"•")
        level_colors.get(ins["level"], st.info)(f"**{icon} {ins['title']}**\n\n{ins['body']}")
