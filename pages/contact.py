import streamlit as st

def render():
    """Render Contact page !!"""
    
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
    
    # Contact Methods
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h2 style='font-size: 28px; margin-bottom: 1.5rem; color: #ff4757;'>Send Us a Message</h2>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-bottom: 2rem;'>
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
            
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("✅ Message sent successfully! We'll get back to you soon.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
    
    with col2:
        # Contact Information - TURNED TO ST.HTML FOR THIS ONE ONLY !! <- prevent leak :)
        st.html("""
            <div class='tool-card'>
                <h2 style='font-size: 28px; margin-bottom: 1.5rem; color: #ff4757;'>Contact Information</h2>
                
                <div style='margin: 1.5rem 0;'>
                    <h4 style='color: #fff; font-size: 16px; margin-bottom: 0.5rem;'>
                        📧 Email
                    </h4>
                    <p style='color: #b0b0b0; font-size: 15px; margin-left: 2rem;'>
                        support@unibox.com<br/>
                        <span style='font-size: 13px; color: #888;'>Response time: 24-48 hours</span>
                    </p>
                </div>
                
                <div style='margin: 1.5rem 0;'>
                    <h4 style='color: #fff; font-size: 16px; margin-bottom: 0.5rem;'>
                        📱 Phone
                    </h4>
                    <p style='color: #b0b0b0; font-size: 15px; margin-left: 2rem;'>
                        +62 812-3456-7890<br/>
                        <span style='font-size: 13px; color: #888;'>Mon-Fri, 9AM - 5PM WIB</span>
                    </p>
                </div>
                
                <div style='margin: 1.5rem 0;'>
                    <h4 style='color: #fff; font-size: 16px; margin-bottom: 0.5rem;'>
                        📍 Location
                    </h4>
                    <p style='color: #b0b0b0; font-size: 15px; margin-left: 2rem;'>
                        Jakarta, Indonesia<br/>
                        <span style='font-size: 13px; color: #888;'>Remote-first company</span>
                    </p>
                </div>
                
                <div style='margin: 2rem 0 1rem 0; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <h4 style='color: #fff; font-size: 16px; margin-bottom: 1rem;'>
                        Follow Us
                    </h4>
                    <p style='color: #888; font-size: 14px;'>
                        🔗 LinkedIn | 🐦 Twitter | 💻 GitHub
                    </p>
                </div>
            </div>
        """)
    
    # FAQ Section
    st.markdown("""
        <div class='tool-card' style='margin-top: 2rem;'>
            <h2 style='font-size: 28px; margin-bottom: 1.5rem; color: #ff4757; text-align: center;'>
                Frequently Asked Questions
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("❓ How long does file conversion take?"):
        st.markdown("Most conversions complete within seconds. Larger files may take up to a few minutes.")
    
    with st.expander("❓ Is my data secure?"):
        st.markdown("Yes! All files are encrypted and automatically deleted after conversion.")
    
    with st.expander("❓ What file size limits do you have?"):
        st.markdown("Currently, we support files up to 200MB.")
    
    with st.expander("❓ Can I use UniBox for commercial purposes?"):
        st.markdown("Yes! UniBox is free for both personal and commercial use.")
    
    st.markdown("</div>", unsafe_allow_html=True)