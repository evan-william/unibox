import streamlit as st

def render():
    """Render About Us page with professional design"""
    
    # Hero Section
    st.markdown("""
        <div class='hero-section'>
            <div class='hero-content'>
                <h1 class='hero-title'>About UniBox</h1>
                <p class='hero-subtitle'>
                    Your trusted partner for seamless file conversion. 
                    We're on a mission to make file conversion simple, fast, and accessible for everyone.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)
    
    # Our Story
    st.markdown("""
        <div class='tool-card'>
            <h2 style='font-size: 32px; margin-bottom: 1rem;'>Our Story</h2>
            <p style='font-size: 16px; line-height: 1.8; color: #b0b0b0;'>
                UniBox was born from a simple frustration: converting files shouldn't be complicated. 
                We've all been there—needing to convert a document for work, struggling with clunky software, 
                or paying for features we don't need. That's why we created UniBox.
            </p>
            <p style='font-size: 16px; line-height: 1.8; color: #b0b0b0; margin-top: 1rem;'>
                Since our launch, we've helped thousands of users convert millions of files across 
                dozens of formats. Whether you're a student preparing assignments, a professional 
                creating presentations, or a developer working with data, UniBox is here to help.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Our Values - USE ST.HTML TO PREVENT CSS LEAK
    st.markdown("""
        <div style='margin: 3rem 0;'>
            <h2 style='text-align: center; font-size: 32px; font-weight: 800; margin-bottom: 2rem;'>Our Values</h2>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.html("""
            <div class='tool-card' style='text-align: center; height: 100%;'>
                <div style='width: 80px; height: 80px; margin: 0 auto 1.5rem auto; 
                            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
                            border-radius: 16px; display: flex; align-items: center; 
                            justify-content: center; border: 1px solid rgba(255, 255, 255, 0.1);'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12 6 12 12 16 14"/>
                    </svg>
                </div>
                <h3 style='font-size: 20px; margin-bottom: 0.5rem;'>Speed & Efficiency</h3>
                <p style='color: #888; font-size: 14px; line-height: 1.6;'>
                    We believe your time is valuable. That's why we've optimized 
                    our conversion engine to deliver lightning-fast results without 
                    compromising quality.
                </p>
            </div>
        """)
    
    with col2:
        st.html("""
            <div class='tool-card' style='text-align: center; height: 100%;'>
                <div style='width: 80px; height: 80px; margin: 0 auto 1.5rem auto; 
                            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
                            border-radius: 16px; display: flex; align-items: center; 
                            justify-content: center; border: 1px solid rgba(255, 255, 255, 0.1);'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    </svg>
                </div>
                <h3 style='font-size: 20px; margin-bottom: 0.5rem;'>Privacy First</h3>
                <p style='color: #888; font-size: 14px; line-height: 1.6;'>
                    Your files are yours alone. We process everything securely 
                    and never store your documents. What happens in UniBox, 
                    stays in UniBox.
                </p>
            </div>
        """)
    
    with col3:
        st.html("""
            <div class='tool-card' style='text-align: center; height: 100%;'>
                <div style='width: 80px; height: 80px; margin: 0 auto 1.5rem auto; 
                            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
                            border-radius: 16px; display: flex; align-items: center; 
                            justify-content: center; border: 1px solid rgba(255, 255, 255, 0.1);'>
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                    </svg>
                </div>
                <h3 style='font-size: 20px; margin-bottom: 0.5rem;'>Quality Output</h3>
                <p style='color: #888; font-size: 14px; line-height: 1.6;'>
                    We use industry-leading conversion algorithms to ensure 
                    your files maintain their formatting, quality, and integrity 
                    through every transformation.
                </p>
            </div>
        """)
    
    # What Sets Us Apart - USE ST.HTML TO PREVENT CSS LEAK
    st.html("""
        <div class='tool-card' style='margin-top: 3rem;'>
            <h2 style='font-size: 32px; margin-bottom: 1.5rem;'>What Sets Us Apart</h2>
            
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: #ff4757; font-size: 18px; margin-bottom: 0.5rem;'>
                    ✓ No Installation Required
                </h4>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.7; padding-left: 1.5rem;'>
                    Access UniBox from any device with a web browser. No downloads, 
                    no installations, no hassle.
                </p>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: #ff4757; font-size: 18px; margin-bottom: 0.5rem;'>
                    ✓ Free Forever
                </h4>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.7; padding-left: 1.5rem;'>
                    We believe file conversion should be accessible to everyone. 
                    No hidden fees, no credit card required, no limits.
                </p>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: #ff4757; font-size: 18px; margin-bottom: 0.5rem;'>
                    ✓ Multiple Formats
                </h4>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.7; padding-left: 1.5rem;'>
                    From documents to media files, we support all the formats you need. 
                    And we're constantly adding more based on user feedback.
                </p>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: #ff4757; font-size: 18px; margin-bottom: 0.5rem;'>
                    ✓ Built by Developers, for Everyone
                </h4>
                <p style='color: #b0b0b0; font-size: 15px; line-height: 1.7; padding-left: 1.5rem;'>
                    We understand the technical challenges because we face them too. 
                    That's why UniBox is both powerful for pros and simple for beginners.
                </p>
            </div>
        </div>
    """)
        
    # Team Section
    st.markdown("""
        <div style='text-align: center; margin: 4rem 0 2rem 0;'>
            <h2 style='font-size: 32px; font-weight: 800; margin-bottom: 1rem;'>Meet the Creator</h2>
            <p style='color: #888; font-size: 16px; max-width: 600px; margin: 0 auto;'>
                UniBox is built and maintained by Evan William, a passionate developer 
                dedicated to creating tools that make life easier.
            </p>
        </div>
        
        <div style='max-width: 400px; margin: 0 auto;'>
            <div class='tool-card' style='text-align: center;'>
                <div style='width: 120px; height: 120px; border-radius: 50%; 
                            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%); 
                            margin: 0 auto 1.5rem auto; display: flex; align-items: center; 
                            justify-content: center; font-size: 48px; font-weight: 800; 
                            color: white;'>
                    EW
                </div>
                <h3 style='font-size: 24px; margin-bottom: 0.5rem;'>Evan William</h3>
                <p style='color: #ff4757; font-size: 14px; margin-bottom: 1rem; font-weight: 600;'>
                    Founder & Lead Developer
                </p>
                <p style='color: #888; font-size: 14px; line-height: 1.6;'>
                    Passionate about creating intuitive tools that solve real problems. 
                    When not coding, you'll find me exploring new technologies and 
                    drinking way too much coffee.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Our Commitment
    st.markdown("""
        <div class='tool-card' style='margin-top: 3rem; text-align: center; 
             background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%); 
             border: 2px solid rgba(255, 71, 87, 0.3);'>
            <h2 style='font-size: 28px; margin-bottom: 1rem;'>Our Commitment to You</h2>
            <p style='color: #b0b0b0; font-size: 16px; line-height: 1.8; max-width: 700px; margin: 0 auto;'>
                We're committed to keeping UniBox free, fast, and private. 
                As we grow, we promise to never compromise on these core values. 
                Your trust is everything to us, and we work every day to earn it.
            </p>
            <p style='color: #ff4757; font-size: 18px; margin-top: 1.5rem; font-weight: 600;'>
                Thank you for choosing UniBox! 🚀
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)