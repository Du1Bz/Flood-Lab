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

match_options = (
    table_df["日時"] + "  " +
    table_df["区分"] + "  " +
    table_df["マップ"] + "  " +
    table_df["ルール"] + "  " +
    table_df["勝敗"]
)
selected_label = st.selectbox("試合を選択", options=match_options.tolist())

# ==================================================
# 指標ヘルプテキスト
# ==================================================

METRIC_HELP: dict[str, str] = {
    "kd_ratio":     "K/D（キルデスレシオ）\nキル数 ÷ デス数。デス=0のときはキル数をそのまま使う。\n1.0が均衡。高いほど死なずに倒せている。",
    "kda":          "KDA\nキル - デス + アシスト÷3。\nアシスト3回をキル1回相当とみなした総合貢献度。",
    "accuracy":     "命中率\n命中数 ÷ 発射数。\n高いほど弾を無駄撃ちせず当てられている。",
    "damage_diff":  "ダメージ差\n与ダメージ - 被ダメージ。\nプラスなら敵より多くダメージを与えた試合。",
    "k_rpi":        "K-RPI（キル相対パフォーマンス指数）\nTrueSkill2が予測した期待キル数に対する実績の比率。\n1.0=期待通り / >1.0=期待超え（ポップオフ） / <1.0=期待以下。",
    "d_rpi":        "D-RPI（デス相対パフォーマンス指数）\nTrueSkill2が予測した期待デス数に対して、実際に少なく死んだ比率。\n>1.0=期待より死ななかった（生存力高） / <1.0=期待より多く死んだ。",
    "impact_score": "インパクトスコア\n(K-RPI + D-RPI) ÷ 2。\nTrueSkill2基準の総合パフォーマンス指標。1.0が平均。",
    "lgai":         "LGAI（ロビー格差補正インパクト）\n敵チームMMR - 自チームCSR。\n正の値=格上相手のロビー / 0付近=均衡 / 負の値=格下相手。",
    "team_mmr":     "自チームMMR\n自チームの平均MMR（マッチメイクレーティング）。\nTrueSkill2がロビーバランスの計算に使う内部値。",
    "enemy_mmr":    "敵チームMMR\n敵チームの平均MMR。\nLGAIの計算にも使われる。自チームMMRとの差がロビーの格差。",
    "csr_pre":      "試合前CSR\nこの試合を始めた時点のCSR（Competitive Skill Rating）。\n公式ランク指標。456〜2500程度の範囲。",
    "csr_post":     "試合後CSR\nこの試合が終わった後のCSR。\n試合前CSRとの差がCSR増減。",
    "emmr_v2":      "eMMR v2（推定MMR）\nFload-Lab独自指標。カルマンフィルタで平滑化した推定MMR。\nCSRとスタッツを組み合わせてノイズを除いたスキルトレンドを表す。",
}

# ==================================================
# ゲージ・色付きメトリクス定義
# ==================================================

RANK_COLORS = {
    "red":    "#D85A30",
    "silver": "#8899AA",
    "blue":   "#5B8DD9",
    "purple": "#9B59B6",
}

def _rank(val, thresholds: list) -> str:
    """thresholds = [silver_min, blue_min, purple_min]"""
    if val is None or pd.isna(val):
        return "silver"
    if val >= thresholds[2]:
        return "purple"
    if val >= thresholds[1]:
        return "blue"
    if val >= thresholds[0]:
        return "silver"
    return "red"

STAT_THRESHOLDS = {
    "kd_ratio":     [0.9,  1.1,  1.3],
    "kda":          [-1.0, 0.0,  2.0],
    "accuracy":     [0.50, 0.55, 0.60],
    "damage_diff":  [-500, 0,    500],
    "k_rpi":        [0.9,  1.1,  1.2],
    "d_rpi":        [0.9,  1.1,  1.3],
    "impact_score": [0.9,  1.1,  1.2],
    "lgai":         [0,    100,  200],
    "csr_pre":      [900,  1200, 1500],
    "csr_post":     [900,  1200, 1500],
    "team_mmr":     [900,  1200, 1500],
    "enemy_mmr":    [900,  1200, 1500],
    "emmr_v2":      [900,  1200, 1500],
}

