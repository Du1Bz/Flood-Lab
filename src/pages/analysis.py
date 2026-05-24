"""
pages/analysis.py
-----------------
分析ページ。フィルターで絞り込んでグラフを自由に探索する。

タブ構成:
  ① トレンド     - 時系列・eMMR/CSR推移
  ② マップ・ルール - マップ別棒グラフ・区分別テーブル・マップ×ルールHM
  ③ TrueSkill2  - K-RPI/D-RPI散布図・セッション疲労・ダメージ差箱ひげ図
  ④ オブジェクト  - ルール連動オブジェクトスタッツ
"""

from __future__ import annotations
from datetime import date, timedelta
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy import stats as scipy_stats

from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY, display_name
from src.utils.session import load_data, sidebar_refresh

st.set_page_config(page_title="分析 | Flood-Lab", layout="wide")
sidebar_refresh()
df, _ = load_data()

if df is None or df.empty:
    st.warning("データをロードできませんでした。")
    st.stop()

df_stat = df[df["exclude_flag"] == ""].copy()

# ==================================================
# サイドバー: フィルター + AIエクスポート
# ==================================================

with st.sidebar:
    st.header("フィルター")

    period_mode = st.radio("期間", ["直近N戦", "過去7日", "過去30日", "カスタム"], index=0)
    if period_mode == "直近N戦":
        n_recent = st.slider("直近N戦", 10, 500, 100, step=10)
        df_filtered = df_stat.tail(n_recent)
    elif period_mode == "過去7日":
        since = pd.Timestamp.now(tz="Asia/Tokyo") - pd.Timedelta(days=7)
        df_filtered = df_stat[df_stat["played_at"] >= since]
    elif period_mode == "過去30日":
        since = pd.Timestamp.now(tz="Asia/Tokyo") - pd.Timedelta(days=30)
        df_filtered = df_stat[df_stat["played_at"] >= since]
    else:
        col_a, col_b = st.columns(2)
        date_from = col_a.date_input("開始日", value=date.today() - timedelta(days=30))
        date_to   = col_b.date_input("終了日", value=date.today())
        df_filtered = df_stat[
            (df_stat["played_at"].dt.date >= date_from) &
            (df_stat["played_at"].dt.date <= date_to)
        ]

    playlist_options = ["すべて"] + [PLAYLIST_DISPLAY.get(p, p) for p in sorted(df_filtered["playlist"].dropna().unique())]
    playlist_sel = st.selectbox("区分", playlist_options)
    if playlist_sel != "すべて":
        inv = {v: k for k, v in PLAYLIST_DISPLAY.items()}
        df_filtered = df_filtered[df_filtered["playlist"] == inv.get(playlist_sel, playlist_sel)]

    map_options = ["すべて"] + sorted(df_filtered["map_name"].dropna().unique().tolist())
    map_sel = st.selectbox("マップ", map_options)
    if map_sel != "すべて":
        df_filtered = df_filtered[df_filtered["map_name"] == map_sel]

    rule_options = ["すべて"] + sorted(df_filtered["rule_name"].dropna().unique().tolist())
    rule_sel = st.selectbox("ルール", rule_options)
    if rule_sel != "すべて":
        df_filtered = df_filtered[df_filtered["rule_name"] == rule_sel]

    st.divider()
    st.caption(f"表示試合数: **{len(df_filtered)}**")

    st.divider()
    st.markdown("**🤖 AI相談用エクスポート**")
    if st.button("📥 JSONを生成", use_container_width=True):
        from src.logic.exporter import build_export
        from datetime import datetime as dt_
        filter_info = {
            "period":   period_mode if period_mode != "直近N戦" else f"直近{n_recent}試合",
            "playlist": playlist_sel, "map": map_sel, "rule": rule_sel,
        }
        cfg = st.session_state.get("config")
        json_str = build_export(df_filtered, filter_info, cfg.my_xuid if cfg else "unknown")
        filename = f"flood_lab_export_{dt_.now().strftime('%Y%m%d_%H%M')}.json"
        st.download_button("💾 ダウンロード", data=json_str.encode("utf-8"),
                           file_name=filename, mime="application/json", use_container_width=True)
        st.caption(f"{len(df_filtered)}試合分のデータを生成しました。")

# ==================================================
# メイン
# ==================================================

st.title("📊 分析")

