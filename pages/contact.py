import streamlit as st

def render():
    """Render Contact page with clean professional design"""
    
    # Hero Section
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
    
    # Contact Form - Premium Design
    st.markdown("""
        <div class='tool-card' style='margin-bottom: 3rem; padding: 3rem 2.5rem;'>
            <h2 style='font-size: 32px; margin-bottom: 1rem; color: #ff4757; text-align: center; font-weight: 800;'>Send Us a Message</h2>
            <p style='color: #888; font-size: 16px; line-height: 1.8; margin-bottom: 2.5rem; text-align: center; max-width: 600px; margin-left: auto; margin-right: auto;'>
                Fill out the form below and we'll get back to you within 48 hours. We're here to help!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Custom CSS for premium form styling
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
        
        .stTextInput > div > div > input::placeholder,
        .stTextArea > div > div > textarea::placeholder {
            color: #666 !important;
        }
        
        /* Form Labels */
        .stTextInput > label,
        .stTextArea > label,
        .stSelectbox > label {
            color: #fff !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            margin-bottom: 8px !important;
            letter-spacing: 0.3px !important;
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
        
        /* Select Dropdown */
        .stSelectbox [data-baseweb="select"] {
            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%) !important;
        }
        
        .stSelectbox [data-baseweb="select"]:hover {
            border-color: rgba(255, 71, 87, 0.5) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Contact Form
    with st.form("contact_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "Your Name *",
                placeholder="John Doe",
                help="Enter your full name"
            )
        
        with col2:
            email = st.text_input(
                "Email Address *",
                placeholder="john@example.com",
                help="We'll never share your email"
            )
        
        subject = st.selectbox(
            "Subject *",
            [
                "General Inquiry",
                "Technical Support",
                "Feature Request",
                "Bug Report",
                "Business/Partnership",
                "Other"
            ]
        )
        
        message = st.text_area(
            "Your Message *",
            placeholder="Tell us how we can help you...",
            height=180,
            help="Please provide as much detail as possible"
        )
        
        # Centered submit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully. We'll get back to you within 48 hours.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields.")
    
    # FAQ Section - Direct after form
    st.markdown("""
        <div class='tool-card' style='margin-top: 3rem; padding: 3rem 2.5rem;'>
            <h2 style='font-size: 32px; margin-bottom: 2rem; color: #ff4757; text-align: center; font-weight: 800;'>
                Frequently Asked Questions
            </h2>
            <p style='color: #888; font-size: 15px; text-align: center; margin-bottom: 2rem;'>
                Quick answers to common questions about UniBox
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Premium Expander Styling
    st.markdown("""
        <style>
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
            background: linear-gradient(135deg, #2d2d2d 0%, #282828 100%) !important;
            border-color: rgba(255, 71, 87, 0.4) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
        }
        
        .streamlit-expanderContent {
            background: #242424 !important;
            color: #b0b0b0 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-top: none !important;
            border-radius: 0 0 12px 12px !important;
            padding: 1.5rem 1.75rem !important;
            font-size: 15px !important;
            line-height: 1.8 !important;
            margin-top: -12px !important;
            margin-bottom: 12px !important;
        }
        
        /* Arrow icon color */
        .streamlit-expanderHeader svg {
            stroke: #ff4757 !important;
            transition: transform 0.3s ease !important;
        }
        
        /* Rotate arrow when expanded */
        details[open] .streamlit-expanderHeader svg {
            transform: rotate(180deg) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.expander("How long does file conversion take?"):
        st.markdown("Most conversions complete within seconds. Larger files may take up to a few minutes depending on file size and complexity. Our advanced conversion engine ensures the fastest processing times without compromising quality.")
    
    with st.expander("Is my data secure?"):
        st.markdown("Absolutely! All files are encrypted during transmission using industry-standard SSL/TLS protocols and automatically deleted from our servers after conversion. We never access, view, or store your files. Your privacy and security are our top priorities.")
    
    with st.expander("What file size limits do you have?"):
        st.markdown("Currently, we support files up to 200MB per conversion. For larger files or batch processing needs, please contact our support team for assistance. We're working on increasing these limits based on user feedback.")
    
    with st.expander("Can I use UniBox for commercial purposes?"):
        st.markdown("Yes! UniBox is completely free for both personal and commercial use. There are no restrictions on how you use our service. Whether you're a student, professional, or business, you can convert files without any limitations.")
    
    with st.expander("Do I need to create an account?"):
        st.markdown("No account needed! You can start converting files immediately without any registration or sign-up process. Simply upload your file, select the output format, and download the converted file. It's that simple.")
    
    with st.expander("Which formats do you support?"):
        st.markdown("We support a wide range of formats including documents (PDF, DOCX, XLSX, CSV), media files (images, videos, audio), and developer formats (JSON, XML, YAML). We're constantly adding new formats based on user requests.")
    
    st.markdown("</div>", unsafe_allow_html=True)