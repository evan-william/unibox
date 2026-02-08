import streamlit as st

def apply_custom_styles():
    """Apply modern CloudConvert-inspired dark theme with professional styling"""
    
    st.markdown("""
        <style>
        /* ===== IMPORT FONTS ===== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* ===== GLOBAL RESET ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        /* ===== REMOVE STREAMLIT BRANDING ===== */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* ===== MAIN LAYOUT ===== */
        .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section {
            background: #1a1a1a !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* ===== TOP NAVIGATION ===== */
        .top-nav {
            background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%);
            padding: 1.25rem 4rem;
            margin: 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }
        
        .nav-wrapper {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        
        .nav-brand span {
            font-size: 26px;
            font-weight: 800;
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }
        
        .nav-links {
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        
        .nav-link {
            color: #b0b0b0;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.2s;
            cursor: pointer;
        }
        
        .nav-link:hover {
            color: #ffffff;
        }
        
        .nav-actions {
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        
        .nav-button {
            padding: 8px 20px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }
        
        .nav-button.secondary {
            background: transparent;
            color: #b0b0b0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .nav-button.secondary:hover {
            background: rgba(255, 255, 255, 0.05);
            color: #ffffff;
        }
        
        .nav-button.primary {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%);
            color: #ffffff;
            border: none;
        }
        
        .nav-button.primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(255, 71, 87, 0.4);
        }
        
        /* ===== HERO SECTION ===== */
        .hero-section {
            background: linear-gradient(135deg, #2d2d2d 0%, #232323 100%);
            padding: 5rem 4rem;
            text-align: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, rgba(255, 71, 87, 0.05) 0%, transparent 70%);
            pointer-events: none;
        }
                
        /* ADD THESE - Force center ALL headings and paragraphs in hero */
        .hero-section h1,
        .hero-section h2,
        .hero-section h3 {
            text-align: center !important;
        }
   
        /* ADD THIS - Force center ALL paragraphs in hero */
        .hero-section p {
            text-align: center !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        
        /* FIX STREAMLIT MARKDOWN CONTAINERS IN HERO */
        .hero-section [data-testid="stMarkdownContainer"] {
            max-width: 900px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            text-align: center !important;
        }

        .hero-section [data-testid="stMarkdownContainer"] * {
            text-align: center !important;
        }
        
        .hero-content {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }
        
        .hero-title {
            font-size: 52px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            letter-spacing: -1px;
        }
        
        .hero-subtitle {
            font-size: 18px;
            color: #b0b0b0;
            line-height: 1.7;
            margin-bottom: 3rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        
        .converter-selector {
            background: #2a2a2a;
            border-radius: 12px;
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }
        
        .selector-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2rem;
        }
        
        .selector-label {
            font-size: 13px;
            font-weight: 600;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.75rem;
        }
        
        .arrow-icon {
            font-size: 24px;
            color: #666;
            margin-top: 28px;
        }
        
        /* ===== CONTENT WRAPPER ===== */
        .content-wrapper {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 4rem 4rem 4rem;
        }
        
        /* Fix for page description text */
        .content-wrapper [data-testid="stMarkdownContainer"] p {
            text-align: center !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        
        /* ===== CATEGORY TABS ===== */
        .category-tabs {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin: 3rem 0;
            padding: 0 2rem;
        }
        
        .category-tab {
            background: #2a2a2a;
            color: #888;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 14px 32px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .category-tab:hover {
            background: #2f2f2f;
            color: #fff;
            border-color: rgba(255, 255, 255, 0.2);
        }
        
        .category-tab.active {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%);
            color: #ffffff;
            border-color: transparent;
            box-shadow: 0 4px 12px rgba(255, 71, 87, 0.3);
        }
        
        /* ===== SIDEBAR ===== */
        [data-testid="stSidebar"] {
            background: #1f1f1f !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        }
        
        [data-testid="stSidebar"] > div:first-child {
            padding: 2rem 1.5rem !important;
        }
        
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        .sidebar-header {
            margin-bottom: 2rem;
        }
        
        .logo-container {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        
        .logo-text h1 {
            font-size: 24px !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 !important;
            line-height: 1.2 !important;
        }
        
        .logo-text p {
            font-size: 12px !important;
            color: #666 !important;
            margin: 0 !important;
            letter-spacing: 0.5px;
            font-weight: 500;
        }
        
        .sidebar-divider {
            height: 1px;
            background: rgba(255, 255, 255, 0.08);
            margin: 1.5rem 0;
        }
        
        .sidebar-title {
            font-size: 11px !important;
            font-weight: 700 !important;
            color: #888 !important;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 1rem !important;
        }
        
        [data-testid="stSidebar"] .stButton > button {
            background: transparent !important;
            color: #888 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 8px !important;
            padding: 12px 16px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            text-align: left !important;
            transition: all 0.2s ease !important;
            margin-bottom: 8px !important;
            width: 100% !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: #2a2a2a !important;
            color: #fff !important;
            border-color: rgba(255, 255, 255, 0.15) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: #fff !important;
            border-color: transparent !important;
        }
        
        .sidebar-footer {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .info-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 14px 0;
            color: #666;
            font-size: 13px;
            font-weight: 500;
        }
        
        /* ===== SELECT BOXES ===== */
        .main [data-testid="stSelectbox"] label {
            font-size: 13px !important;
            font-weight: 600 !important;
            color: #888 !important;
            margin-bottom: 8px !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background: #2a2a2a !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 8px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #ffffff !important;
            font-weight: 500 !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"]:hover {
            border-color: rgba(255, 255, 255, 0.2) !important;
        }
        
        /* ===== FILE UPLOADER ===== */
        [data-testid="stFileUploader"] {
            background: #2a2a2a !important;
            border: 2px dashed rgba(255, 255, 255, 0.15) !important;
            border-radius: 12px !important;
            padding: 3.5rem 2rem !important;
            text-align: center;
            transition: all 0.3s;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #ff4757 !important;
            background: #2d2d2d !important;
        }
        
        [data-testid="stFileUploader"] section {
            border: none !important;
            background: transparent !important;
        }
        
        [data-testid="stFileUploader"] label {
            color: #b0b0b0 !important;
            font-size: 15px !important;
            font-weight: 500 !important;
        }
        
        [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 32px !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            margin-top: 1rem !important;
        }
        
        [data-testid="stFileUploader"] button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255, 71, 87, 0.4);
        }
        
        /* ===== BUTTONS ===== */
        .main .stButton > button {
            background: linear-gradient(135deg, #ff4757 0%, #ff6348 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            transition: all 0.2s !important;
        }
        
        .main .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255, 71, 87, 0.4) !important;
        }
        
        .main .stDownloadButton > button {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        .main .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(46, 204, 113, 0.4) !important;
        }
        
        /* ===== TOOL CARD ===== */
        .tool-card {
            background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
            border-radius: 12px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }
        
        .tool-card h3 {
            font-size: 28px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 1rem !important;
            letter-spacing: -0.5px;
        }
        
        .tool-card p {
            font-size: 16px !important;
            color: #b0b0b0 !important;
            line-height: 1.7 !important;
        }
        
        /* ===== INFO BOX ===== */
        .info-box {
            background: #242424;
            border-left: 3px solid #ff4757;
            border-radius: 8px;
            padding: 1.75rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }
        
        .info-box h4 {
            font-size: 13px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 1.25rem !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
            color: #b0b0b0 !important;
            margin: 10px 0;
            font-size: 14px !important;
            padding-left: 24px;
            position: relative;
            font-weight: 500;
        }
        
        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #2ecc71;
            font-weight: bold;
            font-size: 16px;
        }
        
        /* ===== SUCCESS MESSAGE ===== */
        .success-msg {
            background: rgba(46, 204, 113, 0.1);
            color: #2ecc71;
            padding: 1rem 1.5rem;
            border-left: 3px solid #2ecc71;
            border-radius: 8px;
            font-weight: 600;
            margin: 1.5rem 0;
            font-size: 15px;
        }
        
        /* ===== FEATURE GRID ===== */
        .features-section {
            margin: 5rem 0 3rem 0;
            padding: 4rem 0;
            background: linear-gradient(135deg, #252525 0%, #1f1f1f 100%);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .features-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .features-header h2 {
            font-size: 36px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 1rem;
            letter-spacing: -0.5px;
        }
        
        .features-header p {
            font-size: 17px;
            color: #888;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }
        
        .feature-card {
            background: #2a2a2a;
            border-radius: 12px;
            padding: 2.5rem;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #ff4757, #ff6348);
            transform: scaleX(0);
            transition: transform 0.3s;
        }
        
        .feature-card:hover {
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        }
        
        .feature-card:hover::before {
            transform: scaleX(1);
        }
        
        .feature-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 1.5rem auto;
            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .feature-card h4 {
            font-size: 20px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 0.75rem !important;
            letter-spacing: -0.3px;
        }
        
        .feature-card p {
            font-size: 15px !important;
            color: #888 !important;
            line-height: 1.6 !important;
        }
        
        /* ===== WIP CONTAINER ===== */
        .wip-container {
            background: linear-gradient(135deg, #2a2a2a 0%, #242424 100%);
            border-radius: 16px;
            padding: 5rem 3rem;
            text-align: center;
            margin: 3rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .wip-icon {
            width: 100px;
            height: 100px;
            margin: 0 auto 2rem auto;
            background: linear-gradient(135deg, #2d2d2d 0%, #262626 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            border: 2px solid rgba(255, 255, 255, 0.1);
        }
        
        .wip-container h2 {
            font-size: 38px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 0.75rem !important;
            letter-spacing: -0.5px;
        }
        
        .wip-container h3 {
            font-size: 22px !important;
            font-weight: 600 !important;
            color: #666 !important;
            margin-bottom: 1.5rem !important;
        }
        
        .wip-container p {
            font-size: 17px !important;
            color: #999 !important;
            max-width: 500px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: transparent;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            color: #666;
            padding: 14px 28px;
            font-weight: 600;
            font-size: 15px;
            border-radius: 8px 8px 0 0;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(255, 255, 255, 0.03);
            color: #999;
        }
        
        .stTabs [aria-selected="true"] {
            background: transparent;
            color: #fff;
            border-bottom: 3px solid #ff4757;
        }
        
        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            background: #2a2a2a !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            font-size: 15px !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: #2d2d2d !important;
            border-color: rgba(255, 255, 255, 0.2) !important;
        }
        
        .streamlit-expanderContent {
            background: #242424 !important;
            color: #b0b0b0 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-top: none !important;
            border-radius: 0 0 8px 8px !important;
            padding: 1.5rem !important;
        }
        
        /* ===== MESSAGES ===== */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: 8px !important;
            padding: 1rem 1.5rem !important;
            background: #2a2a2a !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        /* ===== FOOTER ===== */
        .main-footer {
            margin-top: 5rem;
            padding: 3rem 4rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            background: linear-gradient(135deg, #1f1f1f 0%, #1a1a1a 100%);
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1400px;
            margin: 0 auto;
            color: #666;
            font-size: 14px;
        }
        
        .footer-right {
            display: flex;
            gap: 2.5rem;
        }
        
        .footer-right a {
            color: #666;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        
        .footer-right a:hover {
            color: #fff;
        }
        
        /* ===== STATS SECTION ===== */
        .stats-section {
            text-align: center;
            padding: 2rem 0;
            margin: 3rem 0;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .stats-text {
            font-size: 15px;
            color: #666;
        }
        
        .stats-number {
            color: #ff4757;
            font-weight: 700;
        }
        
        /* ===== TEXT COLORS ===== */
        .main * {
            color: #b0b0b0 !important;
        }
        
        .main h1, .main h2, .main h3 {
            color: #ffffff !important;
        }
        
        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .top-nav {
                padding: 1rem 1.5rem;
            }
            
            .hero-section {
                padding: 3rem 1.5rem;
            }
            
            .hero-title {
                font-size: 36px !important;
            }
            
            .content-wrapper {
                padding: 2rem 1.5rem !important;
            }
            
            .footer-content {
                flex-direction: column;
                gap: 1.5rem;
                text-align: center;
            }
            
            .selector-row {
                flex-direction: column;
                gap: 1rem;
            }
            
            .arrow-icon {
                transform: rotate(90deg);
                margin: 0;
            }
        }
        </style>
    """, unsafe_allow_html=True)