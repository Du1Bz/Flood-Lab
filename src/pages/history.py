"""
pages/history.py
----------------
試合履歴ビュー。

全試合を時系列で確認できる。除外フラグの有無にかかわらず全件表示。
行クリックで全フィールドの詳細展開。
"""

from __future__ import annotations

import streamlit as st
import pandas as pd
from datetime import date, timedelta

from src.utils.display import (
    PLAYLIST_DISPLAY,
    RESULT_DISPLAY,
    display_name,
)
from src.utils.helpers import format_duration

st.set_page_config(page_title="試合履歴 | Flood-Lab", layout="wide")

from src.utils.session import load_data, sidebar_refresh
sidebar_refresh()
df, _ = load_data()

if df is None or df.empty:
    st.warning("データをロードできませんでした。")
    st.stop()

df_all = df.copy()

# ==================================================
# サイドバー: フィルター
# ==================================================

with st.sidebar:
    st.header("フィルター")

    # 期間
    period_mode = st.radio("期間", ["すべて", "今週", "今月", "直近N戦", "カスタム"], index=0)

    if period_mode == "今週":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        week_start = today - timedelta(days=today.weekday())
        df_filtered = df_all[df_all["played_at"] >= week_start]
    elif period_mode == "今月":
        today = pd.Timestamp.now(tz="Asia/Tokyo")
        month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        df_filtered = df_all[df_all["played_at"] >= month_start]
    elif period_mode == "直近N戦":
        n = st.slider("直近N戦", 10, 500, 50, step=10)
        df_filtered = df_all.tail(n)
    elif period_mode == "カスタム":
        col_a, col_b = st.columns(2)
        date_from = col_a.date_input("開始日", value=date.today() - timedelta(days=30))
        date_to   = col_b.date_input("終了日", value=date.today())
        df_filtered = df_all[
            (df_all["played_at"].dt.date >= date_from) &
            (df_all["played_at"].dt.date <= date_to)
        ]
    else:
        df_filtered = df_all.copy()

    # 区分
    playlist_options = ["すべて"] + [
        PLAYLIST_DISPLAY.get(p, p) for p in sorted(df_filtered["playlist"].dropna().unique())
    ]
    playlist_sel = st.selectbox("区分", playlist_options)
    if playlist_sel != "すべて":
        inv = {v: k for k, v in PLAYLIST_DISPLAY.items()}
        df_filtered = df_filtered[df_filtered["playlist"] == inv.get(playlist_sel, playlist_sel)]

    # マップ
    map_options = ["すべて"] + sorted(df_filtered["map_name"].dropna().unique().tolist())
    map_sel = st.selectbox("マップ", map_options)
    if map_sel != "すべて":
        df_filtered = df_filtered[df_filtered["map_name"] == map_sel]

    # ルール
    rule_options = ["すべて"] + sorted(df_filtered["rule_name"].dropna().unique().tolist())
    rule_sel = st.selectbox("ルール", rule_options)
    if rule_sel != "すべて":
        df_filtered = df_filtered[df_filtered["rule_name"] == rule_sel]

    # 除外フラグ
    st.divider()
    show_excluded = st.checkbox("除外フラグのある試合も表示", value=True)
    if not show_excluded:
        df_filtered = df_filtered[df_filtered["exclude_flag"] == ""]

    st.caption(f"表示試合数: **{len(df_filtered)}**")

# ==================================================
# メインコンテンツ
# ==================================================

st.title("📋 試合履歴")

if df_filtered.empty:
    st.info("該当する試合がありません。")
    st.stop()

# ==================================================
# 一覧テーブル
# ==================================================

table_df = df_filtered.sort_values("played_at", ascending=False).copy()

# 表示用に整形
table_df["日時"]       = table_df["played_at"].dt.tz_convert("Asia/Tokyo").dt.strftime("%Y-%m-%d %H:%M")
table_df["区分"]       = table_df["playlist"].map(PLAYLIST_DISPLAY).fillna(table_df["playlist"])
table_df["マップ"]     = table_df["map_name"]
table_df["ルール"]     = table_df["rule_name"]
table_df["勝敗"]       = table_df["result"].map(RESULT_DISPLAY).fillna(table_df["result"])
table_df["K/D"]        = table_df["kd_ratio"]
table_df["KDA"]        = table_df["kda"]
table_df["命中率"]     = table_df["accuracy"].apply(lambda x: f"{x:.1%}" if pd.notna(x) else "—")
table_df["ダメージ差"] = table_df["damage_diff"].apply(lambda x: f"{int(x):+d}" if pd.notna(x) else "—")
table_df["CSR増減"]    = table_df["csr_delta"].apply(lambda x: f"{int(x):+d}" if pd.notna(x) else "—")
table_df["試合時間"]   = table_df["duration_sec"].apply(format_duration)
table_df["パーティ"]   = table_df["party_type"]
table_df["除外"]       = table_df["exclude_flag"].apply(lambda x: f"⚠️ {x}" if x else "")

