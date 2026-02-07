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

# Initialize session state for category
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Document Tools"

# HORIZONTAL NAVIGATION BAR (MAIN CONTENT)
st.markdown("""
    <div class='top-nav'>
        <div class='nav-brand'>
            <svg width="28" height="28" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="32" height="32" rx="4" fill="#c9302c"/>
                <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2" fill="none"/>
            </svg>
            <span>UniBox</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Category Navigation Tabs
st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2, 2, 2, 6])

with col1:
    if st.button("Documents", use_container_width=True, type="primary" if st.session_state.selected_category == "Document Tools" else "secondary"):
        st.session_state.selected_category = "Document Tools"
        st.rerun()

with col2:
    if st.button("Media", use_container_width=True, type="primary" if st.session_state.selected_category == "Media Tools" else "secondary"):
        st.session_state.selected_category = "Media Tools"
        st.rerun()

with col3:
    if st.button("Developer", use_container_width=True, type="primary" if st.session_state.selected_category == "Developer Tools" else "secondary"):
        st.session_state.selected_category = "Developer Tools"
        st.rerun()

st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

# SIDEBAR (OPTIONAL)
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="logo-container">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="4" fill="#c9302c"/>
                    <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2" fill="none"/>
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
    
    categories = ["Document Tools", "Media Tools", "Developer Tools"]
    
    for cat_name in categories:
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

st.markdown("</div>", unsafe_allow_html=True)

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