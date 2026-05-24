# streamlit_app.py  ── “Home” page that sends users to the other pages
import streamlit as st

# ────────────────── page-wide settings ────────────────────────────────────
st.set_page_config(
    page_title="WireSense Home",
    layout="wide",
    initial_sidebar_state="collapsed",   # start with sidebar closed
)

# ──────────────────── headline & blurb ───────────────────────────────────
st.title("WireSense – Aluminium-Mill Toolkit")
st.markdown(
    """
    Welcome to **WireSense**.  
    Choose what you’d like to do:
    """
)

# ─────────────────── navigation buttons ──────────────────────────────────
# Map button labels to the *file names* in the pages/ folder
PAGE_MAP = {
    "📜 Live Monitor":              "pages/01_Live_Monitor.py",
    "🔄 Reverse Predictor":         "pages/02_Intial_Parameter_Prediction.py",
    "🎯 Target Feature Recommender":"pages/03_Target_Feature_Recommender.py",
}

# Lay buttons in a single row
cols = st.columns(len(PAGE_MAP))
for col, (label, target) in zip(cols, PAGE_MAP.items()):
    if col.button(label, use_container_width=True):
        # Streamlit ≥1.23 built-in page switch
        st.switch_page(target)

# ─────────────────── footer / version ────────────────────────────────────
st.markdown("---")
st.caption("© 2025 WireSense • Powered by Streamlit")