GAUGE_RANGE = {
    "kd_ratio":     (0,    2.0),
    "kda":          (-5,   5.0),
    "accuracy":     (0,    1.0),
    "damage_diff":  (-4000, 4000),
    "k_rpi":        (0,    2.0),
    "d_rpi":        (0,    2.0),
    "impact_score": (0,    2.0),
    "lgai":         (-500, 500),
    "csr_pre":      (0,    2000),
    "csr_post":     (0,    2000),
    "team_mmr":     (0,    2000),
    "enemy_mmr":    (0,    2000),
    "emmr_v2":      (0,    2000),
}


def _gauge_metric(label: str, val, fmt: str = "{:.2f}", col_key: str = "") -> None:
    """色付きゲージメトリクスを表示する。col_key に対応するヘルプが METRIC_HELP にあれば ℹ️ ツールチップを付ける。"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        st.metric(label, "—")
        return

    rank  = _rank(val, STAT_THRESHOLDS.get(col_key, [None, None, None])) if col_key in STAT_THRESHOLDS else "silver"
    color = RANK_COLORS[rank]

    if col_key in GAUGE_RANGE:
        g_min, g_max = GAUGE_RANGE[col_key]
        ratio = max(0.0, min(1.0, (float(val) - g_min) / (g_max - g_min))) if g_max != g_min else 0.5
    else:
        ratio = 0.5

    bar_w = int(ratio * 100)
    display_val = fmt if "%" in fmt else (fmt.format(val) if "{" in fmt else str(val))

    # ヘルプテキストがあればラベルに title 属性と ℹ️ を付ける
    help_text = METRIC_HELP.get(col_key, "")
    if help_text:
        # title属性内のダブルクォートをエスケープ、改行を&#10;に変換
        safe_help = help_text.replace('"', "&quot;").replace("\n", "&#10;")
        label_html = (
            f'<span title="{safe_help}" style="cursor:help">'
            f'{label} <span style="font-size:10px;opacity:0.5">ℹ</span>'
            f'</span>'
        )
    else:
        label_html = label

    st.markdown(f"""
<div style="margin-bottom:8px">
  <div style="font-size:11px;color:rgba(255,255,255,.5);margin-bottom:2px">{label_html}</div>
  <div style="font-size:18px;font-weight:500;color:{color}">{display_val}</div>
  <div style="background:rgba(255,255,255,.08);border-radius:3px;height:4px;margin-top:3px">
    <div style="background:{color};width:{bar_w}%;height:4px;border-radius:3px"></div>
  </div>
