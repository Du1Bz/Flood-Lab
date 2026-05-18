"""
app.py - Flood-Lab エントリポイント。
st.navigation() でページを明示的に登録する（Streamlit 1.35.0+）。
起動方法: streamlit run app.py
"""
import streamlit as st

st.set_page_config(page_title="Flood-Lab", page_icon="🌊", layout="wide")

pg = st.navigation([
    st.Page("src/pages/app_home.py",  title="🌊 ホーム",        default=True),
    st.Page("src/pages/dashboard.py", title="📊 ダッシュボード"),
    st.Page("src/pages/report.py",    title="📈 定型レポート"),
    st.Page("src/pages/history.py",   title="📋 試合履歴"),
])
pg.run()