import streamlit as st

def render():
    """Render Contact page with clean professional design"""
    
    # 1. Hero Section
    st.markdown("""
        <div class='hero-section'>
            <div class='hero-content'>
                <h1 class='hero-title'>Get in Touch</h1>
                <p class='hero-subtitle'>
                    Have questions, feedback, or need support? We'd love to hear from you!
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # TITLE SECTION 
    st.markdown("<div class='content-wrapper' style='max-width: 800px; margin: 0 auto; padding: 0 1rem;'>", unsafe_allow_html=True)

    # SUBTITLE
    st.markdown("""
        <div style='margin-bottom: 2rem; padding-left: 5px; margin-top: 2rem; '> 
            <h2 style='font-size: 26px; margin-bottom: 0.5rem; color: #fff; font-weight: 700;'>Send Us a Message</h2>
            <p style='color: #888; font-size: 15px;'>
                Fill out the form below and we'll get back to you within 48 hours.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # CSS FOR FORM
    st.markdown("""
        <style>
        /* Spacing antar elemen form global */
        [data-testid="stForm"] {
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            padding: 2rem !important;
            background: rgba(255, 255, 255, 0.02) !important;
            border-radius: 15px !important;
        }

        /* Memberikan jarak antar field (Input & Textarea) */
        .stTextInput, .stTextArea, .stSelectbox {
            margin-bottom: 1.2rem !important;
        }

        /* Label styling */
        .stMarkdown p {
            margin-bottom: 0.5rem !important;
        }

        /* Premium Form Input Styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {
            background: #1e1e1e !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
            padding: 12px 16px !important;
        }
        
        /* Submit Button ADDED margin top... jelek kalau gak */
        [data-testid="stForm"] .stButton > button {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.75rem 3rem !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 71, 87, 0.3) !important;
            width: 100%;
            margin-top: 2 rem;
        }

        [data-testid="stForm"] .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 71, 87, 0.5) !important;
            border: none !important;
        }

        /* Spacing for FAQ */
        .streamlit-expanderHeader {
            margin-bottom: 10px !important;
            background: #1e1e1e !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Contact Form
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name *", placeholder="John Doe")
        with col2:
            email = st.text_input("Email Address *", placeholder="john@example.com")
        
        subject = st.selectbox("Subject *", [
            "General Inquiry", "Technical Support", "Feature Request", 
            "Bug Report", "Business/Partnership", "Other"
        ])
        
        message = st.text_area("Your Message *", placeholder="Tell us how we can help you...", height=180)
        
        # Menggunakan kolom untuk memposisikan button di tengah (opsional) atau full width
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields.")
    
    #  FAQ Section
    st.markdown("""
        <div style='margin-top: 5rem; margin-bottom: 2rem;'>
            <h2 style='font-size: 32px; margin-bottom: 1.5rem; color: #fff; text-align: center; font-weight: 800;'>
                Frequently Asked Questions
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    faqs = [
        ("How long does file conversion take?", "Most conversions complete within seconds. Our advanced conversion engine ensures the fastest processing times."),
        ("Is my data secure?", "Absolutely! All files are encrypted and automatically deleted from our servers after conversion."),
        ("What file size limits do you have?", "Currently, we support files up to 200MB per conversion."),
        ("Can I use UniBox for commercial purposes?", "Yes! UniBox is completely free for both personal and commercial use."),
        ("Do I need to create an account?", "No account needed! You can start converting files immediately."),
    ]

    for question, answer in faqs:
        with st.expander(question):
            st.markdown(f"<div style='padding: 10px; color: #ccc;'>{answer}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)