display_cols = ["日時", "区分", "マップ", "ルール", "勝敗",
                "K/D", "KDA", "命中率", "ダメージ差", "CSR増減",
                "試合時間", "パーティ", "除外"]

st.dataframe(
    table_df[display_cols],
    hide_index=True,
    width="stretch",
    height=500,
)

# ==================================================
# 試合詳細（選択展開）
# ==================================================

st.divider()
st.subheader("🔍 試合詳細")

match_options = table_df["日時"] + "  " + table_df["マップ"] + "  " + table_df["勝敗"]
selected_label = st.selectbox("試合を選択", options=match_options.tolist())

if selected_label:
    idx = match_options[match_options == selected_label].index[0]
    row = df_filtered.loc[idx]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**📌 基本情報**")
        st.write(f"試合ID: `{row.get('match_id', '—')}`")
        st.write(f"日時: {pd.Timestamp(row['played_at']).tz_convert('Asia/Tokyo').strftime('%Y-%m-%d %H:%M')}")
        st.write(f"区分: {PLAYLIST_DISPLAY.get(row.get('playlist', ''), row.get('playlist', '—'))}")
        st.write(f"マップ: {row.get('map_name', '—')}")
        st.write(f"ルール: {row.get('rule_name', '—')}")
        st.write(f"勝敗: {RESULT_DISPLAY.get(row.get('result', ''), row.get('result', '—'))}")
        st.write(f"試合時間: {format_duration(row.get('duration_sec'))}")
        st.write(f"除外フラグ: {row.get('exclude_flag') or 'なし'}")

    with col2:
        st.markdown("**⚔️ 個人スタッツ**")
        st.write(f"キル: {int(row.get('kills', 0))}")
        st.write(f"デス: {int(row.get('deaths', 0))}")
        st.write(f"アシスト: {int(row.get('assists', 0))}")
        st.write(f"K/D: {row.get('kd_ratio', '—')}")
        st.write(f"KDA: {row.get('kda', '—')}")
        kd = row.get('accuracy')
        st.write(f"命中率: {kd:.1%}" if pd.notna(kd) else "命中率: —")
        st.write(f"与ダメージ: {int(row.get('damage_dealt', 0)):,}")
        st.write(f"被ダメージ: {int(row.get('damage_taken', 0)):,}")
        dd = row.get('damage_diff')
        st.write(f"ダメージ差: {int(dd):+,}" if pd.notna(dd) else "ダメージ差: —")
        st.write(f"重火器キル: {int(row.get('power_kills', 0))}")
        st.write(f"パーフェクトキル: {int(row.get('perfect_kills', 0))}")
        st.write(f"チーム内順位: {row.get('team_rank', '—')}")

    with col3:
        st.markdown("**📊 TrueSkill2 / MMR**")
        ek = row.get('expected_kills')
        ed = row.get('expected_deaths')
        st.write(f"期待キル: {ek:.1f}" if pd.notna(ek) else "期待キル: —")
        st.write(f"期待デス: {ed:.1f}" if pd.notna(ed) else "期待デス: —")
        kr = row.get('k_rpi')
        dr = row.get('d_rpi')
        st.write(f"K-RPI: {kr:.3f}" if pd.notna(kr) else "K-RPI: —")
        st.write(f"D-RPI: {dr:.3f}" if pd.notna(dr) else "D-RPI: —")
        lg = row.get('lgai')
        st.write(f"LGAI: {lg:.0f}" if pd.notna(lg) else "LGAI: —")
        im = row.get('impact_score')
        st.write(f"インパクトスコア: {im:.3f}" if pd.notna(im) else "インパクトスコア: —")
        st.write(f"自チームMMR: {int(row['team_mmr']) if pd.notna(row.get('team_mmr')) else '—'}")
        st.write(f"敵チームMMR: {int(row['enemy_mmr']) if pd.notna(row.get('enemy_mmr')) else '—'}")
        cp = row.get('csr_pre')
        co = row.get('csr_post')
        cd = row.get('csr_delta')
        st.write(f"試合前CSR: {int(cp) if pd.notna(cp) else '—'}")
        st.write(f"試合後CSR: {int(co) if pd.notna(co) else '—'}")
        st.write(f"CSR増減: {int(cd):+d}" if pd.notna(cd) else "CSR増減: —")
        st.write(f"eMMR v2: {row['emmr_v2']:.0f}" if pd.notna(row.get('emmr_v2')) else "eMMR v2: —")
        st.write(f"パーティ: {row.get('party_type', '—')}")
        st.write(f"セッションID: {row.get('session_id', '—')} / 試合番号: {row.get('session_seq', '—')}")