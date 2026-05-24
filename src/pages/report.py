"""
pages/report.py
---------------
定型レポートビュー。期間のスナップショット。

役割: 「この期間どうだったか」を固定レイアウトで確認する。
"""

from __future__ import annotations
from datetime import date, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY
from src.utils.helpers import format_duration, week_label, month_label
from src.utils.session import load_data, sidebar_refresh

st.set_page_config(page_title="レポート | Flood-Lab", layout="wide")
sidebar_refresh()
df, _ = load_data()

if df is None or df.empty:
    st.warning("データをロードできませんでした。")
    st.stop()

df_stat = df[df["exclude_flag"] == ""].copy()

# ==================================================
# サイドバー: 期間選択
# ==================================================

with st.sidebar:
    st.header("期間選択")
    period_mode = st.radio("単位", ["週", "月", "セッション", "カスタム"], index=0)

    if period_mode == "週":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        weeks = []
        for i in range(26):
            monday = today - timedelta(days=today.weekday() + i * 7)
            monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)
            sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
            weeks.append((week_label(monday), monday, sunday))
        sel_label = st.selectbox("週を選択", [w[0] for w in weeks], index=0)
        sel_week  = next(w for w in weeks if w[0] == sel_label)
        period_from, period_to = sel_week[1], sel_week[2]
        period_label = sel_label
        prev_from = period_from - timedelta(weeks=1)
        prev_to   = period_from - timedelta(seconds=1)

    elif period_mode == "月":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        months = []
        for i in range(12):
            m = today.month - i; y = today.year
            while m <= 0: m += 12; y -= 1
            first = pd.Timestamp(year=y, month=m, day=1, tz="Asia/Tokyo")
            last  = pd.Timestamp(year=y+1 if m==12 else y, month=1 if m==12 else m+1, day=1, tz="Asia/Tokyo") - pd.Timedelta(seconds=1)
            months.append((month_label(first), first, last))
        sel_label = st.selectbox("月を選択", [m[0] for m in months], index=0)
        sel_month = next(m for m in months if m[0] == sel_label)
        period_from, period_to = sel_month[1], sel_month[2]
        period_label = sel_label
        prev_from = period_from - pd.DateOffset(months=1)
        prev_to   = period_from - pd.Timedelta(seconds=1)

    elif period_mode == "セッション":
        JST = "Asia/Tokyo"
        if "session_id" in df_stat.columns:
            sess_info = (
                df_stat.groupby("session_id")
                .agg(start=("played_at","min"), end=("played_at","max"), games=("result_flag","count"))
                .reset_index().sort_values("start", ascending=False)
            )
            def fmt_session(t):
                t_jst = t.tz_convert(JST)
                return f"{t_jst.year}.{t_jst.month}.{t_jst.day} {t_jst.hour:02d}:{t_jst.minute:02d} ~"
            sess_info["label"] = sess_info["start"].apply(fmt_session)
            sel_label = st.selectbox("セッションを選択", sess_info["label"].tolist(), index=0)
            sel_row   = sess_info[sess_info["label"] == sel_label].iloc[0]
            period_from  = sel_row["start"] - pd.Timedelta(seconds=1)
            period_to    = sel_row["end"]   + pd.Timedelta(hours=2)
            period_label = sel_label.replace(" ~","")
            cur_sid   = sel_row["session_id"]
            prev_rows = sess_info[sess_info["session_id"] == cur_sid - 1]
            if not prev_rows.empty:
                pr = prev_rows.iloc[0]
                prev_from = pr["start"] - pd.Timedelta(seconds=1)
                prev_to   = pr["end"]   + pd.Timedelta(hours=2)
            else:
                prev_from = prev_to = period_from
        else:
            st.warning("セッションデータがありません。")
            period_from = period_to = pd.Timestamp.now(tz="Asia/Tokyo")
            prev_from = prev_to = period_from
            period_label = "セッション"

    else:
        col_a, col_b = st.columns(2)
        date_from = col_a.date_input("開始日", value=date.today() - timedelta(days=7))
        date_to   = col_b.date_input("終了日", value=date.today())
        period_from = pd.Timestamp(date_from, tz="Asia/Tokyo")
        period_to   = pd.Timestamp(date_to, tz="Asia/Tokyo").replace(hour=23, minute=59, second=59)
        period_label = f"{date_from} 〜 {date_to}"
        delta = period_to - period_from
        prev_from = period_from - delta
        prev_to   = period_from - pd.Timedelta(seconds=1)

