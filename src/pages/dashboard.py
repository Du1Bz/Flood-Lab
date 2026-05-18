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

from src.utils.session import load_data, sidebar_refresh
sidebar_refresh()
df, _ = load_data()

if df is None or df.empty:
    st.warning("データをロードできませんでした。")
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

tab_kda, tab_acc, tab_dmg, tab_perf = st.tabs(["KDA", "命中率", "ダメージ/分", "パーフェクト率"])

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
    st.plotly_chart(fig, width="stretch")

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
    st.plotly_chart(fig, width="stretch")

with tab_dmg:
    ts_df["dmg_dealt_pm_ma"] = ts_df["damage_dealt_per_min"].rolling(ma_window, min_periods=1).mean()
    ts_df["dmg_taken_pm_ma"] = ts_df["damage_taken_per_min"].rolling(ma_window, min_periods=1).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["dmg_dealt_pm_ma"],
        mode="lines", name="与ダメージ/分", line=dict(color="#00CC96"),
    ))
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["dmg_taken_pm_ma"],
        mode="lines", name="被ダメージ/分", line=dict(color="#FF6692"),
    ))
    fig.update_layout(
        xaxis_title="試合番号", yaxis_title="ダメージ/分",
        height=350, margin=dict(t=20, b=20),
    )
    st.plotly_chart(fig, width="stretch")

with tab_perf:
    ts_df["perf_rate_ma"] = ts_df["perfect_rate"].rolling(ma_window, min_periods=1).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["perfect_rate"],
        mode="markers", name="パーフェクト率", opacity=0.3,
        marker=dict(size=5, color="#AB63FA"),
    ))
    fig.add_trace(go.Scatter(
        x=ts_df["x_index"], y=ts_df["perf_rate_ma"],
        mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#AB63FA"),
    ))
    fig.update_layout(
        xaxis_title="試合番号", yaxis_title="パーフェクト率",
        yaxis_tickformat=".0%",
        height=350, margin=dict(t=20, b=20),
    )
    st.plotly_chart(fig, width="stretch")

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
    st.plotly_chart(fig, width="stretch")

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
    st.plotly_chart(fig, width="stretch")

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
    width="stretch",
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
    st.plotly_chart(fig, width="stretch")
else:
    st.info("命中率データがありません。")

st.divider()

# ==================================================
# ② K-RPI vs D-RPI 散布図（4象限分析）
# ==================================================

st.subheader("🎯 K-RPI vs D-RPI（4象限分析）")

rpi_df = df_filtered.dropna(subset=["k_rpi", "d_rpi"]).copy()
rpi_df["result_label"] = rpi_df["result"].map(RESULT_DISPLAY)

