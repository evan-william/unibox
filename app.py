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
    page_icon="■",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize dark mode state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# APPLY CUSTOM STYLES (with dark mode parameter)
apply_custom_styles(st.session_state.dark_mode)

# SIDEBAR
with st.sidebar:
    # Header and Mode Switcher in same row
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("<h1 style='text-align: left; margin-bottom: 8px; font-size: 28px;'>UniBox</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; font-size: 13px; margin-top: 0;'>Universal File Converter</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)
        # Use on_click to preserve state
        def toggle_mode():
            st.session_state.dark_mode = not st.session_state.dark_mode
        
        st.button(
            "🌙" if not st.session_state.dark_mode else "☀️", 
            key="mode_toggle",
            on_click=toggle_mode
        )
    
    st.markdown("---")
    
    st.markdown("### Categories")
    category = st.selectbox(
        "Select Category",
        ["Document Tools", "Media Tools", "Developer Tools"],
        label_visibility="collapsed"
    )

# MAIN CONTENT
if category == "Document Tools":
    document_tools.render()
elif category == "Media Tools":
    media_tools.render()
else:
    dev_tools.render()

# FOOTER
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #999; font-size: 13px;'>"
    "UniBox © 2026 - Built by Evan William"
    "</div>",
    unsafe_allow_html=True
)