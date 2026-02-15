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
    
    st.markdown("<div class='content-wrapper' style='max-width: 800px;'>", unsafe_allow_html=True)
    
    # 2. Contact Form Header
    st.markdown("""
        <div style='margin-bottom: 2rem;'>
            <h2 style='font-size: 24px; margin-bottom: 0.75rem; color: #fff; font-weight: 700;'>Send Us a Message</h2>
            <p style='color: #888; font-size: 15px; line-height: 1.6; margin-bottom: 2rem;'>
                Fill out the form below and we'll get back to you within 48 hours.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # 3. Custom CSS for premium form & expander styling
    st.markdown("""
        <style>
        /* Premium Form Input Styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
            font-size: 15px !important;
            padding: 14px 18px !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #ff4757 !important;
            box-shadow: 0 0 0 3px rgba(255, 71, 87, 0.1) !important;
            background: #2a2a2a !important;
        }
        
        /* Submit Button Enhancement */
        .stButton > button {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 16px 48px !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 71, 87, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(255, 71, 87, 0.5) !important;
        }

        /* Premium Expander Styling */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%) !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            font-size: 16px !important;
            padding: 1.25rem 1.5rem !important;
            transition: all 0.3s ease !important;
            margin-bottom: 12px !important;
        }
        
        .streamlit-expanderHeader:hover {
            border-color: rgba(255, 71, 87, 0.4) !important;
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 4. Contact Form (Hanya Satu Kali)
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
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields.")
    
    # 5. FAQ Section
    st.markdown("""
        <div style='margin-top: 4rem; margin-bottom: 2rem;'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #fff; text-align: center; font-weight: 800;'>
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
            st.write(answer)

    st.markdown("</div>", unsafe_allow_html=True)