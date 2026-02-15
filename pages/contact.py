import streamlit as st

def render():
    """Render Contact page with professional design"""
    
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
    
    st.markdown("<div class='content-wrapper' style='max-width: 1200px;'>", unsafe_allow_html=True)
    
    # Contact Methods with REDUCED gap
    col1, col2 = st.columns([1.1, 1], gap="medium")
    
    with col1:
        st.markdown("""
            <div class='tool-card' style='margin-bottom: 0;'>
                <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Send Us a Message</h2>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-bottom: 2rem;'>
                    Fill out the form and we'll get back to you within 48 hours.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Contact Form with better styling
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
        st.html("""
            <style>
                .contact-info-wrapper {
                    background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
                    border-radius: 12px;
                    padding: 2rem 1.5rem;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                    height: 100%;
                }
                .contact-info-title {
                    font-size: 28px;
                    margin-bottom: 2rem;
                    color: #ff4757;
                    font-weight: 700;
                }
                .info-section {
                    margin-bottom: 2rem;
                }
                .info-header {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    margin-bottom: 0.75rem;
                }
                .info-icon-box {
                    width: 40px;
                    height: 40px;
                    min-width: 40px;
                    background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }
                .info-label {
                    color: #fff;
                    font-size: 18px;
                    margin: 0;
                    font-weight: 600;
                }
                .info-details {
                    padding-left: 52px;
                }
                .info-text {
                    color: #b0b0b0;
                    font-size: 15px;
                    margin: 0;
                    margin-bottom: 4px;
                }
                .info-subtext {
                    font-size: 13px;
                    color: #666;
                    margin: 0;
                }
                .social-divider {
                    padding-top: 1.5rem;
                    border-top: 1px solid rgba(255,255,255,0.1);
                    margin-top: 1rem;
                }
                .social-buttons {
                    display: flex;
                    gap: 12px;
                    flex-wrap: wrap;
                }
                .social-link {
                    text-decoration: none;
                }
                .social-icon-btn {
                    width: 44px;
                    height: 44px;
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }
                .social-icon-btn:hover {
                    transform: translateY(-2px);
                }
                .linkedin {
                    background: linear-gradient(135deg, #0077B5 0%, #005582 100%);
                }
                .linkedin:hover {
                    box-shadow: 0 8px 20px rgba(0, 119, 181, 0.4);
                }
                .twitter {
                    background: linear-gradient(135deg, #1DA1F2 0%, #0d8bd9 100%);
                }
                .twitter:hover {
                    box-shadow: 0 8px 20px rgba(29, 161, 242, 0.4);
                }
                .github {
                    background: linear-gradient(135deg, #333 0%, #24292e 100%);
                }
                .github:hover {
                    box-shadow: 0 8px 20px rgba(36, 41, 46, 0.4);
                }
            </style>
            
            <div class='contact-info-wrapper'>
                <h2 class='contact-info-title'>Contact Information</h2>
                
                <!-- Email Section -->
                <div class='info-section'>
                    <div class='info-header'>
                        <div class='info-icon-box'>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="2" y="4" width="20" height="16" rx="2" stroke="#ff4757" stroke-width="2"/>
                                <path d="M22 7L13 12.7C12.4 13.1 11.6 13.1 11 12.7L2 7" stroke="#ff4757" stroke-width="2" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <h4 class='info-label'>Email</h4>
                    </div>
                    <div class='info-details'>
                        <p class='info-text'>support@unibox.com</p>
                        <p class='info-subtext'>Response time: 24-48 hours</p>
                    </div>
                </div>
                
                <!-- Phone Section -->
                <div class='info-section'>
                    <div class='info-header'>
                        <div class='info-icon-box'>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M22 16.9V19.9C22 21 21 22 19.9 22C11.4 21.2 4.8 14.6 4 6.1C4 5 5 4 6.1 4H9.1C9.6 4 10.1 4.4 10.2 5C10.3 5.8 10.4 6.6 10.7 7.4C10.9 7.9 10.7 8.3 10.4 8.6L8.8 9.8C10.2 12.5 12.5 14.8 15.2 16.2L16.4 14.6C16.7 14.3 17.2 14.2 17.6 14.3C18.4 14.6 19.2 14.8 20 14.9C20.6 14.9 21 15.4 21 15.9V16.9Z" stroke="#ff4757" stroke-width="2" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <h4 class='info-label'>Phone</h4>
                    </div>
                    <div class='info-details'>
                        <p class='info-text'>+62 812-3456-7890</p>
                        <p class='info-subtext'>Mon-Fri, 9AM - 5PM WIB</p>
                    </div>
                </div>
                
                <!-- Location Section -->
                <div class='info-section'>
                    <div class='info-header'>
                        <div class='info-icon-box'>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M21 10C21 17 12 23 12 23C12 23 3 17 3 10C3 5 7 1 12 1C17 1 21 5 21 10Z" stroke="#ff4757" stroke-width="2"/>
                                <circle cx="12" cy="10" r="3" stroke="#ff4757" stroke-width="2"/>
                            </svg>
                        </div>
                        <h4 class='info-label'>Location</h4>
                    </div>
                    <div class='info-details'>
                        <p class='info-text'>Jakarta, Indonesia</p>
                        <p class='info-subtext'>Remote-first company</p>
                    </div>
                </div>
                
                <!-- Social Media -->
                <div class='social-divider'>
                    <h4 class='info-label' style='margin-bottom: 1rem;'>Follow Us</h4>
                    <div class='social-buttons'>
                        <a href='#' class='social-link'>
                            <div class='social-icon-btn linkedin'>
                                <svg width="22" height="22" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                                </svg>
                            </div>
                        </a>
                        <a href='#' class='social-link'>
                            <div class='social-icon-btn twitter'>
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                                </svg>
                            </div>
                        </a>
                        <a href='#' class='social-link'>
                            <div class='social-icon-btn github'>
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
                                </svg>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        """)
    
    # FAQ Section with better styling
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