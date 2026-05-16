"""
app.py
------
Flood-Lab のエントリポイント。

起動方法:
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Flood-Lab",
    page_icon="🌊",
    layout="wide",
)

# ==================================================
# セッションステートの初期化
# ==================================================

if "df" not in st.session_state:
    st.session_state["df"] = None
if "config" not in st.session_state:
    st.session_state["config"] = None

# ==================================================
# データのロード（キャッシュ管理）
# ==================================================

@st.cache_data(show_spinner="DB を読み込み中...")
def _load(_db_path_str: str, _my_xuid: str):
    """キャッシュキーに db_path と xuid を使う。"""
    from pathlib import Path
    from src.core.config import AppConfig
    from src.core.database import load_matches
    from src.logic.processor import build_match_df

    cfg = AppConfig(my_xuid=_my_xuid, db_path=Path(_db_path_str))
    raw = load_matches(cfg)
    df  = build_match_df(raw, Path(_db_path_str), _my_xuid)
    return df, cfg


def get_data():
    """設定を読み込んでデータを返す。エラーは Streamlit UI で表示する。"""
    try:
        from src.core.config import load_config, find_openspartan_dbs
        cfg = load_config()
    except (ValueError, FileNotFoundError) as e:
        st.error(str(e))
        # 複数 DB が見つかった場合: セレクトボックスで選ばせる
        dbs = find_openspartan_dbs()
        if dbs:
            selected = st.selectbox(
                "使用するプロファイルを選択してください",
                options=dbs,
                format_func=lambda p: f"{p.stem}  ({p})",
            )
            if selected:
                from src.core.config import AppConfig
                xuid = f"xuid({selected.stem})"
                cfg  = AppConfig(my_xuid=xuid, db_path=selected)
            else:
                st.stop()
        else:
            st.stop()
        return None, None

    df, cfg = _load(str(cfg.db_path), cfg.my_xuid)
    return df, cfg


# ==================================================
# サイドバー: 更新ボタン
# ==================================================

with st.sidebar:
    st.title("🌊 Flood-Lab")
    if st.button("🔄 データ更新", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

# ==================================================
# メインページ: ナビ & データロード
# ==================================================

df, cfg = get_data()

if df is None or df.empty:
    st.info("試合データが見つかりませんでした。OpenSpartan Workshop を起動してデータを同期してください。")
    st.stop()

# セッションステートに保存（各ページから参照できるようにする）
st.session_state["df"]     = df
st.session_state["config"] = cfg

# トップページ: サマリー表示
st.title("🌊 Flood-Lab")
st.caption(f"プロファイル: {cfg.my_xuid}  |  DB: {cfg.db_path}")

# 全体スナップショット
rank_df = df[df["playlist"].isin(["ranked_arena", "ranked_slayer"])
             & (df["exclude_flag"] == "")]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("総試合数（ランク）",   len(rank_df))
col2.metric("勝率",                 f"{rank_df['result_flag'].mean():.1%}" if len(rank_df) else "—")
col3.metric("平均K/D",              f"{rank_df['kd_ratio'].mean():.2f}"   if len(rank_df) else "—")
col4.metric("平均インパクトスコア", f"{rank_df['impact_score'].mean():.2f}" if rank_df["impact_score"].notna().any() else "—")
col5.metric("全試合数（全体）",     len(df))

st.info("サイドバーのページリンクから各ビューを開いてください。")
