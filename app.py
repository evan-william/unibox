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
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# APPLY CUSTOM STYLES
apply_custom_styles()

# SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>⚡ UniBox</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 0.9em; margin-top: 0;'>Universal File Converter</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📂 Categories")
    category = st.selectbox(
        "Select Category",
        ["📄 Document Tools", "🎨 Media Tools", "⚙️ Dev & Data Tools"],
        label_visibility="collapsed"
    )

# MAIN CONTENT
if category == "📄 Document Tools":
    document_tools.render()
elif category == "🎨 Media Tools":
    media_tools.render()
else:
    dev_tools.render()

# FOOTER
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 0.85em;'>"
    "Built with Streamlit | © 2024 UniBox"
    "</div>",
    unsafe_allow_html=True
)