import streamlit as st
import sys
from pathlib import Path

# Add converters directory to path
sys.path.append(str(Path(__file__).parent))

from utils.styles import apply_custom_styles
from pages import document_tools, media_tools, dev_tools

# PAGE CONFIG
st.set_page_config(
    page_title="UniBox - Universal File Converter",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize dark mode state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True  # Default to dark mode like CloudConvert

# APPLY CUSTOM STYLES (with dark mode parameter)
apply_custom_styles(st.session_state.dark_mode)

# NAVIGATION BAR
def toggle_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("""
        <div class='navbar-brand'>
            <span class='brand-icon'>☁️</span>
            <span class='brand-text'>uni<strong>box</strong></span>
        </div>
    """, unsafe_allow_html=True)

with col2:
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    with nav_col1:
        if st.button("📄 Documents", key="nav_doc", use_container_width=True):
            st.session_state.category = "Document Tools"
    with nav_col2:
        if st.button("🎨 Media", key="nav_media", use_container_width=True):
            st.session_state.category = "Media Tools"
    with nav_col3:
        if st.button("💻 Developer", key="nav_dev", use_container_width=True):
            st.session_state.category = "Developer Tools"

with col3:
    mode_col1, mode_col2 = st.columns([3, 1])
    with mode_col2:
        st.button(
            "🌙" if not st.session_state.dark_mode else "☀️", 
            key="mode_toggle",
            on_click=toggle_mode
        )

st.markdown("<div class='navbar-divider'></div>", unsafe_allow_html=True)

# Initialize category if not set
if 'category' not in st.session_state:
    st.session_state.category = "Document Tools"

# MAIN CONTENT
if st.session_state.category == "Document Tools":
    document_tools.render()
elif st.session_state.category == "Media Tools":
    media_tools.render()
else:
    dev_tools.render()

# FOOTER
st.markdown("<div class='footer-space'></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='footer'>"
    "UniBox © 2026 - Built by Evan William"
    "</div>",
    unsafe_allow_html=True
)