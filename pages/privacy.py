import streamlit as st

def render():
    """Render Privacy Policy page !!"""
    
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
                <h1 class='hero-title'>Privacy Policy</h1>
                <p class='hero-subtitle'>
                    Your privacy matters to us. Learn how we collect, use, and protect your information.
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
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Introduction</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                At UniBox, we take your privacy seriously. This Privacy Policy explains how we collect, 
                use, disclose, and safeguard your information when you use our file conversion service. 
                By using UniBox, you agree to the collection and use of information in accordance with this policy.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Information We Collect - GANTI JADI st.html()
    st.html("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>1. Information We Collect</h2>
            
            <h3 style='font-size: 20px; margin: 1.5rem 0 0.75rem 0; color: #fff;'>
                1.1 Files You Upload
            </h3>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                When you use our conversion service, you upload files to our servers for processing. 
                These files are:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li>Temporarily stored during the conversion process</li>
                <li>Automatically deleted after conversion is complete</li>
                <li>Never accessed, viewed, or stored by our team</li>
                <li>Processed in a secure, encrypted environment</li>
            </ul>
            
            <h3 style='font-size: 20px; margin: 1.5rem 0 0.75rem 0; color: #fff;'>
                1.2 Usage Data
            </h3>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We automatically collect certain information when you visit UniBox, including:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li>Your IP address and browser type</li>
                <li>Pages visited and time spent on our site</li>
                <li>File formats converted (not file contents)</li>
                <li>Device information and operating system</li>
            </ul>
            
            <h3 style='font-size: 20px; margin: 1.5rem 0 0.75rem 0; color: #fff;'>
                1.3 Cookies and Tracking
            </h3>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We use cookies and similar tracking technologies to:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li>Remember your preferences and settings</li>
                <li>Analyze site traffic and usage patterns</li>
                <li>Improve user experience</li>
                <li>Prevent fraud and enhance security</li>
            </ul>
        </div>
    """)
    
    # How We Use Your Information
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>2. How We Use Your Information</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We use the information we collect to:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li><strong style='color: #fff;'>Provide Our Service:</strong> Process your file conversions quickly and accurately</li>
                <li><strong style='color: #fff;'>Improve Performance:</strong> Optimize our conversion algorithms and server infrastructure</li>
                <li><strong style='color: #fff;'>Ensure Security:</strong> Detect and prevent fraud, abuse, and security threats</li>
                <li><strong style='color: #fff;'>Analyze Usage:</strong> Understand how users interact with UniBox to improve features</li>
                <li><strong style='color: #fff;'>Communicate:</strong> Send important updates about our service (if you opt-in)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Data Security
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>3. Data Security</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We implement industry-standard security measures to protect your data:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li><strong style='color: #fff;'>Encryption:</strong> All data is encrypted in transit using SSL/TLS</li>
                <li><strong style='color: #fff;'>Secure Servers:</strong> Files are processed on secure, isolated servers</li>
                <li><strong style='color: #fff;'>Automatic Deletion:</strong> All uploaded files are deleted within 1 hour</li>
                <li><strong style='color: #fff;'>No Permanent Storage:</strong> We never store your converted files</li>
                <li><strong style='color: #fff;'>Access Controls:</strong> Strict employee access policies and monitoring</li>
            </ul>
            <div style='background: rgba(255, 71, 87, 0.1); border-left: 3px solid #ff4757; 
                        padding: 1rem 1.5rem; border-radius: 8px; margin-top: 1.5rem;'>
                <p style='color: #ff4757; font-size: 14px; margin: 0; font-weight: 600;'>
                    ⚠️ Important: While we use best-in-class security, no method of transmission over 
                    the Internet is 100% secure. Please do not upload highly sensitive or confidential 
                    documents that could cause harm if compromised.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Data Retention
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>4. Data Retention</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                <strong style='color: #fff;'>Uploaded Files:</strong> Automatically deleted immediately 
                after conversion or within 1 hour, whichever comes first.
            </p>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-top: 1rem;'>
                <strong style='color: #fff;'>Usage Statistics:</strong> Anonymized usage data 
                (file formats, conversion counts) is retained for analytical purposes only. 
                This data cannot be traced back to individual users.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Third-Party Services
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>5. Third-Party Services</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We may use third-party services for:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li><strong style='color: #fff;'>Analytics:</strong> Google Analytics to understand site usage</li>
                <li><strong style='color: #fff;'>Hosting:</strong> Cloud providers for server infrastructure</li>
                <li><strong style='color: #fff;'>CDN:</strong> Content delivery networks for faster performance</li>
            </ul>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-top: 1rem;'>
                These third parties have their own privacy policies. We do not share your uploaded 
                files with any third-party services.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Your Rights
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>6. Your Privacy Rights</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                You have the right to:
            </p>
            <ul style='color: #b0b0b0; font-size: 15px; line-height: 1.8; margin-left: 2rem;'>
                <li><strong style='color: #fff;'>Access:</strong> Request information about data we collect</li>
                <li><strong style='color: #fff;'>Opt-Out:</strong> Disable cookies in your browser settings</li>
                <li><strong style='color: #fff;'>Delete:</strong> Files are auto-deleted; no action needed</li>
                <li><strong style='color: #fff;'>Object:</strong> Object to processing of your data</li>
                <li><strong style='color: #fff;'>Withdraw Consent:</strong> Stop using the service at any time</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Children's Privacy
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>7. Children's Privacy</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                UniBox is not intended for children under 13 years of age. We do not knowingly 
                collect personal information from children. If you are a parent or guardian and 
                believe your child has provided us with information, please contact us immediately.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Changes to Privacy Policy
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>8. Changes to This Policy</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                We may update this Privacy Policy from time to time. We will notify you of any changes 
                by posting the new policy on this page and updating the "Last updated" date. 
                You are advised to review this policy periodically for any changes.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact
    st.markdown("""
        <div class='tool-card' style='background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
             border: 2px solid rgba(255, 71, 87, 0.3); text-align: center;'>
            <h2 style='font-size: 28px; margin-bottom: 1rem; color: #ff4757;'>Questions About Privacy?</h2>
            <p style='color: #b0b0b0; font-size: 15px; line-height: 1.8;'>
                If you have any questions about this Privacy Policy or our data practices, 
                please contact us through our Contact page.
            </p>
            <p style='color: #888; font-size: 14px; margin-top: 1rem;'>
                We typically respond within 48 hours.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)