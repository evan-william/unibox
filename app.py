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
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# APPLY CUSTOM STYLES
apply_custom_styles()

# SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="logo-container">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="6" fill="#4A90E2"/>
                    <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2" fill="none"/>
                    <circle cx="16" cy="16" r="3" fill="white"/>
                </svg>
                <div class="logo-text">
                    <h1>UniBox</h1>
                    <p>File Converter</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='sidebar-title'>Categories</h3>", unsafe_allow_html=True)
    
    # Custom category selector
    categories = {
        "Document Tools": """
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>
                <polyline points="10 9 9 9 8 9"/>
            </svg>
        """,
        "Media Tools": """
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>
            </svg>
        """,
        "Developer Tools": """
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>
            </svg>
        """
    }
    
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "Document Tools"
    
    for cat_name, icon in categories.items():
        is_active = st.session_state.selected_category == cat_name
        if st.button(
            cat_name,
            key=f"cat_{cat_name}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.selected_category = cat_name
            st.rerun()
        
    st.markdown("<div class='sidebar-spacer'></div>", unsafe_allow_html=True)
    
    # Footer info
    st.markdown("""
        <div class='sidebar-footer'>
            <div class='info-item'>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
                <span>Secure & Private</span>
            </div>
            <div class='info-item'>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                </svg>
                <span>Fast Processing</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# MAIN CONTENT
category = st.session_state.selected_category

if category == "Document Tools":
    document_tools.render()
elif category == "Media Tools":
    media_tools.render()
else:
    dev_tools.render()

# FOOTER
st.markdown("""
    <div class='main-footer'>
        <div class='footer-content'>
            <div class='footer-left'>
                <p>© 2026 UniBox - Built by Evan William</p>
            </div>
            <div class='footer-right'>
                <a href='#'>Privacy</a>
                <a href='#'>Terms</a>
                <a href='#'>Contact</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)