</div>
""", unsafe_allow_html=True)


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
        st.write(f"キル: {int(row.get('kills', 0))}　デス: {int(row.get('deaths', 0))}　アシスト: {int(row.get('assists', 0))}")
        _gauge_metric("K/D",       row.get("kd_ratio"),    "{:.2f}",  "kd_ratio")
        _gauge_metric("KDA",       row.get("kda"),          "{:.2f}",  "kda")
        acc = row.get("accuracy")
        if pd.notna(acc):
            _gauge_metric("命中率", acc, f"{float(acc):.1%}", "accuracy")
        else:
            st.metric("命中率", "—")
        _gauge_metric("ダメージ差", row.get("damage_diff"), "{:+.0f}", "damage_diff")
        st.write(f"与ダメージ: {int(row.get('damage_dealt', 0)):,}")
        st.write(f"被ダメージ: {int(row.get('damage_taken', 0)):,}")
        st.write(f"重火器キル: {int(row.get('power_kills', 0))}　パーフェクトキル: {int(row.get('perfect_kills', 0))}")
        st.write(f"チーム内順位: {row.get('team_rank', '—')}")

    with col3:
        st.markdown("**📊 TrueSkill2 / MMR**")
        ek = row.get("expected_kills")
        ed = row.get("expected_deaths")
        st.write(f"期待キル: {ek:.1f}" if pd.notna(ek) else "期待キル: —")
        st.write(f"期待デス: {ed:.1f}" if pd.notna(ed) else "期待デス: —")
        _gauge_metric("K-RPI",        row.get("k_rpi"),        "{:.3f}", "k_rpi")
        _gauge_metric("D-RPI",        row.get("d_rpi"),        "{:.3f}", "d_rpi")
        _gauge_metric("インパクトスコア", row.get("impact_score"), "{:.3f}", "impact_score")
        _gauge_metric("LGAI",         row.get("lgai"),         "{:+.0f}", "lgai")
        _gauge_metric("自チームMMR",  row.get("team_mmr"),     "{:.0f}",  "team_mmr")
        _gauge_metric("敵チームMMR",  row.get("enemy_mmr"),    "{:.0f}",  "enemy_mmr")
        cp = row.get("csr_pre")
        co = row.get("csr_post")
        cd = row.get("csr_delta")
        _gauge_metric("試合前CSR",    cp, "{:.0f}", "csr_pre")
        _gauge_metric("試合後CSR",    co, "{:.0f}", "csr_post")
        st.write(f"CSR増減: {int(cd):+d}" if pd.notna(cd) else "CSR増減: —")
        _gauge_metric("eMMR v2",      row.get("emmr_v2"),      "{:.0f}",  "emmr_v2")
        st.write(f"パーティ: {row.get('party_type', '—')}")
        st.write(f"セッションID: {row.get('session_id', '—')} / 試合番号: {row.get('session_seq', '—')}")

    # オブジェクトスタッツ（該当ルールのみ表示）
    OBJ_SECTIONS = {
        "oddball": {
            "label": "🎱 Oddball スタッツ",
            "fields": [
                ("oddball_skull_time_sec", "ボール保持時間（秒）"),
                ("oddball_scoring_ticks",  "スコアティック"),
                ("oddball_skull_grabs",    "ボールグラブ"),
                ("oddball_carrier_kills",  "ボールキャリアキル"),
                ("oddball_skulls_denied",  "キャリア阻止"),
            ],
        },
        "strongholds": {
            "label": "🏰 Strongholds スタッツ",
            "fields": [
                ("zone_occupation_sec", "ゾーン占領時間（秒）"),
                ("zone_scoring_ticks",  "スコアティック"),
                ("zone_captures",       "ゾーンキャプチャ"),
                ("zone_def_kills",      "防御キル"),
                ("zone_off_kills",      "攻撃キル"),
                ("zone_secures",        "ゾーンセキュア"),
            ],
        },
        "koth": {
            "label": "👑 KOTH スタッツ",
            "fields": [
                ("zone_occupation_sec", "ヒル保持時間（秒）"),
                ("zone_scoring_ticks",  "スコアティック"),
                ("zone_def_kills",      "防御キル"),
                ("zone_off_kills",      "攻撃キル"),
            ],
        },
        "ctf": {
            "label": "🚩 CTF スタッツ",
            "fields": [
                ("flag_captures",         "旗キャプチャ"),
                ("flag_grabs",            "旗グラブ"),
                ("flag_returns",          "旗リターン"),
                ("flag_secures",          "旗セキュア"),
                ("flag_steals",           "旗スティール"),
                ("flag_carrier_time_sec", "旗保持時間（秒）"),
                ("flag_carriers_killed",  "旗キャリアキル"),
            ],
        },
    }

    rule = (row.get("rule_name") or "").lower()
    if "oddball" in rule:
        section = OBJ_SECTIONS["oddball"]
    elif "stronghold" in rule:
        section = OBJ_SECTIONS["strongholds"]
    elif "king" in rule or "koth" in rule:
        section = OBJ_SECTIONS["koth"]
    elif "ctf" in rule or "capture" in rule:
        section = OBJ_SECTIONS["ctf"]
    else:
        section = None

    if section:
        has_data = any(pd.notna(row.get(f)) for f, _ in section["fields"])
        if has_data:
            st.markdown(f"**{section['label']}**")
            obj_cols_display = st.columns(len(section["fields"]))
            for i, (field, label) in enumerate(section["fields"]):
                val = row.get(field)
                obj_cols_display[i].metric(
                    label,
                    f"{int(val)}" if pd.notna(val) else "—"
                )