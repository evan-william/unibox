import streamlit as st

def apply_custom_styles():
    """Apply professional CloudConvert dark theme"""
    
    st.markdown("""
        <style>
        /* ===== GLOBAL RESET ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* ===== REMOVE STREAMLIT BRANDING ===== */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* ===== TOP NAVIGATION ===== */
        .top-nav {
            background: #1a1a1a;
            padding: 1rem 2rem;
            margin: -3rem -2rem 2rem -2rem;
            border-bottom: 1px solid #333;
        }
        
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .nav-brand span {
            font-size: 24px;
            font-weight: 700;
            color: #fff;
        }
        
        /* Navigation tab buttons */
        .main > div:first-child .stButton > button {
            background: transparent !important;
            color: #aaa !important;
            border: 1px solid #333 !important;
            border-radius: 4px !important;
            padding: 10px 20px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
        }
        
        .main > div:first-child .stButton > button:hover {
            background: #2d2d2d !important;
            color: #fff !important;
            border-color: #555 !important;
        }
        
        .main > div:first-child .stButton > button[kind="primary"] {
            background: #c9302c !important;
            color: #fff !important;
            border-color: #c9302c !important;
        }
        
        .main > div:first-child .stButton > button[kind="primary"]:hover {
            background: #ac2925 !important;
            border-color: #ac2925 !important;
        }
        
        /* ===== MAIN LAYOUT ===== */
        .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section {
            background: #2d2d2d !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 3rem 2rem 2rem 2rem !important;
            max-width: 1200px !important;
        }
        
        /* ===== SIDEBAR ===== */
        [data-testid="stSidebar"] {
            background: #1a1a1a !important;
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
            margin-bottom: 2rem;
        }
        
        .logo-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .logo-text h1 {
            font-size: 24px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin: 0 !important;
            line-height: 1.2 !important;
        }
        
        .logo-text p {
            font-size: 12px !important;
            color: #888 !important;
            margin: 0 !important;
            letter-spacing: 0.5px;
        }
        
        .sidebar-divider {
            height: 1px;
            background: #333;
            margin: 1.5rem 0;
        }
        
        .sidebar-title {
            font-size: 12px !important;
            font-weight: 700 !important;
            color: #fff !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 1rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #333;
        }
        
        /* ===== SIDEBAR BUTTONS ===== */
        [data-testid="stSidebar"] .stButton > button {
            background: transparent !important;
            color: #aaa !important;
            border: 1px solid #333 !important;
            border-radius: 4px !important;
            padding: 12px 16px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            text-align: center !important;
            transition: all 0.2s ease !important;
            margin-bottom: 8px !important;
            width: 100% !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: #2d2d2d !important;
            color: #fff !important;
            border-color: #555 !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: #c9302c !important;
            color: #fff !important;
            border-color: #c9302c !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            background: #ac2925 !important;
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
            gap: 10px;
            margin: 12px 0;
            color: #888;
            font-size: 13px;
        }
        
        .info-item svg {
            opacity: 0.6;
        }
        
        /* ===== HERO SECTION ===== */
        .hero-section {
            background: #3d3d3d;
            border-radius: 4px;
            padding: 4rem 3rem;
            margin-bottom: 3rem;
            border: 1px solid #4d4d4d;
        }
        
        .hero-section h1 {
            font-size: 48px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 1rem !important;
            line-height: 1.2 !important;
        }
        
        .hero-section p {
            font-size: 18px !important;
            color: #ccc !important;
            max-width: 700px;
            margin: 0 auto !important;
            line-height: 1.6 !important;
        }
        
        /* ===== CONVERTER BOX ===== */
        .converter-box {
            background: #3d3d3d;
            border-radius: 4px;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 800px;
            border: 1px solid #4d4d4d;
        }
        
        .converter-row {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .converter-item {
            flex: 1;
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            padding: 1rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .converter-item:hover {
            border-color: #4A90E2;
            background: #f0f7ff;
        }
        
        .converter-arrow {
            color: #666;
            font-size: 24px;
            font-weight: 300;
        }
        
        /* ===== SELECT BOXES ===== */
        .main [data-testid="stSelectbox"] {
            margin-bottom: 1.5rem;
        }
        
        .main [data-testid="stSelectbox"] label {
            font-size: 14px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
            margin-bottom: 8px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background: #2d2d2d !important;
            border: 1px solid #4d4d4d !important;
            border-radius: 4px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #ffffff !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"]:hover {
            border-color: #666 !important;
        }
        
        /* ===== FILE UPLOADER ===== */
        [data-testid="stFileUploader"] {
            background: #3d3d3d !important;
            border: 2px dashed #555 !important;
            border-radius: 4px !important;
            padding: 3rem 2rem !important;
            text-align: center;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #777 !important;
            background: #404040 !important;
        }
        
        [data-testid="stFileUploader"] section {
            border: none !important;
            background: transparent !important;
        }
        
        [data-testid="stFileUploader"] label {
            color: #ccc !important;
        }
        
        [data-testid="stFileUploader"] * {
            color: #ccc !important;
        }
        
        [data-testid="stFileUploader"] button {
            background: #c9302c !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 12px 32px !important;
            font-weight: 600 !important;
            font-size: 15px !important;
        }
        
        [data-testid="stFileUploader"] button:hover {
            background: #ac2925 !important;
        }
        
        /* ===== BUTTONS ===== */
        .main .stButton > button {
            background: #c9302c !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        .main .stButton > button:hover {
            background: #ac2925 !important;
        }
        
        /* ===== DOWNLOAD BUTTON ===== */
        .main .stDownloadButton > button {
            background: #5cb85c !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        .main .stDownloadButton > button:hover {
            background: #4cae4c !important;
        }
        
        /* ===== TOOL CARD ===== */
        .tool-card {
            background: #3d3d3d;
            border-radius: 4px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            border: 1px solid #4d4d4d;
        }
        
        .tool-card h3 {
            font-size: 24px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 1rem !important;
        }
        
        .tool-card p {
            font-size: 16px !important;
            color: #ccc !important;
            line-height: 1.6 !important;
        }
        
        /* ===== INFO BOX ===== */
        .info-box {
            background: #2d2d2d;
            border-left: 4px solid #c9302c;
            border-radius: 4px;
            padding: 1.5rem;
        }
        
        .info-box h4 {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 1rem !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
            color: #ccc !important;
            margin: 8px 0;
            font-size: 14px !important;
            padding-left: 24px;
            position: relative;
        }
        
        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #c9302c;
            font-weight: bold;
        }
        
        /* ===== SUCCESS MESSAGE ===== */
        .success-msg {
            background: #3d3d3d;
            color: #5cb85c;
            padding: 1rem 1.5rem;
            border-left: 4px solid #5cb85c;
            border-radius: 4px;
            font-weight: 500;
            margin: 1rem 0;
        }
        
        /* ===== FEATURE GRID ===== */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .feature-card {
            background: #3d3d3d;
            border-radius: 4px;
            padding: 2rem;
            text-align: center;
            border: 1px solid #4d4d4d;
        }
        
        .feature-card:hover {
            border-color: #666;
        }
        
        .feature-icon {
            width: 60px;
            height: 60px;
            margin: 0 auto 1rem auto;
            background: #2d2d2d;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .feature-card h4 {
            font-size: 18px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 0.5rem !important;
        }
        
        .feature-card p {
            font-size: 14px !important;
            color: #aaa !important;
            line-height: 1.5 !important;
        }
        
        /* ===== WIP CONTAINER ===== */
        .wip-container {
            background: #3d3d3d;
            border-radius: 4px;
            padding: 4rem 2rem;
            text-align: center;
            margin: 2rem 0;
            border: 1px solid #4d4d4d;
        }
        
        .wip-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 1.5rem auto;
            background: #2d2d2d;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .wip-container h2 {
            font-size: 32px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            margin-bottom: 0.5rem !important;
        }
        
        .wip-container h3 {
            font-size: 20px !important;
            font-weight: 400 !important;
            color: #888 !important;
            margin-bottom: 1rem !important;
        }
        
        .wip-container p {
            font-size: 16px !important;
            color: #ccc !important;
        }
        
        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
            border-bottom: 1px solid #4d4d4d;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            color: #888;
            padding: 12px 24px;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background: transparent;
            color: #fff;
            border-bottom: 2px solid #c9302c;
        }
        
        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            background: #3d3d3d !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
            color: #ffffff !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: #404040 !important;
        }
        
        .streamlit-expanderContent {
            background: #2d2d2d !important;
            color: #ccc !important;
        }
        
        /* ===== MESSAGES ===== */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: 4px !important;
            padding: 1rem 1.5rem !important;
            background: #3d3d3d !important;
            color: #ccc !important;
        }
        
        /* ===== FOOTER ===== */
        .main-footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #4d4d4d;
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            color: #888;
            font-size: 14px;
        }
        
        .footer-right {
            display: flex;
            gap: 2rem;
        }
        
        .footer-right a {
            color: #888;
            text-decoration: none;
        }
        
        .footer-right a:hover {
            color: #ccc;
        }
        
        /* ===== TEXT COLORS ===== */
        .main * {
            color: #ccc !important;
        }
        
        .main h1, .main h2, .main h3 {
            color: #ffffff !important;
        }
        
        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .block-container {
                padding: 2rem 1rem !important;
            }
            
            .hero-section {
                padding: 3rem 2rem;
            }
            
            .hero-section h1 {
                font-size: 32px !important;
            }
            
            .footer-content {
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }
        }
        </style>
    """, unsafe_allow_html=True)