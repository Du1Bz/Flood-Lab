"""
utils/session.py
----------------
セッションステートのデータロードと
サイドバー更新ボタンを各ページから呼ぶ共通処理。
"""

from __future__ import annotations

import streamlit as st
from pathlib import Path


@st.cache_data(show_spinner="DB を読み込み中...")
def _load(_db_path_str: str, _my_xuid: str):
    from src.core.config import AppConfig
    from src.core.database import load_matches
    from src.logic.processor import build_match_df

    cfg = AppConfig(my_xuid=_my_xuid, db_path=Path(_db_path_str))
    raw = load_matches(cfg)
    df  = build_match_df(raw, Path(_db_path_str), _my_xuid)
    return df, cfg


def load_data():
    """
    設定を読み込んでキャッシュ済みDataFrameを返す。
    セッションステートに保存するので2回目以降は即返す。
    """
    if st.session_state.get("df") is not None:
        return st.session_state["df"], st.session_state["config"]

    try:
        from src.core.config import load_config
        cfg = load_config()
    except (ValueError, FileNotFoundError) as e:
        st.error(str(e))
        from src.core.config import find_openspartan_dbs
        dbs = find_openspartan_dbs()
        if dbs:
            selected = st.selectbox(
                "使用するプロファイルを選択してください",
                options=dbs,
                format_func=lambda p: f"{p.stem}  ({p})",
            )
            if selected:
                from src.core.config import AppConfig
                cfg = AppConfig(my_xuid=f"xuid({selected.stem})", db_path=selected)
            else:
                st.stop()
        else:
            st.stop()
        return None, None

    df, cfg = _load(str(cfg.db_path), cfg.my_xuid)
    st.session_state["df"]     = df
    st.session_state["config"] = cfg
    return df, cfg


def sidebar_refresh():
    """サイドバーに更新ボタンを表示する。各ページの先頭で呼ぶ。"""
    with st.sidebar:
        if st.button("🔄 データ更新", use_container_width=True):
            st.cache_data.clear()
            st.session_state.pop("df", None)
            st.session_state.pop("config", None)
            st.rerun()
