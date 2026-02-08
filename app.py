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

# MODERN HEADER WITH NAVIGATION
st.markdown("""
    <div class='modern-header'>
        <div class='header-content'>
            <div class='header-left'>
                <div class='logo-brand'>
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect width="32" height="32" rx="6" fill="url(#gradient)"/>
                        <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2.5" fill="none"/>
                        <defs>
                            <linearGradient id="gradient" x1="0" y1="0" x2="32" y2="32">
                                <stop offset="0%" stop-color="#c9302c"/>
                                <stop offset="100%" stop-color="#a02622"/>
                            </linearGradient>
                        </defs>
                    </svg>
                    <span class='brand-name'>UniBox</span>
                </div>
            </div>
            <div class='header-right'>
                <a href='#' class='header-link'>Pricing</a>
                <a href='#' class='header-link'>API</a>
                <a href='#' class='header-link'>Blog</a>
                <button class='header-btn-outline'>Sign In</button>
                <button class='header-btn-primary'>Get Started</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
    <div class='hero-section'>
        <div class='hero-content'>
            <h1 class='hero-title'>Universal File Converter</h1>
            <p class='hero-subtitle'>
                Convert your files between 200+ formats with ease. Fast, secure, and completely free. 
                Support for documents, images, videos, audio, and more.
            </p>
            
            <div class='conversion-selector'>
                <div class='selector-label'>Select your conversion:</div>
                <div class='selector-boxes'>
                    <div class='format-box'>
                        <span class='format-label'>from</span>
                        <div class='format-value' id='from-format'>Choose format...</div>
                    </div>
                    <div class='arrow-box'>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7"/>
                        </svg>
                    </div>
                    <div class='format-box'>
                        <span class='format-label'>to</span>
                        <div class='format-value' id='to-format'>Choose format...</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# CATEGORY TABS
st.markdown("<div class='content-container'>", unsafe_allow_html=True)

# Modern tab navigation
st.markdown("<div class='category-tabs'>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("📄 Documents", use_container_width=True, 
                 type="primary" if st.session_state.selected_category == "Document Tools" else "secondary",
                 key="tab_docs"):
        st.session_state.selected_category = "Document Tools"
        st.rerun()

with col3:
    if st.button("🎨 Media", use_container_width=True,
                 type="primary" if st.session_state.selected_category == "Media Tools" else "secondary",
                 key="tab_media"):
        st.session_state.selected_category = "Media Tools"
        st.rerun()

with col4:
    if st.button("💻 Developer", use_container_width=True,
                 type="primary" if st.session_state.selected_category == "Developer Tools" else "secondary",
                 key="tab_dev"):
        st.session_state.selected_category = "Developer Tools"
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)

# MAIN CONTENT
category = st.session_state.selected_category

if category == "Document Tools":
    document_tools.render()
elif category == "Media Tools":
    media_tools.render()
else:
    dev_tools.render()

st.markdown("</div>", unsafe_allow_html=True)

# STATS SECTION
st.markdown("""
    <div class='stats-section'>
        <div class='stats-container'>
            <div class='stat-item'>
                <div class='stat-number'>2.8B+</div>
                <div class='stat-label'>Files Converted</div>
            </div>
            <div class='stat-divider'></div>
            <div class='stat-item'>
                <div class='stat-number'>200+</div>
                <div class='stat-label'>Format Supported</div>
            </div>
            <div class='stat-divider'></div>
            <div class='stat-item'>
                <div class='stat-number'>22TB+</div>
                <div class='stat-label'>Total Data Processed</div>
            </div>
            <div class='stat-divider'></div>
            <div class='stat-item'>
                <div class='stat-number'>100%</div>
                <div class='stat-label'>Free to Use</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# WHY CHOOSE US SECTION
st.markdown("""
    <div class='why-choose-section'>
        <div class='section-header'>
            <h2>Why Choose UniBox?</h2>
            <p>Trusted by millions worldwide for fast, secure, and reliable file conversion</p>
        </div>
        
        <div class='features-showcase'>
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    </svg>
                </div>
                <h3>Bank-Level Security</h3>
                <p>ISO 27001 certified with end-to-end encryption. Your files are automatically deleted after conversion.</p>
            </div>
            
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12 6 12 12 16 14"/>
                    </svg>
                </div>
                <h3>Lightning Fast</h3>
                <p>Advanced algorithms ensure rapid conversion without compromising quality. Most files convert in seconds.</p>
            </div>
            
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                        <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                        <line x1="12" y1="22.08" x2="12" y2="12"/>
                    </svg>
                </div>
                <h3>200+ Formats</h3>
                <p>Support for all major file formats including documents, images, videos, audio, archives, and more.</p>
            </div>
            
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                        <circle cx="9" cy="7" r="4"/>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                    </svg>
                </div>
                <h3>No Registration</h3>
                <p>Start converting immediately. No account required, no software installation, completely hassle-free.</p>
            </div>
            
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                    </svg>
                </div>
                <h3>Highest Quality</h3>
                <p>Advanced conversion engines preserve formatting, colors, fonts, and all metadata perfectly.</p>
            </div>
            
            <div class='showcase-card'>
                <div class='showcase-icon'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                        <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                    </svg>
                </div>
                <h3>Cloud Powered</h3>
                <p>Process files of any size. Our cloud infrastructure handles everything without slowing down your device.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div class='modern-footer'>
        <div class='footer-container'>
            <div class='footer-grid'>
                <div class='footer-col'>
                    <h4>Company</h4>
                    <a href='#'>About Us</a>
                    <a href='#'>Careers</a>
                    <a href='#'>Press Kit</a>
                    <a href='#'>Contact</a>
                </div>
                
                <div class='footer-col'>
                    <h4>Resources</h4>
                    <a href='#'>Blog</a>
                    <a href='#'>Help Center</a>
                    <a href='#'>API Documentation</a>
                    <a href='#'>Status</a>
                </div>
                
                <div class='footer-col'>
                    <h4>Legal</h4>
                    <a href='#'>Privacy Policy</a>
                    <a href='#'>Terms of Service</a>
                    <a href='#'>Cookie Policy</a>
                    <a href='#'>GDPR</a>
                </div>
                
                <div class='footer-col'>
                    <h4>Connect</h4>
                    <a href='#'>Twitter</a>
                    <a href='#'>GitHub</a>
                    <a href='#'>LinkedIn</a>
                    <a href='#'>Discord</a>
                </div>
            </div>
            
            <div class='footer-bottom'>
                <p>© 2026 UniBox. Built with ❤️ by Evan William</p>
                <p class='footer-location'>Made in Surabaya, Indonesia 🇮🇩</p>
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
                    <rect width="32" height="32" rx="6" fill="url(#gradient)"/>
                    <path d="M16 8L22 12V20L16 24L10 20V12L16 8Z" stroke="white" stroke-width="2.5" fill="none"/>
                    <defs>
                        <linearGradient id="gradient" x1="0" y1="0" x2="32" y2="32">
                            <stop offset="0%" stop-color="#c9302c"/>
                            <stop offset="100%" stop-color="#a02622"/>
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
    
    st.markdown("<h3 class='sidebar-title'>Quick Access</h3>", unsafe_allow_html=True)
    
    categories = [
        ("Document Tools", "📄"),
        ("Media Tools", "🎨"),
        ("Developer Tools", "💻")
    ]
    
    for cat_name, icon in categories:
        is_active = st.session_state.selected_category == cat_name
        if st.button(
            f"{icon}  {cat_name}",
            key=f"cat_{cat_name}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.selected_category = cat_name
            st.rerun()
    
    st.markdown("<div class='sidebar-spacer'></div>", unsafe_allow_html=True)
    
    # Sidebar footer with stats
    st.markdown("""
        <div class='sidebar-stats'>
            <div class='sidebar-stat-item'>
                <div class='stat-value'>2.8B+</div>
                <div class='stat-desc'>Files Converted</div>
            </div>
            <div class='sidebar-stat-item'>
                <div class='stat-value'>200+</div>
                <div class='stat-desc'>Formats</div>
            </div>
        </div>
        
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
                <span>High Quality</span>
            </div>
            <div class='info-item'>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>Lightning Fast</span>
            </div>
        </div>
    """, unsafe_allow_html=True)