cur_df  = df_stat[(df_stat["played_at"] >= period_from) & (df_stat["played_at"] <= period_to)]
prev_df = df_stat[(df_stat["played_at"] >= prev_from)   & (df_stat["played_at"] <= prev_to)]

# ==================================================
# メイン
# ==================================================

st.title(f"📅 レポート — {period_label}")
st.caption(f"{period_from.strftime('%Y/%m/%d')} 〜 {period_to.strftime('%Y/%m/%d')}")

if cur_df.empty:
    st.info("この期間に試合データがありません。")
    st.stop()

# サマリーカード
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("試合数",     len(cur_df))
col2.metric("勝率",       f"{cur_df['result_flag'].mean():.1%}")
col3.metric("平均K/D",    f"{cur_df['kd_ratio'].mean():.2f}")
acc = cur_df["accuracy"].dropna()
col4.metric("平均命中率", f"{acc.mean():.1%}" if len(acc) else "—")
col5.metric("CSR増減合計", f"{cur_df['csr_delta'].sum():+.0f}" if cur_df["csr_delta"].notna().any() else "—")

st.divider()

# eMMR v2 推移
st.subheader("📈 eMMR v2 推移")
emmr_df = cur_df[
    ~cur_df["playlist"].isin(["custom","casual","btb","pve","minigame"])
].dropna(subset=["emmr_v2"]).sort_values("played_at").copy()
emmr_df["x"] = range(len(emmr_df))
if not emmr_df.empty:
    fig = go.Figure()
    cmap = {"ranked_arena":"#636EFA","ranked_slayer":"#EF553B","ranked_doubles":"#00CC96","ranked_ffa":"#FECB52","ranked_snipers":"#B6E880"}
    for pl, grp in emmr_df.groupby("playlist"):
        fig.add_trace(go.Scatter(x=grp["x"], y=grp["emmr_v2"], mode="lines+markers",
            name=PLAYLIST_DISPLAY.get(pl, pl), line=dict(color=cmap.get(pl,"#aaa"), width=2), marker=dict(size=5)))
    fig.update_layout(xaxis_title="試合番号", yaxis_title="eMMR v2", height=400,
                      margin=dict(t=10,b=10), legend=dict(orientation="h", y=1.05))
    st.plotly_chart(fig, width="stretch")
else:
    st.info("eMMR v2 のデータがありません。")

st.divider()

# マップ×ルール 勝率ヒートマップ
st.subheader("🗺️ マップ × ルール 勝率")
hm_df = cur_df.groupby(["map_name","rule_name"]).agg(
    勝率=("result_flag","mean"), 試合数=("result_flag","count")).reset_index()
if not hm_df.empty:
    pivot   = hm_df.pivot(index="map_name", columns="rule_name", values="勝率")
    pivot_n = hm_df.pivot(index="map_name", columns="rule_name", values="試合数").fillna(0).astype(int)
    z_vals  = pivot.values.copy().astype(float)
    text_vals = []
    for r in pivot.index:
        row_text = []
        for c in pivot.columns:
            v = pivot.loc[r,c]
            n = pivot_n.loc[r,c] if c in pivot_n.columns and r in pivot_n.index else 0
            row_text.append("—" if pd.isna(v) else f"{v:.0%} ({n}試合)")
        text_vals.append(row_text)
    z_display = np.where(np.isnan(z_vals), -1, z_vals)
    colorscale = [
        [0.000,"#2a2a2a"],[0.499,"#2a2a2a"],
        [0.500,"#7f1d1d"],[0.675,"#dc2626"],[0.740,"#f97316"],
        [0.750,"#eab308"],[0.760,"#84cc16"],[0.825,"#16a34a"],[1.000,"#14532d"],
    ]
    fig = go.Figure(data=go.Heatmap(
        z=z_display, x=pivot.columns.tolist(), y=pivot.index.tolist(),
        colorscale=colorscale, zmin=-1, zmax=1,
        text=text_vals, texttemplate="%{text}", textfont=dict(size=11),
        hovertemplate="マップ: %{y}<br>ルール: %{x}<br>%{text}<extra></extra>",
        showscale=True,
        colorbar=dict(tickvals=[0,0.25,0.5,0.75,1.0],
                      ticktext=["0%","25%","50%","75%","100%"], thickness=12, len=0.8),
    ))
    fig.update_layout(xaxis_title="ルール", yaxis_title="マップ",
                      height=max(300, len(pivot)*32+100), margin=dict(t=20,b=20,l=120,r=80))
    st.plotly_chart(fig, width="stretch")

