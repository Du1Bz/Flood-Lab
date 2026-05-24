"""
app.py - Flood-Lab エントリポイント。5ページ構成。
起動方法: streamlit run app.py
"""
import streamlit as st

st.set_page_config(page_title="Flood-Lab", page_icon="🌊", layout="wide")

pg = st.navigation([
    st.Page("src/pages/app_home.py",    title="🌊 ホーム",      default=True),
    st.Page("src/pages/analysis.py",    title="📊 分析"),
    st.Page("src/pages/report.py",      title="📅 レポート"),
    st.Page("src/pages/hypothesis.py",  title="🔬 仮説検証"),
    st.Page("src/pages/history.py",     title="📋 試合履歴"),
])
pg.run()