if df_filtered.empty:
    st.info("該当する試合がありません。フィルター条件を変更してください。")
    st.stop()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("試合数",   len(df_filtered))
col2.metric("勝率",     f"{df_filtered['result_flag'].mean():.1%}")
col3.metric("平均K/D",  f"{df_filtered['kd_ratio'].mean():.2f}")
acc_v = df_filtered["accuracy"].dropna()
col4.metric("平均命中率", f"{acc_v.mean():.1%}" if len(acc_v) else "—")
is_v = df_filtered["impact_score"].dropna()
col5.metric("平均インパクト", f"{is_v.mean():.3f}" if len(is_v) else "—")

tab1, tab2, tab3, tab4 = st.tabs(["📈 トレンド", "🗺️ マップ・ルール", "🎯 TrueSkill2", "🏆 オブジェクト"])

# ============================================================
# タブ① トレンド
# ============================================================

with tab1:
    ma_window = st.slider("移動平均ウィンドウ（試合数）", 3, 30, 10, key="ma_window")
    ts_df = df_filtered.sort_values("played_at").copy()
    ts_df["x_index"] = range(len(ts_df))

    sub1, sub2, sub3, sub4 = st.tabs(["KDA", "命中率", "ダメージ/分", "パーフェクト率"])

    with sub1:
        ts_df["kda_ma"] = ts_df["kda"].rolling(ma_window, min_periods=1).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["kda"],
            mode="markers", name="KDA", opacity=0.35, marker=dict(size=5, color="#636EFA")))
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["kda_ma"],
            mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#636EFA")))
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        fig.update_layout(xaxis_title="試合番号", yaxis_title="KDA",
                          height=350, margin=dict(t=20, b=20), legend=dict(orientation="h", y=1.05))
        st.plotly_chart(fig, width="stretch")

    with sub2:
        ts_df["accuracy_ma"] = ts_df["accuracy"].rolling(ma_window, min_periods=1).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["accuracy"],
            mode="markers", name="命中率", opacity=0.35, marker=dict(size=5, color="#EF553B")))
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["accuracy_ma"],
            mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#EF553B")))
        fig.update_layout(xaxis_title="試合番号", yaxis_title="命中率",
                          yaxis_tickformat=".0%", height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, width="stretch")

    with sub3:
        ts_df["dmg_dealt_ma"] = ts_df["damage_dealt_per_min"].rolling(ma_window, min_periods=1).mean()
        ts_df["dmg_taken_ma"] = ts_df["damage_taken_per_min"].rolling(ma_window, min_periods=1).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["dmg_dealt_ma"],
            mode="lines", name="与ダメージ/分", line=dict(color="#00CC96")))
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["dmg_taken_ma"],
            mode="lines", name="被ダメージ/分", line=dict(color="#FF6692")))
        fig.update_layout(xaxis_title="試合番号", yaxis_title="ダメージ/分",
                          height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, width="stretch")

    with sub4:
        ts_df["perf_ma"] = ts_df["perfect_rate"].rolling(ma_window, min_periods=1).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["perfect_rate"],
            mode="markers", name="パーフェクト率", opacity=0.3, marker=dict(size=5, color="#AB63FA")))
        fig.add_trace(go.Scatter(x=ts_df["x_index"], y=ts_df["perf_ma"],
            mode="lines", name=f"移動平均({ma_window})", line=dict(width=2, color="#AB63FA")))
        fig.update_layout(xaxis_title="試合番号", yaxis_title="パーフェクト率",
                          yaxis_tickformat=".0%", height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, width="stretch")

    st.divider()

    # eMMR v2 推移
    st.subheader("📉 eMMR v2 推移")
    emmr_df = df_filtered[
        ~df_filtered["playlist"].isin(["custom","casual","btb","pve","minigame"])
    ].dropna(subset=["emmr_v2"]).sort_values("played_at").copy()
    emmr_df["x"] = range(len(emmr_df))
    if not emmr_df.empty:
        fig = go.Figure()
        for pl, grp in emmr_df.groupby("playlist"):
            color_map = {"ranked_arena":"#636EFA","ranked_slayer":"#EF553B",
                         "ranked_doubles":"#00CC96","ranked_ffa":"#FECB52","ranked_snipers":"#B6E880"}
            fig.add_trace(go.Scatter(x=grp["x"], y=grp["emmr_v2"], mode="lines+markers",
                name=PLAYLIST_DISPLAY.get(pl, pl), line=dict(color=color_map.get(pl,"#aaa"), width=2),
                marker=dict(size=5)))
        fig.update_layout(xaxis_title="試合番号", yaxis_title="eMMR v2", height=350,
                          margin=dict(t=20, b=20), legend=dict(orientation="h", y=1.05))
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("eMMR v2 のデータがありません。")

    # CSR 推移
    st.subheader("🎖️ CSR 推移")
    csr_df = df_filtered.dropna(subset=["csr_post"]).sort_values("played_at")
    if not csr_df.empty:
        fig = px.line(csr_df, x="played_at", y="csr_post", color="playlist",
            color_discrete_map={"ranked_arena":"#636EFA","ranked_slayer":"#EF553B",
                                 "ranked_doubles":"#00CC96","ranked_ffa":"#FECB52"},
            labels={"played_at":"日時","csr_post":"CSR（試合後）","playlist":"区分"}, height=350)
        for trace in fig.data:
            trace.name = PLAYLIST_DISPLAY.get(trace.name, trace.name)
        fig.update_layout(margin=dict(t=20, b=20))
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("CSR データがありません。")

