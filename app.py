import streamlit as st
import sys
from pathlib import Path
import streamlit.components.v1 as components

# Add converters directory to path !
sys.path.append(str(Path(__file__).parent))

from utils.styles import apply_custom_styles
from pages import document_tools, media_tools, dev_tools, about, privacy, terms, contact
from database import get_stats

# PAGE CONFIG (STREAMLIT)
st.set_page_config(
    page_title="UniBox - Universal File Converter",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# FORCE OPEN SIDEBAR JAVASCRIPT ESPECIALLY FOR LAPTOP/PC !!!
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

# Initialize session state
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Document Tools"

if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# Handle query parameters for footer navigation 
query_params = st.query_params
if 'page' in query_params:
    requested_page = query_params['page']
    if requested_page in ['about', 'privacy', 'terms', 'contact']:
        st.session_state.current_page = requested_page
    else:
        st.session_state.current_page = "home"

# TOP NAVIGATION BAR !
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

# Check if we're on a footer page
if st.session_state.current_page != "home":
    # HIDE SIDEBAR FOR FOOTER PAGES - FULLY HIDDEN WITH ALL ELEMENTS
    st.markdown("""
        <style>
        /* NUCLEAR OPTION - Hide ALL sidebar elements completely */
        [data-testid="stSidebar"],
        section[data-testid="stSidebar"],
        .st-emotion-cache-1ob5c3r,
        .e9ic3ti0,
        [data-testid="stSidebarContent"],
        .st-emotion-cache-155jwzh,
        .e9ic3ti2,
        [data-testid="stSidebarNav"],
        .st-emotion-cache-fsmas1,
        .e1pqlk430,
        [data-testid="stSidebarNavItems"],
        .st-emotion-cache-1gczx66,
        .e1pqlk431,
        [data-testid="stSidebarNavLink"],
        [data-testid="stSidebarNavLinkContainer"],
        .st-emotion-cache-1gb1rig,
        .e1pqlk432,
        .st-emotion-cache-hqtgao,
        .st-emotion-cache-1erimsn,
        .e1pqlk435,
        [data-testid="stSidebarHeader"],
        .st-emotion-cache-10p9htt,
        .e9ic3ti4,
        [data-testid="stSidebarUserContent"],
        .st-emotion-cache-1echtaq,
        .e9ic3ti1,
        [data-testid="stSidebarCollapseButton"],
        .st-emotion-cache-13veyas,
        .e9ic3ti10,
        [data-testid="stLogoSpacer"],
        .st-emotion-cache-11ukie,
        .e9ic3ti9,
        section.st-emotion-cache-1ob5c3r.e9ic3ti0,
        .st-emotion-cache-1sv6ehc,
        .e9ic3ti3 {
            display: none !important;
            visibility: hidden !important;
            width: 0 !important;
            min-width: 0 !important;
            max-width: 0 !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            opacity: 0 !important;
            pointer-events: none !important;
            position: absolute !important;
            left: -9999px !important;
            overflow: hidden !important;
        }
        
        /* Force hide sidebar navigation links */
        a[data-testid="stSidebarNavLink"],
        li.st-emotion-cache-1ag8dug.e1pqlk434,
        div.st-emotion-cache-1gb1rig.e1pqlk432 {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Expand main content to full width */
        .main .block-container {
            max-width: 100% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            margin-left: 0 !important;
        }
        
        .main {
            margin-left: 0 !important;
        }
        
        /* Remove sidebar toggle button completely */
        [data-testid="collapsedControl"],
        button[kind="headerNoPadding"],
        button.st-emotion-cache-pkm19r.e1mwqyj915,
        .st-emotion-cache-13veyas.e9ic3ti10 button {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        /* Force main container to full width without sidebar space */
        [data-testid="stAppViewContainer"] > section:first-child {
            width: 0 !important;
            flex-shrink: 1 !important;
            display: none !important;
        }
        
        /* Ensure no sidebar space is reserved */
        .st-emotion-cache-1ob5c3r.e9ic3ti0 {
            width: 0 !important;
            flex-shrink: 0 !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        /* Hide resize handle */
        div[style*="cursor: col-resize"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Render footer pages !
    if st.session_state.current_page == "about":
        about.render()
    elif st.session_state.current_page == "privacy":
        privacy.render()
    elif st.session_state.current_page == "terms":
        terms.render()
    elif st.session_state.current_page == "contact":
        contact.render()
    
    # Back to home button
    st.markdown("<div class='content-wrapper' style='text-align: center; margin-top: 2rem;'>", unsafe_allow_html=True)
    if st.button("← Back to Home", key="back_home"):
        st.session_state.current_page = "home"
        st.query_params.clear()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
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

    # SIDEBAR ENABLER
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

    # MAIN CONTENT WRAPPER HERE
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

    # The 3 Category Navigation Tabs !
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

    # STATS SECTION
    try:
        stats = get_stats()
        total_files = stats['total_files_formatted']
        total_size = stats['size_formatted']
    except Exception as e:
        total_files = "0"
        total_size = "0 KB" 

    st.markdown(f"""
        <div class='stats-section'>
            <p class='stats-text'>
                We've already converted <span class='stats-number'>{total_files}</span> files 
                with a total size of <span class='stats-number'>{total_size}</span>.
            </p>
        </div>
    """, unsafe_allow_html=True)

# FOOTER (shown on all pages FOR CONSISTENCY)
st.markdown("---") 

# LAYOUT LINK FOOTER
foot_col1, foot_col2 = st.columns([2, 1])

with foot_col1:
    st.markdown(f"<p style='color: #888; font-size: 14px;'>© 2026 UniBox - Built by Evan William</p>", unsafe_allow_html=True)

with foot_col2:
    # BUTTON LINK STYLING
    st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] button {
            background: none !important;
            border: none !important;
            padding: 0 !important;
            color: #888 !important;
            text-decoration: none !important;
            font-size: 14px !important;
            font-weight: normal !important;
        }
        div[data-testid="stHorizontalBlock"] button:hover {
            color: #ff4757 !important;
            text-decoration: underline !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("About", key="f_about"):
        st.session_state.current_page = "about"
        st.rerun()
    if c2.button("Privacy", key="f_priv"):
        st.session_state.current_page = "privacy"
        st.rerun()
    if c3.button("Terms", key="f_terms"):
        st.session_state.current_page = "terms"
        st.rerun()
    if c4.button("Contact", key="f_cont"):
        st.session_state.current_page = "contact"
        st.rerun()