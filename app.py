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

# HORIZONTAL NAVIGATION BAR WITH LINKS
st.markdown("""
    <div class='top-nav'>
        <div class='nav-brand'>
            <div class='nav-left'>
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="6" fill="#c9302c"/>
                    <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2.5" fill="none"/>
                </svg>
                <span class='nav-brand-text'>UniBox</span>
            </div>
            <div class='nav-links'>
                <span class='nav-link'>Tools</span>
                <span class='nav-link'>API</span>
                <span class='nav-link'>
                    Pricing
                    <span class='nav-badge'>New</span>
                </span>
                <span class='nav-link'>Blog</span>
                <span class='nav-link'>Support</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# HERO SECTION WITH STATS
st.markdown("""
    <div class='hero-section'>
        <div class='hero-content'>
            <h1>Universal File Converter</h1>
            <p>
                Convert documents, media files, and developer formats with ease. 
                Professional quality, lightning-fast processing, and complete privacy protection.
                No sign-up required – start converting immediately.
            </p>
            <div class='stats-row'>
                <div class='stat-item'>
                    <span class='stat-number'>200+</span>
                    <span class='stat-label'>Formats Supported</span>
                </div>
                <div class='stat-item'>
                    <span class='stat-number'>1M+</span>
                    <span class='stat-label'>Files Converted</span>
                </div>
                <div class='stat-item'>
                    <span class='stat-number'>100%</span>
                    <span class='stat-label'>Secure & Private</span>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Content wrapper
st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

# Category Navigation Tabs
st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

# Center the tabs
tab_left, tab_center, tab_right = st.columns([2, 6, 2])

with tab_center:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Documents", use_container_width=True, type="primary" if st.session_state.selected_category == "Document Tools" else "secondary"):
            st.session_state.selected_category = "Document Tools"
            st.rerun()
    
    with col2:
        if st.button("🎬 Media", use_container_width=True, type="primary" if st.session_state.selected_category == "Media Tools" else "secondary"):
            st.session_state.selected_category = "Media Tools"
            st.rerun()
    
    with col3:
        if st.button("💻 Developer", use_container_width=True, type="primary" if st.session_state.selected_category == "Developer Tools" else "secondary"):
            st.session_state.selected_category = "Developer Tools"
            st.rerun()

st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="logo-container">
                <svg width="40" height="40" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="6" fill="#c9302c"/>
                    <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2.5" fill="none"/>
                </svg>
                <div class="logo-text">
                    <h1>UniBox</h1>
                    <p>FILE CONVERTER</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='sidebar-title'>Categories</h3>", unsafe_allow_html=True)
    
    categories = {
        "Document Tools": "📄",
        "Media Tools": "🎬",
        "Developer Tools": "💻"
    }
    
    for cat_name, icon in categories.items():
        is_active = st.session_state.selected_category == cat_name
        if st.button(
            f"{icon} {cat_name}",
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
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
                <span>Secure & Private</span>
            </div>
            <div class='info-item'>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>Fast Processing</span>
            </div>
            <div class='info-item'>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                </svg>
                <span>High Quality</span>
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
                <p>© 2026 UniBox • Made with ❤️ by Evan William</p>
            </div>
            <div class='footer-right'>
                <a href='#'>Privacy Policy</a>
                <a href='#'>Terms of Service</a>
                <a href='#'>Contact Us</a>
                <a href='#'>GitHub</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)