if not rpi_df.empty:
    fig = px.scatter(
        rpi_df,
        x="k_rpi", y="d_rpi",
        color="result_label",
        color_discrete_map={"勝ち": "#00CC96", "負け": "#EF553B", "引き分け": "#FFA15A", "途中抜け": "#AAAAAA"},
        hover_data={"map_name": True, "rule_name": True, "kda": True},
        labels={"k_rpi": "K-RPI（キル達成率）", "d_rpi": "D-RPI（生存率）", "result_label": "勝敗"},
        opacity=0.65,
        height=450,
    )
    fig.update_traces(marker=dict(size=7))
    # 4象限の基準線
    fig.add_vline(x=1.0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
    fig.add_hline(y=1.0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
    # 象限ラベル
    x_max = max(rpi_df["k_rpi"].quantile(0.98), 1.5)
    y_max = max(rpi_df["d_rpi"].quantile(0.98), 1.5)
    fig.add_annotation(x=x_max*0.95, y=y_max*0.95, text="キル◎ 生存◎", showarrow=False,
                       font=dict(color="rgba(0,204,150,0.6)", size=11))
    fig.add_annotation(x=0.3,        y=y_max*0.95, text="キル✕ 生存◎", showarrow=False,
                       font=dict(color="rgba(255,165,0,0.6)", size=11))
    fig.add_annotation(x=x_max*0.95, y=0.3,        text="キル◎ 生存✕", showarrow=False,
                       font=dict(color="rgba(255,165,0,0.6)", size=11))
    fig.add_annotation(x=0.3,        y=0.3,        text="キル✕ 生存✕", showarrow=False,
                       font=dict(color="rgba(239,85,59,0.6)", size=11))
    fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(fig, width="stretch")
else:
    st.info("TrueSkill2データがありません。")

st.divider()

# ==================================================
# ③ セッション内疲労（折れ線 + 信頼区間）
# ==================================================

st.subheader("😴 セッション内パフォーマンス推移")

if "session_seq" in df_filtered.columns and "kda" in df_filtered.columns:
    import numpy as np
    from scipy import stats as scipy_stats

    fatigue_df = df_filtered.dropna(subset=["kda", "session_seq"]).copy()
    fatigue_df["session_seq"] = fatigue_df["session_seq"].astype(int)
    max_seq = int(fatigue_df["session_seq"].quantile(0.9))  # 外れ値除外

    fatigue_df = fatigue_df[fatigue_df["session_seq"] <= max_seq]

    seq_stats = (
        fatigue_df.groupby("session_seq")["kda"]
        .agg(["mean", "sem", "count"])
        .reset_index()
    )
    seq_stats.columns = ["seq", "mean", "sem", "count"]
    seq_stats = seq_stats[seq_stats["count"] >= 3]  # 3試合以上のセッション番号のみ

    if not seq_stats.empty:
        ci95 = seq_stats["sem"] * 1.96
        fig = go.Figure()
        # CI帯
        fig.add_trace(go.Scatter(
            x=pd.concat([seq_stats["seq"], seq_stats["seq"].iloc[::-1]]),
            y=pd.concat([seq_stats["mean"] + ci95, (seq_stats["mean"] - ci95).iloc[::-1]]),
            fill="toself", fillcolor="rgba(99,110,250,0.15)",
            line=dict(color="rgba(0,0,0,0)"), name="95% CI", showlegend=True,
        ))
        # 平均線
        fig.add_trace(go.Scatter(
            x=seq_stats["seq"], y=seq_stats["mean"],
            mode="lines+markers", name="平均KDA",
            line=dict(color="#636EFA", width=2),
            marker=dict(size=6),
        ))
        fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.2)")
        fig.update_layout(
            xaxis_title="セッション内試合番号",
            yaxis_title="KDA",
            xaxis=dict(dtick=1),
            height=350, margin=dict(t=20, b=20),
        )
        st.plotly_chart(fig, width="stretch")
        # 相関係数
        if len(seq_stats) >= 3:
            r, p = scipy_stats.pearsonr(seq_stats["seq"], seq_stats["mean"])
            trend = "📉 後半に低下傾向あり" if r < -0.3 and p < 0.1 else "→ 明確な低下傾向なし"
            st.caption(f"相関係数 r = {r:.3f}（p = {p:.3f}）　{trend}")
    else:
        st.info("セッションデータが不十分です。")
else:
    st.info("セッションデータがありません。")

st.divider()

# ==================================================
# ① ダメージ差の分布（マップ別 箱ひげ図）
# ==================================================

st.subheader("📦 マップ別 ダメージ差の分布")

box_df = df_filtered.dropna(subset=["damage_diff"]).copy()

if not box_df.empty:
    # 5試合以上のマップのみ
    map_counts = box_df["map_name"].value_counts()
    valid_maps = map_counts[map_counts >= 5].index.tolist()
    box_df = box_df[box_df["map_name"].isin(valid_maps)]

    # 中央値でソート
    map_order = (
        box_df.groupby("map_name")["damage_diff"]
        .median()
        .sort_values(ascending=True)
        .index.tolist()
    )

    fig = go.Figure()
    for map_name in map_order:
        mdf = box_df[box_df["map_name"] == map_name]
        fig.add_trace(go.Box(
            y=mdf["damage_diff"],
            name=map_name,
            boxmean=True,
            marker_color="#636EFA",
            line_color="#636EFA",
        ))

    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
    fig.update_layout(
        yaxis_title="ダメージ差",
        xaxis_title="マップ",
        showlegend=False,
        height=400,
        margin=dict(t=20, b=20),
    )
    st.plotly_chart(fig, width="stretch")
else:
    st.info("データがありません。")

st.divider()

# ==================================================
# eMMR v2 推移グラフ
# ==================================================

st.subheader("📉 eMMR v2 推移")

emmr_df = df_filtered[
    df_filtered["playlist"] != "custom"
].dropna(subset=["emmr_v2"]).sort_values("played_at")
if not emmr_df.empty:
    fig = px.line(
        emmr_df, x="played_at", y="emmr_v2",
        color="playlist",
        color_discrete_map={
            "ranked_arena":   "#636EFA",
            "ranked_slayer":  "#EF553B",
            "ranked_doubles": "#00CC96",
            "ranked_ffa":     "#FECB52",
            "ranked_snipers": "#B6E880",
        },
        labels={"played_at": "日時", "emmr_v2": "eMMR v2", "playlist": "区分"},
        height=350,
    )
    for trace in fig.data:
        trace.name = PLAYLIST_DISPLAY.get(trace.name, trace.name)
    fig.update_layout(margin=dict(t=20, b=20))
    st.plotly_chart(fig, width="stretch")
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
    st.plotly_chart(fig, width="stretch")
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

st.dataframe(show_df, width="stretch", height=400)