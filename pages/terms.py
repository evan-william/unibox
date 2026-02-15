import streamlit as st

def render():
    """Render Terms of Service page !!!"""
    
    # Hero Section
    st.markdown("""
        <div class='hero-section'>
            <div class='hero-content'>
                <h1 class='hero-title'>Terms of Service</h1>
                <p class='hero-subtitle'>
                    Please read these terms carefully before using UniBox.
                </p>
                <p style='color: #888; font-size: 14px; margin-top: 1rem;'>
                    Last updated: February 15, 2026
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='content-wrapper' style='max-width: 900px;'>", unsafe_allow_html=True)
    
    # Copy all the terms content from above...
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Agreement to Terms</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                By accessing and using UniBox, you agree to be bound by these Terms of Service.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)