st.divider()

# 最高/最低KDA試合
st.subheader("🎯 注目試合")
col_best, col_worst = st.columns(2)

def _match_card(row: pd.Series, label: str):
    st.markdown(f"**{label}**")
    st.write(f"📅 {pd.Timestamp(row['played_at']).tz_convert('Asia/Tokyo').strftime('%m/%d %H:%M')}")
    st.write(f"🗺️ {row.get('map_name','—')} / {row.get('rule_name','—')}")
    st.write(f"🏆 {RESULT_DISPLAY.get(row.get('result',''),'—')}")
    st.write(f"KDA: **{row.get('kda','—'):.2f}**")
    st.write(f"K/D: {row.get('kd_ratio','—'):.2f}")
    dd = row.get("damage_diff")
    st.write(f"ダメージ差: {int(dd):+,}" if pd.notna(dd) else "ダメージ差: —")

with col_best:
    if cur_df["kda"].notna().any():
        _match_card(cur_df.loc[cur_df["kda"].idxmax()], "✨ 最高KDA試合")
with col_worst:
    if cur_df["kda"].notna().any():
        _match_card(cur_df.loc[cur_df["kda"].idxmin()], "💀 最低KDA試合")

st.divider()

# 区分別勝率
st.subheader("🏆 区分別勝率")
sec_agg = (
    cur_df.groupby("playlist")
    .agg(試合数=("result_flag","count"), 勝率=("result_flag","mean"),
         KD=("kd_ratio","mean"), CSR増減=("csr_delta","sum")).reset_index()
)
sec_agg["区分"] = sec_agg["playlist"].map(PLAYLIST_DISPLAY)
sec_agg["勝率"] = sec_agg["勝率"].apply(lambda x: f"{x:.1%}")
sec_agg["KD"]   = sec_agg["KD"].apply(lambda x: f"{x:.2f}")
sec_agg["CSR"]  = sec_agg["CSR増減"].apply(lambda x: f"{x:+.0f}" if pd.notna(x) else "—")
st.dataframe(sec_agg[["区分","試合数","勝率","KD","CSR"]].rename(columns={"CSR":"CSR増減合計"}),
             hide_index=True, width="stretch")

st.divider()

# 前期間比較
st.subheader("📈 前期間との比較")

def _delta_metric(label, cur_val, prev_val, fmt=".2f"):
    if cur_val is None or pd.isna(cur_val):
        st.metric(label, "—"); return
    if prev_val is None or pd.isna(prev_val):
        st.metric(label, f"{cur_val:{fmt}}"); return
    st.metric(label, f"{cur_val:{fmt}}", delta=f"{cur_val-prev_val:+{fmt}}")

c1, c2, c3, c4 = st.columns(4)
with c1: _delta_metric("勝率(%)", cur_df["result_flag"].mean()*100 if len(cur_df) else None,
                        prev_df["result_flag"].mean()*100 if len(prev_df) else None, ".1f")
with c2: _delta_metric("平均KDA", cur_df["kda"].mean() if len(cur_df) else None,
                        prev_df["kda"].mean() if len(prev_df) else None)
with c3: _delta_metric("命中率(%)",
                        cur_df["accuracy"].dropna().mean()*100 if cur_df["accuracy"].notna().any() else None,
                        prev_df["accuracy"].dropna().mean()*100 if len(prev_df) and prev_df["accuracy"].notna().any() else None, ".1f")
with c4: _delta_metric("平均KPM",
                        cur_df["kpm"].dropna().mean() if cur_df["kpm"].notna().any() else None,
                        prev_df["kpm"].dropna().mean() if len(prev_df) and prev_df["kpm"].notna().any() else None, ".3f")
if prev_df.empty:
    st.caption("前期間のデータがないため比較できません。")