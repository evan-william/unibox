import streamlit as st
import sys
from pathlib import Path
import streamlit.components.v1 as components

# Add converters directory to path
sys.path.append(str(Path(__file__).parent))

from utils.styles import apply_custom_styles
from pages import document_tools, media_tools, dev_tools
from database import get_stats  # ✅ Import database stats

# PAGE CONFIG
st.set_page_config(
    page_title="UniBox - Universal File Converter",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# FORCE OPEN SIDEBAR JAVASCRIPT
components.html(
    """
    <script>
    var container = window.parent.document.querySelector("[data-testid='stSidebar']");
    var button = window.parent.document.querySelector('button[kind="headerNoPadding"]');
    if (container && container.getAttribute('aria-expanded') === 'false') {
        button.click();
    }
    </script>
    """,
    height=0,
    width=0,
)

# APPLY CUSTOM STYLES
apply_custom_styles()

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: flex !important;
            visibility: visible !important;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for category
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Document Tools"

# TOP NAVIGATION BAR
st.markdown("""
    <div class='top-nav'>
        <div class='nav-wrapper'>
            <div class='nav-brand'>
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="6" fill="url(#grad1)"/>
                    <path d="M16 9L21 12V20L16 23L11 20V12L16 9Z" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    <defs>
                        <linearGradient id="grad1" x1="0" y1="0" x2="32" y2="32">
                            <stop offset="0%" style="stop-color:#ff4757;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#ff6348;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                </svg>
                <span>UniBox</span>
            </div>
            <div class='nav-links'>
                <a class='nav-link'>Tools</a>
                <a class='nav-link'>API</a>
                <a class='nav-link'>Pricing</a>
            </div>
            <div class='nav-actions'>
                <button class='nav-button secondary'>Login</button>
                <button class='nav-button primary'>Sign Up</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
    <div class='hero-section'>
        <div class='hero-content'>
            <h1 class='hero-title'>File Converter</h1>
            <p class='hero-subtitle' style='text-align: center;'>
                UniBox is an online file converter. We support nearly all audio, video,
                document, ebook, archive, image, spreadsheet, and presentation formats.
                To get started, use the button below and select files to convert from your computer.
            </p>
            <div class='converter-selector'>
                <div class='selector-row'>
                    <div style='flex: 1;'>
                        <div class='selector-label'>Convert From</div>
                        <div id='from-select-placeholder'></div>
                    </div>
                    <div class='arrow-icon'>→</div>
                    <div style='flex: 1;'>
                        <div class='selector-label'>Convert To</div>
                        <div id='to-select-placeholder'></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="logo-container">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="32" height="32" rx="6" fill="url(#grad2)"/>
                    <path d="M16 9L21 12V20L16 23L11 20V12L16 9Z" stroke="white" stroke-width="2.5" fill="none"/>
                    <defs>
                        <linearGradient id="grad2" x1="0" y1="0" x2="32" y2="32">
                            <stop offset="0%" style="stop-color:#ff4757;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#ff6348;stop-opacity:1" />
                        </linearGradient>
                    </defs>
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
    
    st.markdown("<div class='sidebar-footer'>", unsafe_allow_html=True)
    st.markdown("""
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
        <div class='info-item'>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12 6 12 12 16 14"/>
            </svg>
            <span>No Installation</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# MAIN CONTENT WRAPPER
st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

# Category Navigation Tabs
col_left, col_center, col_right = st.columns([1, 8, 1])

with col_center:
    st.markdown("<div class='category-tabs'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Documents", use_container_width=True, type="primary" if st.session_state.selected_category == "Document Tools" else "secondary", key="tab_doc"):
            st.session_state.selected_category = "Document Tools"
            st.rerun()
    
    with col2:
        if st.button("Media", use_container_width=True, type="primary" if st.session_state.selected_category == "Media Tools" else "secondary", key="tab_media"):
            st.session_state.selected_category = "Media Tools"
            st.rerun()
    
    with col3:
        if st.button("Developer", use_container_width=True, type="primary" if st.session_state.selected_category == "Developer Tools" else "secondary", key="tab_dev"):
            st.session_state.selected_category = "Developer Tools"
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Render selected category
category = st.session_state.selected_category

if category == "Document Tools":
    document_tools.render()
elif category == "Media Tools":
    media_tools.render()
else:
    dev_tools.render()

st.markdown("</div>", unsafe_allow_html=True)

# STATS SECTION - NOW WITH REAL DATABASE DATA
try:
    stats = get_stats()
    total_files = stats['total_files_formatted']
    total_mb = stats['total_mb_formatted']  # ✅ GANTI dari total_tb ke total_mb
except Exception as e:
    # Fallback to default values if database not available
    total_files = "0"
    total_mb = "0"  

st.markdown(f"""
    <div class='stats-section'>
        <p class='stats-text'>
            We've already converted <span class='stats-number'>{total_files}</span> files 
            with a total size of <span class='stats-number'>{total_mb} MB</span>.
        </p>
    </div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div class='main-footer'>
        <div class='footer-content'>
            <div class='footer-left'>
                <p>© 2026 UniBox - Built by Evan William</p>
            </div>
            <div class='footer-right'>
                <a href='#'>About Us</a>
                <a href='#'>Privacy</a>
                <a href='#'>Terms</a>
                <a href='#'>Contact</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)