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
    # Header with toggle switch
    st.markdown("<h1 style='text-align: left; margin-bottom: 8px; font-size: 28px;'>UniBox</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; font-size: 13px; margin-top: 0; margin-bottom: 16px;'>Universal File Converter</p>", unsafe_allow_html=True)
    
    # Custom toggle switch
    toggle_html = f"""
    <style>
    .theme-switch-wrapper {{
        display: flex;
        align-items: center;
        justify-content: flex-end;
        margin-bottom: 20px;
    }}
    
    .theme-switch {{
        display: inline-block;
        height: 34px;
        position: relative;
        width: 60px;
    }}
    
    .theme-switch input {{
        display: none;
    }}
    
    .slider {{
        background-color: #ccc;
        bottom: 0;
        cursor: pointer;
        left: 0;
        position: absolute;
        right: 0;
        top: 0;
        transition: .4s;
        border-radius: 34px;
    }}
    
    .slider:before {{
        background-color: white;
        bottom: 4px;
        content: "";
        height: 26px;
        left: 4px;
        position: absolute;
        transition: .4s;
        width: 26px;
        border-radius: 50%;
    }}
    
    input:checked + .slider {{
        background-color: #2c3e50;
    }}
    
    input:checked + .slider:before {{
        transform: translateX(26px);
    }}
    
    .slider .icon {{
        position: absolute;
        top: 7px;
        font-size: 18px;
        transition: .4s;
    }}
    
    .slider .sun {{
        left: 8px;
        opacity: {'0' if st.session_state.dark_mode else '1'};
    }}
    
    .slider .moon {{
        right: 8px;
        opacity: {'1' if st.session_state.dark_mode else '0'};
    }}
    </style>
    
    <div class="theme-switch-wrapper">
        <label class="theme-switch" for="checkbox">
            <input type="checkbox" id="checkbox" {'checked' if st.session_state.dark_mode else ''} 
                   onchange="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: this.checked}}, '*')">
            <div class="slider">
                <span class="icon sun">☀️</span>
                <span class="icon moon">🌙</span>
            </div>
        </label>
    </div>
    """
    
    # Display toggle and handle click
    toggle = st.components.v1.html(toggle_html, height=50)
    
    # Alternative: Simple checkbox that triggers rerun
    col1, col2, col3 = st.columns([2, 1, 1])
    with col3:
        if st.checkbox("", value=st.session_state.dark_mode, key="theme_toggle", label_visibility="collapsed"):
            if not st.session_state.dark_mode:
                st.session_state.dark_mode = True
                st.rerun()
        else:
            if st.session_state.dark_mode:
                st.session_state.dark_mode = False
                st.rerun()
    
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
    "UniBox © 2024 - Built by Evan William"
    "</div>",
    unsafe_allow_html=True
)