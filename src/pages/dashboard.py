"""
pages/dashboard.py
------------------
自由分析ビュー（ダッシュボード）。

サイドバーのフィルター（区分 × マップ × ルール × 期間）で
DataFrame を絞り込み、各グラフ・テーブルを表示する。
"""

from __future__ import annotations

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta

from src.utils.display import (
    PLAYLIST_DISPLAY,
    RESULT_DISPLAY,
    display_name,
)

st.set_page_config(page_title="ダッシュボード | Flood-Lab", layout="wide")

# ==================================================
# データの取得（app.py からセッションステート経由）
# ==================================================

df: pd.DataFrame | None = st.session_state.get("df")

if df is None or df.empty:
    st.warning("トップページ（app.py）を先に開いてデータをロードしてください。")
    st.stop()

# 除外フラグを含む全データを持つ
df_all = df.copy()
# 統計・グラフ用: 除外フラグのないものだけ
df_stat = df_all[df_all["exclude_flag"] == ""].copy()

# ==================================================
# サイドバー: フィルター
# ==================================================

with st.sidebar:
    st.header("フィルター")

    # --- 期間 ---
    period_mode = st.radio(
        "期間",
        ["直近N戦", "今週", "今月", "カスタム"],
        index=0,
    )

    if period_mode == "直近N戦":
        n_recent = st.slider("直近N戦", 10, 500, 100, step=10)
        df_filtered = df_stat.tail(n_recent)
    elif period_mode == "今週":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        week_start = today - timedelta(days=today.weekday())
        df_filtered = df_stat[df_stat["played_at"] >= week_start]
    elif period_mode == "今月":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        df_filtered = df_stat[df_stat["played_at"] >= month_start]
    else:  # カスタム
        col_a, col_b = st.columns(2)
        date_from = col_a.date_input("開始日", value=date.today() - timedelta(days=30))
        date_to   = col_b.date_input("終了日", value=date.today())
        df_filtered = df_stat[
            (df_stat["played_at"].dt.date >= date_from) &
            (df_stat["played_at"].dt.date <= date_to)
        ]

    # --- 区分（プレイリスト）---
    playlist_options = ["すべて"] + [
        PLAYLIST_DISPLAY.get(p, p)
        for p in df_filtered["playlist"].dropna().unique()
    ]
    playlist_sel = st.selectbox("区分", playlist_options)

    if playlist_sel != "すべて":
        inv_playlist = {v: k for k, v in PLAYLIST_DISPLAY.items()}
        playlist_key = inv_playlist.get(playlist_sel, playlist_sel)
        df_filtered = df_filtered[df_filtered["playlist"] == playlist_key]

    # --- マップ ---
    map_options = ["すべて"] + sorted(df_filtered["map_name"].dropna().unique().tolist())
    map_sel = st.selectbox("マップ", map_options)
    if map_sel != "すべて":
        df_filtered = df_filtered[df_filtered["map_name"] == map_sel]

    # --- ルール ---
    rule_options = ["すべて"] + sorted(df_filtered["rule_name"].dropna().unique().tolist())
    rule_sel = st.selectbox("ルール", rule_options)
    if rule_sel != "すべて":
        df_filtered = df_filtered[df_filtered["rule_name"] == rule_sel]

    st.divider()
    st.caption(f"表示試合数: **{len(df_filtered)}**")

# ==================================================
# メインコンテンツ
# ==================================================

st.title("📊 ダッシュボード")

if df_filtered.empty:
    st.info("該当する試合がありません。フィルター条件を変更してください。")
    st.stop()

# --- サマリーカード ---
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("試合数",   len(df_filtered))
col2.metric("勝率",     f"{df_filtered['result_flag'].mean():.1%}")
col3.metric("平均K/D",  f"{df_filtered['kd_ratio'].mean():.2f}")

acc_vals = df_filtered["accuracy"].dropna()
col4.metric("平均命中率", f"{acc_vals.mean():.1%}" if len(acc_vals) else "—")

is_vals = df_filtered["impact_score"].dropna()
col5.metric("平均インパクト", f"{is_vals.mean():.3f}" if len(is_vals) else "—")

st.divider()

# ==================================================
# KDA / Accuracy の時系列折れ線
# ==================================================

st.subheader("📈 KDA・命中率の推移")

