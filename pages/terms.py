import streamlit as st

def render():
    """Render Terms of Service page"""
    
    # BACK TO HOME 
    st.markdown("""
        <style>
        /* 1. Styling Tombol Utama (Gradien Merah UniBox) */
        .stButton > button {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.6rem 2.5rem !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 71, 87, 0.3) !important;
            display: block;
            margin-top: 2rem !important;
            margin-bottom: 2rem !important;
        }
        
        /* 2. Efek Hover agar Interaktif */
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 71, 87, 0.5) !important;
            border: none !important;
            color: white !important;
        }

        /* 3. Efek Klik (Active) */
        .stButton > button:active {
            transform: translateY(0px) !important;
        }
        </style>
    """, unsafe_allow_html=True)
        
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
    
    # Introduction
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Agreement to Terms</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                By accessing and using UniBox ("the Service"), you agree to be bound by these Terms of Service 
                ("Terms"). If you disagree with any part of these terms, you may not access the Service.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Service Description
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>1. Description of Service</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                UniBox provides an online file conversion service for documents, media, and developer formats.
                The Service is provided "as is" and we reserve the right to modify or discontinue at any time.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # User Obligations
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>2. User Obligations</h2>
            <h3 style='font-size: 20px; margin: 1.5rem 0 0.75rem 0; color: #fff;'>2.1 Acceptable Use</h3>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>You agree to use UniBox only for lawful purposes. You must not:</p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li>Upload illegal content or malware</li>
                <li>Infringe intellectual property rights</li>
                <li>Attempt unauthorized access</li>
                <li>Abuse or overload our servers</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Disclaimers
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>3. Disclaimers</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                The Service is provided "AS IS" without warranties. We are not liable for any damages 
                arising from use of the Service. Always keep backup copies of important files.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact
    st.markdown("""
        <div class='tool-card' style='background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
             border: 2px solid rgba(255, 71, 87, 0.3); text-align: center;'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Questions?</h2>
            <p style='color: #b0b0b0; font-size: 15px;'>Contact us if you have questions about these Terms.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)