# ============================================================
# タブ② マップ・ルール
# ============================================================

with tab2:
    # マップ別棒グラフ
    st.subheader("🗺️ マップ別パフォーマンス")
    map_agg = (
        df_filtered.groupby("map_name")
        .agg(試合数=("result_flag","count"), 勝率=("result_flag","mean"),
             KD=("kd_ratio","mean"), ダメージ差=("damage_diff","mean"))
        .query("試合数 >= 3").sort_values("勝率", ascending=False).reset_index()
    )
    map_agg["勝率_pct"] = (map_agg["勝率"] * 100).round(1)
    map_agg["KD"] = map_agg["KD"].round(2)

    sub_wr, sub_kd = st.tabs(["勝率", "K/D"])
    with sub_wr:
        fig = px.bar(map_agg, x="map_name", y="勝率_pct", text="勝率_pct",
            color="勝率_pct", color_continuous_scale="RdYlGn", range_color=[30,70],
            labels={"map_name":"マップ","勝率_pct":"勝率(%)"}, height=350)
        fig.add_hline(y=50, line_dash="dash", line_color="gray")
        fig.update_traces(texttemplate="%{text}%", textposition="outside")
        fig.update_layout(margin=dict(t=20,b=20), coloraxis_showscale=False)
        st.plotly_chart(fig, width="stretch")
    with sub_kd:
        fig = px.bar(map_agg, x="map_name", y="KD", text="KD",
            color="KD", color_continuous_scale="RdYlGn", range_color=[0.5,1.5],
            labels={"map_name":"マップ","KD":"平均K/D"}, height=350)
        fig.add_hline(y=1, line_dash="dash", line_color="gray")
        fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig.update_layout(margin=dict(t=20,b=20), coloraxis_showscale=False)
        st.plotly_chart(fig, width="stretch")

    st.divider()

    # 区分別比較
    st.subheader("🏆 区分別比較")
    sec_agg = (
        df_filtered.groupby("playlist")
        .agg(試合数=("result_flag","count"), 勝率=("result_flag","mean"),
             KD=("kd_ratio","mean"), ダメージ差=("damage_diff","mean")).reset_index()
    )
    sec_agg["区分"] = sec_agg["playlist"].map(PLAYLIST_DISPLAY)
    sec_agg["勝率"] = (sec_agg["勝率"] * 100).round(1)
    sec_agg["KD"]   = sec_agg["KD"].round(2)
    sec_agg["ダメージ差"] = sec_agg["ダメージ差"].round(0)
    st.dataframe(sec_agg[["区分","試合数","勝率","KD","ダメージ差"]], hide_index=True, width="stretch")

    st.divider()

    # マップ×ルール 勝率ヒートマップ
    st.subheader("🗺️ マップ × ルール 勝率")
    hm_df = df_filtered.groupby(["map_name","rule_name"]).agg(
        勝率=("result_flag","mean"), 試合数=("result_flag","count")).reset_index()
    if not hm_df.empty:
        import numpy as np_
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
        z_display = np_.where(np_.isnan(z_vals), -1, z_vals)
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

    # PWコントロール率
    st.subheader("🔫 PWコントロール率")
    st.caption("自チームPWキル / (自チーム + 敵チームPWキル)。0.5が均衡、高いほどPWを活かせた試合。")

    pw_df = df_filtered.dropna(subset=["pw_control_rate"]).sort_values("played_at").copy()
    pw_df["x"] = range(len(pw_df))
    pw_df["result_label"] = pw_df["result"].map(RESULT_DISPLAY)

    if pw_df.empty:
        st.info("PWコントロール率のデータがありません（両チームPWキル0の試合のみの場合や試合数が少ない場合）。")
    else:
        pw_df["pw_ma"] = pw_df["pw_control_rate"].rolling(10, min_periods=1).mean()

        # 時系列折れ線 + 勝敗カラーの散布
        fig = go.Figure()
        for result_val, color, label in [
            ("win",  "#00CC96", "勝ち"),
            ("loss", "#EF553B", "負け"),
            ("draw", "#FFA15A", "引き分け"),
        ]:
            grp = pw_df[pw_df["result"] == result_val]
            if not grp.empty:
                fig.add_trace(go.Scatter(
                    x=grp["x"], y=grp["pw_control_rate"],
                    mode="markers", name=label,
                    marker=dict(color=color, size=7, opacity=0.6),
                    hovertemplate="試合番号: %{x}<br>PW率: %{y:.1%}<br>" + label + "<extra></extra>",
                ))
        fig.add_trace(go.Scatter(
            x=pw_df["x"], y=pw_df["pw_ma"],
            mode="lines", name="移動平均(10)",
            line=dict(color="white", width=2),
        ))
        fig.add_hline(y=0.5, line_dash="dash", line_color="rgba(255,255,255,0.3)",
                      annotation_text="均衡(0.5)", annotation_position="right")
        fig.update_layout(
            xaxis_title="試合番号", yaxis_title="PWコントロール率",
            yaxis_tickformat=".0%", yaxis_range=[0, 1],
            height=350, margin=dict(t=20, b=20),
            legend=dict(orientation="h", y=1.05),
        )
        st.plotly_chart(fig, width="stretch")

        # マップ別PWコントロール率の棒グラフ
        st.markdown("**マップ別 平均PWコントロール率**（3試合以上）")
        pw_map = (
            pw_df.groupby("map_name")["pw_control_rate"]
            .agg(["mean", "count"]).reset_index()
            .query("count >= 3")
            .sort_values("mean", ascending=False)
        )
        if not pw_map.empty:
            pw_map["pct"] = (pw_map["mean"] * 100).round(1)
            fig2 = px.bar(
                pw_map, x="map_name", y="pct", text="pct",
                color="pct", color_continuous_scale="RdYlGn", range_color=[30, 70],
                labels={"map_name": "マップ", "pct": "PWコントロール率(%)"},
                height=320,
            )
            fig2.add_hline(y=50, line_dash="dash", line_color="gray")
            fig2.update_traces(texttemplate="%{text}%", textposition="outside")
            fig2.update_layout(margin=dict(t=20, b=20), coloraxis_showscale=False)
            st.plotly_chart(fig2, width="stretch")

        # PWコントロール率と勝敗の関係（箱ひげ図）
        st.markdown("**勝敗別 PWコントロール率の分布**")
        fig3 = px.box(
            pw_df, x="result_label", y="pw_control_rate", color="result_label",
            color_discrete_map={"勝ち": "#00CC96", "負け": "#EF553B", "引き分け": "#FFA15A"},
            labels={"result_label": "勝敗", "pw_control_rate": "PWコントロール率"},
            points="all", height=350,
        )
        fig3.add_hline(y=0.5, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        fig3.update_layout(showlegend=False, yaxis_tickformat=".0%", margin=dict(t=20, b=20))
        st.plotly_chart(fig3, width="stretch")

# ============================================================
# タブ③ TrueSkill2
# ============================================================

with tab3:
    # K-RPI vs D-RPI 4象限
    st.subheader("🎯 K-RPI vs D-RPI（4象限分析）")
    rpi_df = df_filtered.dropna(subset=["k_rpi","d_rpi"]).copy()
    rpi_df["result_label"] = rpi_df["result"].map(RESULT_DISPLAY)
    if not rpi_df.empty:
        fig = px.scatter(rpi_df, x="k_rpi", y="d_rpi", color="result_label",
            color_discrete_map={"勝ち":"#00CC96","負け":"#EF553B","引き分け":"#FFA15A","途中抜け":"#AAAAAA"},
            hover_data={"map_name":True,"rule_name":True,"kda":True},
            labels={"k_rpi":"K-RPI（キル達成率）","d_rpi":"D-RPI（生存率）","result_label":"勝敗"},
            opacity=0.65, height=450)
        fig.update_traces(marker=dict(size=7))
        fig.add_vline(x=1.0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        fig.add_hline(y=1.0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        x_max = max(rpi_df["k_rpi"].quantile(0.98), 1.5)
        y_max = max(rpi_df["d_rpi"].quantile(0.98), 1.5)
        for x, y, txt, clr in [
            (x_max*0.95, y_max*0.95, "キル◎ 生存◎", "rgba(0,204,150,0.6)"),
            (0.3,        y_max*0.95, "キル✕ 生存◎", "rgba(255,165,0,0.6)"),
            (x_max*0.95, 0.3,        "キル◎ 生存✕", "rgba(255,165,0,0.6)"),
            (0.3,        0.3,        "キル✕ 生存✕", "rgba(239,85,59,0.6)"),
        ]:
            fig.add_annotation(x=x, y=y, text=txt, showarrow=False, font=dict(color=clr, size=11))
        fig.update_layout(margin=dict(t=20, b=20))
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("TrueSkill2データがありません。")

    st.divider()

    # セッション疲労
    st.subheader("😴 セッション内パフォーマンス推移")
    if "session_seq" in df_filtered.columns:
        fat_df = df_filtered.dropna(subset=["kda","session_seq"]).copy()
        fat_df["session_seq"] = fat_df["session_seq"].astype(int)
        max_seq = int(fat_df["session_seq"].quantile(0.9))
        fat_df  = fat_df[fat_df["session_seq"] <= max_seq]
        seq_s   = fat_df.groupby("session_seq")["kda"].agg(["mean","sem","count"]).reset_index()
        seq_s.columns = ["seq","mean","sem","count"]
        seq_s   = seq_s[seq_s["count"] >= 3]
        if not seq_s.empty:
            ci95 = seq_s["sem"] * 1.96
            fig  = go.Figure()
            fig.add_trace(go.Scatter(
                x=pd.concat([seq_s["seq"], seq_s["seq"].iloc[::-1]]),
                y=pd.concat([seq_s["mean"]+ci95, (seq_s["mean"]-ci95).iloc[::-1]]),
                fill="toself", fillcolor="rgba(99,110,250,0.15)",
                line=dict(color="rgba(0,0,0,0)"), name="95% CI"))
            fig.add_trace(go.Scatter(x=seq_s["seq"], y=seq_s["mean"],
                mode="lines+markers", name="平均KDA",
                line=dict(color="#636EFA", width=2), marker=dict(size=6)))
            fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.2)")
            fig.update_layout(xaxis_title="セッション内試合番号", yaxis_title="KDA",
                              xaxis=dict(dtick=1), height=350, margin=dict(t=20,b=20))
            st.plotly_chart(fig, width="stretch")
            if len(seq_s) >= 3:
                r, p = scipy_stats.pearsonr(seq_s["seq"], seq_s["mean"])
                trend = "📉 後半に低下傾向あり" if r < -0.3 and p < 0.1 else "→ 明確な低下傾向なし"
                st.caption(f"相関係数 r = {r:.3f}（p = {p:.3f}）　{trend}")

    st.divider()

    # ダメージ差 箱ひげ図
    st.subheader("📦 マップ別 ダメージ差の分布")
    box_df = df_filtered.dropna(subset=["damage_diff"]).copy()
    if not box_df.empty:
        valid_maps = box_df["map_name"].value_counts()
        valid_maps = valid_maps[valid_maps >= 5].index.tolist()
        box_df = box_df[box_df["map_name"].isin(valid_maps)]
        map_order = box_df.groupby("map_name")["damage_diff"].median().sort_values().index.tolist()
        fig = go.Figure()
        for mn in map_order:
            mdf = box_df[box_df["map_name"] == mn]
            fig.add_trace(go.Box(y=mdf["damage_diff"], name=mn, boxmean=True,
                marker_color="#636EFA", line_color="#636EFA"))
        fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        fig.update_layout(yaxis_title="ダメージ差", xaxis_title="マップ",
                          showlegend=False, height=400, margin=dict(t=20,b=20))
        st.plotly_chart(fig, width="stretch")

    st.divider()

    # エンゲージメント密度
    st.subheader("⚡ エンゲージメント密度")
    st.caption("(キル + デス + アシスト) / 試合時間(分)。試合への関与の濃さ。ルール間・マップ間の比較に。")

    eng_df = df_filtered.dropna(subset=["engagement_density"]).copy()
    eng_df["result_label"] = eng_df["result"].map(RESULT_DISPLAY)

    if eng_df.empty:
        st.info("エンゲージメント密度のデータがありません。")
    else:
        col_eng1, col_eng2 = st.columns(2)

        # ルール別エンゲージメント密度（箱ひげ図）
        with col_eng1:
            st.markdown("**ルール別**")
            rule_order = (
                eng_df.groupby("rule_name")["engagement_density"]
                .median().sort_values(ascending=False).index.tolist()
            )
            fig_eng1 = px.box(
                eng_df, x="rule_name", y="engagement_density",
                category_orders={"rule_name": rule_order},
                color="rule_name",
                labels={"rule_name": "ルール", "engagement_density": "エンゲージメント密度"},
                points="outliers", height=380,
            )
            fig_eng1.update_layout(showlegend=False, margin=dict(t=20, b=20))
            st.plotly_chart(fig_eng1, width="stretch")

        # 勝敗別エンゲージメント密度（箱ひげ図）
        with col_eng2:
            st.markdown("**勝敗別**")
            fig_eng2 = px.box(
                eng_df, x="result_label", y="engagement_density", color="result_label",
                color_discrete_map={"勝ち": "#00CC96", "負け": "#EF553B", "引き分け": "#FFA15A"},
                labels={"result_label": "勝敗", "engagement_density": "エンゲージメント密度"},
                points="outliers", height=380,
            )
            fig_eng2.update_layout(showlegend=False, margin=dict(t=20, b=20))
            st.plotly_chart(fig_eng2, width="stretch")

        # エンゲージメント密度 × PWコントロール率 散布図（両方ある場合のみ）
        both_df = df_filtered.dropna(subset=["engagement_density", "pw_control_rate"]).copy()
        both_df["result_label"] = both_df["result"].map(RESULT_DISPLAY)
        if len(both_df) >= 5:
            st.markdown("**エンゲージメント密度 × PWコントロール率**")
            fig_both = px.scatter(
                both_df, x="engagement_density", y="pw_control_rate",
                color="result_label",
                color_discrete_map={"勝ち": "#00CC96", "負け": "#EF553B", "引き分け": "#FFA15A"},
                hover_data={"map_name": True, "rule_name": True},
                labels={
                    "engagement_density": "エンゲージメント密度",
                    "pw_control_rate": "PWコントロール率",
                    "result_label": "勝敗",
                },
                opacity=0.7, height=400,
            )
            fig_both.add_hline(y=0.5, line_dash="dash", line_color="rgba(255,255,255,0.2)")
            fig_both.update_traces(marker=dict(size=7))
            fig_both.update_layout(
                yaxis_tickformat=".0%",
                margin=dict(t=20, b=20),
                legend=dict(orientation="h", y=1.05),
            )
            st.plotly_chart(fig_both, width="stretch")

# ============================================================
# タブ④ オブジェクト
# ============================================================

OBJ_RULES = {
    "Oddball":     ["oddball_skull_time_sec","oddball_scoring_ticks","oddball_skull_grabs","oddball_carrier_kills","oddball_skulls_denied"],
    "Strongholds": ["zone_occupation_sec","zone_scoring_ticks","zone_captures","zone_def_kills","zone_off_kills","zone_secures"],
    "King of the Hill": ["zone_occupation_sec","zone_scoring_ticks","zone_def_kills","zone_off_kills"],
    "KOTH":        ["zone_occupation_sec","zone_scoring_ticks","zone_def_kills","zone_off_kills"],
    "CTF":         ["flag_captures","flag_grabs","flag_returns","flag_secures","flag_steals","flag_carrier_time_sec","flag_carriers_killed"],
}
OBJ_LABELS = {
    "oddball_skull_time_sec":"ボール保持時間（秒）","oddball_scoring_ticks":"スコアティック",
    "oddball_skull_grabs":"ボールグラブ","oddball_carrier_kills":"ボールキャリアキル","oddball_skulls_denied":"キャリア阻止",
    "zone_occupation_sec":"ゾーン占領時間（秒）","zone_scoring_ticks":"スコアティック",
    "zone_captures":"ゾーンキャプチャ","zone_def_kills":"ゾーン内防御キル","zone_off_kills":"ゾーン内攻撃キル","zone_secures":"ゾーンセキュア",
    "flag_captures":"旗キャプチャ","flag_grabs":"旗グラブ","flag_returns":"旗リターン",
    "flag_secures":"旗セキュア","flag_steals":"旗スティール",
    "flag_carrier_time_sec":"旗保持時間（秒）","flag_carriers_killed":"旗キャリアキル",
}

with tab4:
    active_rules = df_filtered["rule_name"].dropna().unique().tolist()
    matched_cols: list[str] = []
    for rule in active_rules:
        for pattern, cols in OBJ_RULES.items():
            if pattern.lower() in rule.lower():
                matched_cols = cols
                break
        if matched_cols:
            break

    if not matched_cols or not any(c in df_filtered.columns for c in matched_cols):
        st.info("オブジェクトルール（Oddball / Strongholds / KOTH / CTF）を選択するとスタッツが表示されます。")
    else:
        obj_df = df_filtered.dropna(subset=[matched_cols[0]]).copy()
        if obj_df.empty:
            st.info("このフィルター条件でオブジェクトスタッツが見つかりませんでした。")
        else:
            cols_per_row = min(len(matched_cols), 4)
            card_cols = st.columns(cols_per_row)
            for i, col in enumerate(matched_cols[:cols_per_row]):
                if col in obj_df.columns:
                    mean_val = obj_df[col].mean()
                    label    = OBJ_LABELS.get(col, col)
                    if pd.notna(mean_val):
                        card_cols[i % cols_per_row].metric(label, f"{mean_val:.1f}")

            primary_col = matched_cols[0]
            if primary_col in obj_df.columns:
                obj_df = obj_df.sort_values("played_at").copy()
                obj_df["x"] = range(len(obj_df))
                ma_col = obj_df[primary_col].rolling(5, min_periods=1).mean()
                fig = go.Figure()
                fig.add_trace(go.Bar(x=obj_df["x"], y=obj_df[primary_col],
                    marker_color=obj_df["result_flag"].map({1:"#00CC96",0:"#EF553B"}),
                    name=OBJ_LABELS.get(primary_col, primary_col)))
                fig.add_trace(go.Scatter(x=obj_df["x"], y=ma_col,
                    mode="lines", name="移動平均(5)", line=dict(color="white", width=2)))
                fig.update_layout(xaxis_title="試合番号",
                                  yaxis_title=OBJ_LABELS.get(primary_col, primary_col),
                                  height=300, margin=dict(t=20,b=20))
                st.plotly_chart(fig, width="stretch")

                obj_df["result_label"] = obj_df["result"].map(RESULT_DISPLAY)
                fig = px.box(obj_df, x="result_label", y=primary_col, color="result_label",
                    color_discrete_map={"勝ち":"#00CC96","負け":"#EF553B"},
                    labels={"result_label":"勝敗", primary_col: OBJ_LABELS.get(primary_col, primary_col)},
                    points="all", height=320)
                fig.update_layout(showlegend=False, margin=dict(t=20,b=20))
                st.plotly_chart(fig, width="stretch")

st.divider()

# マッチ一覧
st.subheader("📋 マッチ一覧")
display_cols = ["played_at","playlist","map_name","rule_name","result",
                "kills","deaths","assists","kd_ratio","accuracy","damage_diff",
                "csr_pre","csr_post","csr_delta","party_type","exclude_flag"]
available = [c for c in display_cols if c in df_filtered.columns]
show_df = df_filtered[available].copy().sort_values("played_at", ascending=False)
rename_map = {c: display_name(c) for c in available}
rename_map["playlist"] = "区分"
rename_map["result"]   = "勝敗"
show_df = show_df.rename(columns=rename_map)
if "区分" in show_df.columns:
    show_df["区分"] = show_df["区分"].map(PLAYLIST_DISPLAY).fillna(show_df["区分"])
if "勝敗" in show_df.columns:
    show_df["勝敗"] = show_df["勝敗"].map(RESULT_DISPLAY).fillna(show_df["勝敗"])
if "命中率" in show_df.columns:
    show_df["命中率"] = show_df["命中率"].apply(lambda x: f"{x:.1%}" if pd.notna(x) else "—")
st.dataframe(show_df, width="stretch", height=400)