ma_window = st.slider("移動平均ウィンドウ（試合数）", 3, 30, 10, key="ma_window")

ts_df = df_filtered.sort_values("played_at").copy()
ts_df["kda_ma"]      = ts_df["kda"].rolling(ma_window, min_periods=1).mean()
ts_df["accuracy_ma"] = ts_df["accuracy"].rolling(ma_window, min_periods=1).mean()
ts_df["x_index"]     = range(len(ts_df))

tab_kda, tab_acc, tab_dmg = st.tabs(["KDA", "命中率", "ダメージ"])

with tab_kda:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["kda"],
        mode="markers", name="KDA", opacity=0.35,
        marker=dict(size=5, color="#636EFA"),
    ))
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["kda_ma"],
        mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#636EFA"),
    ))
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.update_layout(
        xaxis_title="試合番号", yaxis_title="KDA",
        height=350, margin=dict(t=20, b=20),
        legend=dict(orientation="h", y=1.05),
    )
    st.plotly_chart(fig, use_container_width=True)

with tab_acc:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["accuracy"],
        mode="markers", name="命中率", opacity=0.35,
        marker=dict(size=5, color="#EF553B"),
    ))
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["accuracy_ma"],
        mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#EF553B"),
    ))
    fig.update_layout(
        xaxis_title="試合番号",
        yaxis_title="命中率",
        yaxis_tickformat=".0%",
        height=350, margin=dict(t=20, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

with tab_dmg:
    ts_df["dmg_dealt_ma"] = ts_df["damage_dealt"].rolling(ma_window, min_periods=1).mean()
    ts_df["dmg_taken_ma"] = ts_df["damage_taken"].rolling(ma_window, min_periods=1).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["dmg_dealt_ma"],
        mode="lines", name="与ダメージ移動平均", line=dict(color="#00CC96"),
    ))
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["dmg_taken_ma"],
        mode="lines", name="被ダメージ移動平均", line=dict(color="#FF6692"),
    ))
    fig.update_layout(
        xaxis_title="試合番号", yaxis_title="ダメージ",
        height=350, margin=dict(t=20, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==================================================
# マップ別 KDA・勝率
# ==================================================

st.subheader("🗺️ マップ別パフォーマンス")

map_agg = (
    df_filtered.groupby("map_name")
    .agg(
        試合数=("result_flag", "count"),
        勝率=("result_flag", "mean"),
        KD=("kd_ratio", "mean"),
        ダメージ差=("damage_diff", "mean"),
    )
    .query("試合数 >= 3")
    .sort_values("勝率", ascending=False)
    .reset_index()
)
map_agg["勝率_pct"] = (map_agg["勝率"] * 100).round(1)
map_agg["KD"]       = map_agg["KD"].round(2)
map_agg["ダメージ差"] = map_agg["ダメージ差"].round(0)

tab_map_wr, tab_map_kd = st.tabs(["勝率", "K/D"])

with tab_map_wr:
    fig = px.bar(
        map_agg, x="map_name", y="勝率_pct",
        text="勝率_pct", color="勝率_pct",
        color_continuous_scale="RdYlGn",
        range_color=[30, 70],
        labels={"map_name": "マップ", "勝率_pct": "勝率(%)"},
        height=350,
    )
    fig.add_hline(y=50, line_dash="dash", line_color="gray")
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(margin=dict(t=20, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

with tab_map_kd:
    fig = px.bar(
        map_agg, x="map_name", y="KD",
        text="KD", color="KD",
        color_continuous_scale="RdYlGn",
        range_color=[0.5, 1.5],
        labels={"map_name": "マップ", "KD": "平均K/D"},
        height=350,
    )
    fig.add_hline(y=1, line_dash="dash", line_color="gray")
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(margin=dict(t=20, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==================================================
# 区分別比較
# ==================================================

st.subheader("🏆 区分別比較")

section_agg = (
    df_filtered.groupby("playlist")
    .agg(
        試合数=("result_flag", "count"),
        勝率=("result_flag", "mean"),
        KD=("kd_ratio", "mean"),
        ダメージ差=("damage_diff", "mean"),
    )
    .reset_index()
)
section_agg["区分"]  = section_agg["playlist"].map(PLAYLIST_DISPLAY)
section_agg["勝率"]  = (section_agg["勝率"] * 100).round(1)
section_agg["KD"]    = section_agg["KD"].round(2)
section_agg["ダメージ差"] = section_agg["ダメージ差"].round(0)

st.dataframe(
    section_agg[["区分", "試合数", "勝率", "KD", "ダメージ差"]],
    hide_index=True,
    use_container_width=True,
)

st.divider()

# ==================================================
# KDA vs Accuracy 散布図
# ==================================================

st.subheader("🎯 KDA vs 命中率")

scatter_df = df_filtered.dropna(subset=["kda", "accuracy"]).copy()
scatter_df["result_label"] = scatter_df["result"].map(RESULT_DISPLAY)

if not scatter_df.empty:
    fig = px.scatter(
        scatter_df,
        x="accuracy", y="kda",
        color="result_label",
        color_discrete_map={"勝ち": "#00CC96", "負け": "#EF553B", "引き分け": "#FFA15A", "途中抜け": "#AAAAAA"},
        hover_data={"map_name": True, "rule_name": True, "played_at": True},
        labels={"accuracy": "命中率", "kda": "KDA", "result_label": "勝敗"},
        opacity=0.7,
        height=400,
    )
    fig.update_traces(marker=dict(size=7))
    fig.update_xaxes(tickformat=".0%")
    fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("命中率データがありません。")

st.divider()

# ==================================================
# eMMR v2 推移グラフ
# ==================================================

st.subheader("📉 eMMR v2 推移")

emmr_df = df_filtered.dropna(subset=["emmr_v2"]).sort_values("played_at")
if not emmr_df.empty:
    fig = px.line(
        emmr_df, x="played_at", y="emmr_v2",
        color="playlist",
        color_discrete_map={
            "ranked_arena":  "#636EFA",
            "ranked_slayer": "#EF553B",
        },
        labels={"played_at": "日時", "emmr_v2": "eMMR v2", "playlist": "区分"},
        height=350,
    )
    # 凡例の表示名を日本語に
    for trace in fig.data:
        trace.name = PLAYLIST_DISPLAY.get(trace.name, trace.name)
    fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("eMMR v2 のデータがありません。")

st.divider()

# ==================================================
# CSR 推移グラフ
# ==================================================

st.subheader("🎖️ CSR 推移")

csr_df = df_filtered.dropna(subset=["csr_post"]).sort_values("played_at")
if not csr_df.empty:
    fig = px.line(
        csr_df, x="played_at", y="csr_post",
        color="playlist",
        color_discrete_map={
            "ranked_arena":  "#636EFA",
            "ranked_slayer": "#EF553B",
        },
        labels={"played_at": "日時", "csr_post": "CSR（試合後）", "playlist": "区分"},
        height=350,
    )
    for trace in fig.data:
        trace.name = PLAYLIST_DISPLAY.get(trace.name, trace.name)
    fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("CSR データがありません。")

st.divider()

# ==================================================
# マッチ一覧テーブル
# ==================================================

st.subheader("📋 マッチ一覧")

display_cols = [
    "played_at", "playlist", "map_name", "rule_name",
    "result", "kills", "deaths", "assists",
    "kd_ratio", "accuracy", "damage_diff",
    "csr_pre", "csr_post", "csr_delta",
    "party_type", "exclude_flag",
]
available = [c for c in display_cols if c in df_filtered.columns]

show_df = df_filtered[available].copy().sort_values("played_at", ascending=False)

# 表示名に変換したカラム名で出す
rename_map = {c: display_name(c) for c in available}
rename_map["playlist"] = "区分"
rename_map["result"]   = "勝敗"
show_df = show_df.rename(columns=rename_map)

# 区分・勝敗を日本語に変換
if "区分" in show_df.columns:
    show_df["区分"] = show_df["区分"].map(PLAYLIST_DISPLAY).fillna(show_df["区分"])
if "勝敗" in show_df.columns:
    show_df["勝敗"] = show_df["勝敗"].map(RESULT_DISPLAY).fillna(show_df["勝敗"])
if "命中率" in show_df.columns:
    show_df["命中率"] = show_df["命中率"].apply(
        lambda x: f"{x:.1%}" if pd.notna(x) else "—"
    )

st.dataframe(show_df, use_container_width=True, height=400)
