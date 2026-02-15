import streamlit as st

def render():
    """Render Contact page with simple clean design"""
    
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
    
    st.markdown("<div class='content-wrapper' style='max-width: 900px;'>", unsafe_allow_html=True)
    
    # Contact Form - Centered and Clean
    st.markdown("""
        <div class='tool-card' style='margin-bottom: 2rem;'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757; text-align: center;'>Send Us a Message</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-bottom: 2rem; text-align: center;'>
                Fill out the form and we'll get back to you within 48 hours.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact Form
    with st.form("contact_form"):
        name = st.text_input(
            "Your Name *",
            placeholder="John Doe",
            help="Enter your full name"
        )
        
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
            "Message *",
            placeholder="Tell us how we can help you...",
            height=200,
            help="Please provide as much detail as possible"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully! We'll get back to you soon.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields.")
    
    # Contact Info Cards - Simple 3 Column Layout
    st.markdown("<div style='margin: 3rem 0 2rem 0;'><h3 style='text-align: center; font-size: 24px; font-weight: 700; margin-bottom: 2rem;'>Other Ways to Reach Us</h3></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='tool-card' style='text-align: center; padding: 2rem 1.5rem;'>
                <div style='font-size: 36px; margin-bottom: 1rem;'>📧</div>
                <h4 style='font-size: 18px; margin-bottom: 0.5rem; color: #fff;'>Email</h4>
                <p style='color: #b0b0b0; font-size: 14px; margin: 0;'>support@unibox.com</p>
                <p style='color: #666; font-size: 12px; margin-top: 0.5rem;'>24-48 hours response</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='tool-card' style='text-align: center; padding: 2rem 1.5rem;'>
                <div style='font-size: 36px; margin-bottom: 1rem;'>📱</div>
                <h4 style='font-size: 18px; margin-bottom: 0.5rem; color: #fff;'>Phone</h4>
                <p style='color: #b0b0b0; font-size: 14px; margin: 0;'>+62 812-3456-7890</p>
                <p style='color: #666; font-size: 12px; margin-top: 0.5rem;'>Mon-Fri, 9AM-5PM WIB</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='tool-card' style='text-align: center; padding: 2rem 1.5rem;'>
                <div style='font-size: 36px; margin-bottom: 1rem;'>📍</div>
                <h4 style='font-size: 18px; margin-bottom: 0.5rem; color: #fff;'>Location</h4>
                <p style='color: #b0b0b0; font-size: 14px; margin: 0;'>Jakarta, Indonesia</p>
                <p style='color: #666; font-size: 12px; margin-top: 0.5rem;'>Remote-first company</p>
            </div>
        """, unsafe_allow_html=True)
    
    # FAQ Section
    st.markdown("""
        <div class='tool-card' style='margin-top: 3rem;'>
            <h2 style='font-size: 28px; margin-bottom: 1.5rem; color: #ff4757; text-align: center;'>
                Frequently Asked Questions
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Custom CSS for better expander styling
    st.markdown("""
        <style>
        /* Improved Expander Styling */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%) !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            font-size: 15px !important;
            padding: 1rem 1.25rem !important;
            transition: all 0.2s ease !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #2d2d2d 0%, #282828 100%) !important;
            border-color: rgba(255, 71, 87, 0.3) !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
        }
        
        .streamlit-expanderContent {
            background: #242424 !important;
            color: #b0b0b0 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-top: none !important;
            border-radius: 0 0 10px 10px !important;
            padding: 1.25rem 1.5rem !important;
            font-size: 14px !important;
            line-height: 1.7 !important;
        }
        
        /* Custom icon for expander */
        .streamlit-expanderHeader svg {
            stroke: #ff4757 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.expander("How long does file conversion take?"):
        st.markdown("Most conversions complete within seconds. Larger files may take up to a few minutes depending on file size and complexity.")
    
    with st.expander("Is my data secure?"):
        st.markdown("Yes! All files are encrypted during transmission and automatically deleted from our servers after conversion. We never access or store your files.")
    
    with st.expander("What file size limits do you have?"):
        st.markdown("Currently, we support files up to 200MB per conversion. For larger files, please contact our support team for assistance.")
    
    with st.expander("Can I use UniBox for commercial purposes?"):
        st.markdown("Yes! UniBox is free for both personal and commercial use. There are no restrictions on how you use our service.")
    
    with st.expander("Do I need to create an account?"):
        st.markdown("No account needed! You can start converting files immediately without any registration or sign-up process.")
    
    st.markdown("</div>", unsafe_allow_html=True)