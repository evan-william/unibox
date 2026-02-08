import streamlit as st

def apply_custom_styles():
    """Apply professional CloudConvert-inspired dark theme with modern UI"""
    
    st.markdown("""
        <style>
        /* ===== IMPORT FONTS ===== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        /* ===== GLOBAL RESET ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* ===== REMOVE STREAMLIT BRANDING ===== */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* ===== TOP NAVIGATION ===== */
        .top-nav {
            background: linear-gradient(135deg, #1a1a1a 0%, #242424 100%);
            padding: 1rem 3rem;
            margin: 0;
            border-bottom: 1px solid #333;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .nav-brand {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .nav-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .nav-brand-text {
            font-size: 24px;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.5px;
        }
        
        .nav-links {
            display: flex;
            gap: 2.5rem;
            align-items: center;
        }
        
        .nav-link {
            color: #aaa;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s ease;
            cursor: pointer;
            position: relative;
        }
        
        .nav-link:hover {
            color: #fff;
        }
        
        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 0;
            width: 0;
            height: 2px;
            background: #c9302c;
            transition: width 0.3s ease;
        }
        
        .nav-link:hover::after {
            width: 100%;
        }
        
        .nav-badge {
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%);
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
            margin-left: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Content container */
        .content-wrapper {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 4rem 3rem 4rem;
        }
        
        /* ===== HERO SECTION ===== */
        .hero-section {
            background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
            padding: 5rem 3rem;
            margin: 0 -4rem 3rem -4rem;
            text-align: center;
            border-bottom: 1px solid #333;
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(201, 48, 44, 0.1) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .hero-section::after {
            content: '';
            position: absolute;
            bottom: -50%;
            left: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(201, 48, 44, 0.1) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
        }
        
        .hero-section h1 {
            font-size: 52px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 1.2rem !important;
            letter-spacing: -1.5px;
            line-height: 1.2 !important;
        }
        
        .hero-section p {
            font-size: 19px !important;
            color: #bbb !important;
            max-width: 750px;
            margin: 0 auto 3rem auto;
            line-height: 1.7;
            font-weight: 400;
        }
        
        .stats-row {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
            flex-wrap: wrap;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 36px;
            font-weight: 800;
            background: linear-gradient(135deg, #c9302c 0%, #ff4444 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: block;
            letter-spacing: -1px;
        }
        
        .stat-label {
            font-size: 13px;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 8px;
            font-weight: 600;
        }
        
        /* Navigation tab buttons */
        .main > div:first-child .stButton > button {
            background: #3d3d3d !important;
            color: #aaa !important;
            border: 1px solid #4d4d4d !important;
            border-radius: 8px !important;
            padding: 14px 28px !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }
        
        .main > div:first-child .stButton > button:hover {
            background: #404040 !important;
            color: #fff !important;
            border-color: #666 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
        }
        
        .main > div:first-child .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%) !important;
            color: #fff !important;
            border-color: #c9302c !important;
            box-shadow: 0 4px 16px rgba(201, 48, 44, 0.4) !important;
        }
        
        .main > div:first-child .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #ac2925 0%, #9a2421 100%) !important;
            border-color: #ac2925 !important;
            transform: translateY(-2px) !important;
        }
        
        /* ===== MAIN LAYOUT ===== */
        .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section {
            background: #2d2d2d !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* ===== SIDEBAR ===== */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a1a 0%, #242424 100%) !important;
            border-right: 1px solid #333 !important;
        }
        
        [data-testid="stSidebar"] > div:first-child {
            padding: 2rem 1.5rem !important;
        }
        
        /* Hide default navigation */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* ===== SIDEBAR HEADER ===== */
        .sidebar-header {
            margin-bottom: 2.5rem;
        }
        
        .logo-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .logo-text h1 {
            font-size: 26px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin: 0 !important;
            line-height: 1.2 !important;
            letter-spacing: -0.5px;
        }
        
        .logo-text p {
            font-size: 12px !important;
            color: #888 !important;
            margin: 0 !important;
            letter-spacing: 0.5px;
            font-weight: 500;
        }
        
        .sidebar-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, #333 50%, transparent 100%);
            margin: 1.5rem 0;
        }
        
        .sidebar-title {
            font-size: 12px !important;
            font-weight: 700 !important;
            color: #fff !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 1rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #333;
        }
        
        /* ===== SIDEBAR BUTTONS ===== */
        [data-testid="stSidebar"] .stButton > button {
            background: #2d2d2d !important;
            color: #aaa !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            padding: 14px 18px !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            text-align: center !important;
            transition: all 0.3s ease !important;
            margin-bottom: 10px !important;
            width: 100% !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: #3d3d3d !important;
            color: #fff !important;
            border-color: #555 !important;
            transform: translateX(4px) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%) !important;
            color: #fff !important;
            border-color: #c9302c !important;
            box-shadow: 0 2px 8px rgba(201, 48, 44, 0.3) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #ac2925 0%, #9a2421 100%) !important;
            border-color: #ac2925 !important;
        }
        
        /* ===== SIDEBAR FOOTER ===== */
        .sidebar-spacer {
            flex: 1;
            min-height: 100px;
        }
        
        .sidebar-footer {
            margin-top: auto;
            padding-top: 2rem;
            border-top: 1px solid #333;
        }
        
        .info-item {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 14px 0;
            color: #888;
            font-size: 13px;
            font-weight: 500;
        }
        
        .info-item svg {
            opacity: 0.7;
        }
        
        /* ===== SELECT BOXES ===== */
        .main [data-testid="stSelectbox"] {
            margin-bottom: 2rem;
        }
        
        .main [data-testid="stSelectbox"] label {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 10px !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background: #3d3d3d !important;
            border: 2px solid #4d4d4d !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #ffffff !important;
            font-weight: 500 !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"]:hover {
            border-color: #666 !important;
            box-shadow: 0 0 0 3px rgba(201, 48, 44, 0.1) !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"]:focus-within {
            border-color: #c9302c !important;
            box-shadow: 0 0 0 3px rgba(201, 48, 44, 0.2) !important;
        }
        
        /* ===== FILE UPLOADER ===== */
        [data-testid="stFileUploader"] {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%) !important;
            border: 2px dashed #555 !important;
            border-radius: 12px !important;
            padding: 4rem 2rem !important;
            text-align: center;
            transition: all 0.3s ease !important;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #c9302c !important;
            background: linear-gradient(135deg, #404040 0%, #383838 100%) !important;
            box-shadow: 0 8px 24px rgba(201, 48, 44, 0.15) !important;
        }
        
        [data-testid="stFileUploader"] section {
            border: none !important;
            background: transparent !important;
        }
        
        [data-testid="stFileUploader"] label {
            color: #ccc !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        [data-testid="stFileUploader"] * {
            color: #ccc !important;
        }
        
        [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 36px !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 12px rgba(201, 48, 44, 0.3) !important;
        }
        
        [data-testid="stFileUploader"] button:hover {
            background: linear-gradient(135deg, #ac2925 0%, #9a2421 100%) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 16px rgba(201, 48, 44, 0.4) !important;
        }
        
        /* ===== BUTTONS ===== */
        .main .stButton > button {
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 16px 36px !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 12px rgba(201, 48, 44, 0.3) !important;
        }
        
        .main .stButton > button:hover {
            background: linear-gradient(135deg, #ac2925 0%, #9a2421 100%) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 16px rgba(201, 48, 44, 0.4) !important;
        }
        
        /* ===== DOWNLOAD BUTTON ===== */
        .main .stDownloadButton > button {
            background: linear-gradient(135deg, #5cb85c 0%, #4cae4c 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 16px 36px !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 12px rgba(92, 184, 92, 0.3) !important;
        }
        
        .main .stDownloadButton > button:hover {
            background: linear-gradient(135deg, #4cae4c 0%, #449d44 100%) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 16px rgba(92, 184, 92, 0.4) !important;
        }
        
        /* ===== TOOL CARD ===== */
        .tool-card {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%);
            border-radius: 12px;
            padding: 3rem;
            margin-bottom: 3rem;
            border: 1px solid #4d4d4d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }
        
        .tool-card:hover {
            border-color: #666;
            box-shadow: 0 12px 32px rgba(0,0,0,0.4);
            transform: translateY(-4px);
        }
        
        .tool-card h3 {
            font-size: 28px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 1.2rem !important;
            letter-spacing: -0.5px;
        }
        
        .tool-card p {
            font-size: 16px !important;
            color: #ccc !important;
            line-height: 1.7 !important;
        }
        
        /* ===== INFO BOX ===== */
        .info-box {
            background: #2d2d2d;
            border-left: 4px solid #c9302c;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        }
        
        .info-box h4 {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 1.2rem !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
            color: #ccc !important;
            margin: 10px 0;
            font-size: 14px !important;
            padding-left: 28px;
            position: relative;
            line-height: 1.6;
        }
        
        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #c9302c;
            font-weight: bold;
            font-size: 16px;
        }
        
        /* ===== SUCCESS MESSAGE ===== */
        .success-msg {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%);
            color: #5cb85c;
            padding: 1.2rem 1.8rem;
            border-left: 4px solid #5cb85c;
            border-radius: 8px;
            font-weight: 600;
            margin: 1.5rem 0;
            box-shadow: 0 4px 12px rgba(92, 184, 92, 0.2);
            font-size: 15px;
        }
        
        /* ===== FEATURE GRID ===== */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%);
            border-radius: 12px;
            padding: 2.5rem;
            text-align: center;
            border: 1px solid #4d4d4d;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        }
        
        .feature-card:hover {
            border-color: #666;
            transform: translateY(-8px);
            box-shadow: 0 12px 32px rgba(0,0,0,0.3);
        }
        
        .feature-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 1.5rem auto;
            background: linear-gradient(135deg, #c9302c 0%, #ac2925 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 16px rgba(201, 48, 44, 0.3);
        }
        
        .feature-card h4 {
            font-size: 20px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 0.8rem !important;
            letter-spacing: -0.3px;
        }
        
        .feature-card p {
            font-size: 14px !important;
            color: #aaa !important;
            line-height: 1.6 !important;
        }
        
        /* ===== WIP CONTAINER ===== */
        .wip-container {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%);
            border-radius: 12px;
            padding: 5rem 3rem;
            text-align: center;
            margin: 2rem 0;
            border: 1px solid #4d4d4d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }
        
        .wip-icon {
            width: 100px;
            height: 100px;
            margin: 0 auto 2rem auto;
            background: linear-gradient(135deg, #2d2d2d 0%, #252525 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }
        
        .wip-container h2 {
            font-size: 36px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 0.8rem !important;
            letter-spacing: -0.5px;
        }
        
        .wip-container h3 {
            font-size: 22px !important;
            font-weight: 600 !important;
            color: #888 !important;
            margin-bottom: 1.2rem !important;
        }
        
        .wip-container p {
            font-size: 16px !important;
            color: #ccc !important;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background: transparent;
            border-bottom: 2px solid #4d4d4d;
            padding-bottom: 0;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            color: #888;
            padding: 14px 28px;
            font-weight: 700;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            color: #ccc;
        }
        
        .stTabs [aria-selected="true"] {
            background: transparent;
            color: #fff;
            border-bottom: 3px solid #c9302c;
        }
        
        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            background: #3d3d3d !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            padding: 1rem 1.5rem !important;
            transition: all 0.3s ease !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: #404040 !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        }
        
        .streamlit-expanderContent {
            background: #2d2d2d !important;
            color: #ccc !important;
            padding: 1.5rem !important;
        }
        
        /* ===== MESSAGES ===== */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: 8px !important;
            padding: 1.2rem 1.8rem !important;
            background: #3d3d3d !important;
            color: #ccc !important;
            font-weight: 500 !important;
            border-left: 4px solid !important;
        }
        
        .stSuccess {
            border-left-color: #5cb85c !important;
        }
        
        .stInfo {
            border-left-color: #5bc0de !important;
        }
        
        .stWarning {
            border-left-color: #f0ad4e !important;
        }
        
        .stError {
            border-left-color: #d9534f !important;
        }
        
        /* ===== FOOTER ===== */
        .main-footer {
            margin-top: 4rem;
            padding: 3rem 3rem;
            border-top: 1px solid #4d4d4d;
            background: linear-gradient(135deg, #1a1a1a 0%, #242424 100%);
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1400px;
            margin: 0 auto;
            color: #888;
            font-size: 14px;
            font-weight: 500;
        }
        
        .footer-right {
            display: flex;
            gap: 2.5rem;
        }
        
        .footer-right a {
            color: #888;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.2s ease;
        }
        
        .footer-right a:hover {
            color: #fff;
        }
        
        /* ===== TEXT COLORS ===== */
        .main * {
            color: #ccc !important;
        }
        
        .main h1, .main h2, .main h3 {
            color: #ffffff !important;
        }
        
        .main h2 {
            margin-bottom: 2.5rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.5px !important;
        }
        
        /* ===== SUPPORTED FORMATS SECTION ===== */
        .formats-section {
            background: linear-gradient(135deg, #3d3d3d 0%, #353535 100%);
            border-radius: 12px;
            padding: 3rem;
            margin: 3rem 0;
            border: 1px solid #4d4d4d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }
        
        .formats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .format-badge {
            background: #2d2d2d;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #333;
            font-weight: 600;
            color: #ccc;
            transition: all 0.3s ease;
        }
        
        .format-badge:hover {
            background: #353535;
            border-color: #c9302c;
            color: #fff;
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(201, 48, 44, 0.2);
        }
        
        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .content-wrapper {
                padding: 0 2rem 3rem 2rem !important;
            }
            
            .hero-section {
                padding: 3rem 2rem;
                margin: 0 -2rem 3rem -2rem;
            }
            
            .hero-section h1 {
                font-size: 36px !important;
            }
            
            .hero-section p {
                font-size: 16px !important;
            }
            
            .stats-row {
                gap: 2rem;
            }
            
            .stat-number {
                font-size: 28px;
            }
            
            .footer-content {
                flex-direction: column;
                gap: 1.5rem;
                text-align: center;
            }
            
            .nav-links {
                display: none;
            }
            
            .feature-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
    """, unsafe_allow_html=True)