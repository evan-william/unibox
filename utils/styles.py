import streamlit as st

def apply_custom_styles():
    """Apply clean, modern, bug-free styles"""
    
    st.markdown("""
        <style>
        /* IMPORTS */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        /* GLOBAL RESET */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }
        
        /* HIDE STREAMLIT ELEMENTS */
        #MainMenu, footer, header {visibility: hidden;}
        .stDeployButton {display: none;}
        
        /* MAIN LAYOUT */
        .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%) !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* HEADER */
        .modern-header {
            background: rgba(26, 26, 26, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .brand-name {
            font-size: 24px;
            font-weight: 800;
            background: linear-gradient(135deg, #ff4444 0%, #c9302c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .header-right {
            display: flex;
            align-items: center;
            gap: 2rem;
        }
        
        .header-link {
            color: #ccc;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .header-link:hover {
            color: #fff;
        }
        
        .header-btn-outline {
            background: transparent;
            border: 1.5px solid #444;
            color: #fff;
            padding: 8px 20px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .header-btn-outline:hover {
            border-color: #c9302c;
            color: #c9302c;
        }
        
        .header-btn-primary {
            background: linear-gradient(135deg, #c9302c 0%, #a02622 100%);
            border: none;
            color: #fff;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .header-btn-primary:hover {
            transform: translateY(-2px);
        }
        
        /* HERO SECTION */
        .hero-section {
            background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%);
            padding: 5rem 3rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .hero-content {
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
        }
        
        .hero-title {
            font-size: 56px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 1.5rem !important;
            line-height: 1.2 !important;
        }
        
        .hero-subtitle {
            font-size: 18px !important;
            color: #aaa !important;
            line-height: 1.7 !important;
            margin-bottom: 0 !important;
        }
        
        /* CONTENT CONTAINER */
        .content-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 3rem;
        }
        
        /* STATS SECTION */
        .stats-section {
            background: linear-gradient(135deg, #2a2a2a 0%, #1f1f1f 100%);
            padding: 4rem 3rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .stats-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 48px;
            font-weight: 800;
            background: linear-gradient(135deg, #ff4444 0%, #c9302c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            color: #888;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .stat-divider {
            width: 1px;
            height: 60px;
            background: rgba(255, 255, 255, 0.1);
        }
        
        /* WHY CHOOSE SECTION */
        .why-choose-section {
            padding: 6rem 3rem;
            background: #2d2d2d;
        }
        
        .section-header {
            text-align: center;
            max-width: 700px;
            margin: 0 auto 4rem auto;
        }
        
        .section-header h2 {
            font-size: 42px !important;
            font-weight: 800 !important;
            color: #fff !important;
            margin-bottom: 1rem !important;
        }
        
        .section-header p {
            font-size: 18px !important;
            color: #999 !important;
        }
        
        .features-showcase {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 2rem;
        }
        
        .showcase-card {
            background: rgba(61, 61, 61, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 2.5rem;
            transition: all 0.3s;
        }
        
        .showcase-card:hover {
            border-color: rgba(201, 48, 44, 0.5);
            transform: translateY(-4px);
        }
        
        .showcase-icon {
            width: 70px;
            height: 70px;
            background: rgba(201, 48, 44, 0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }
        
        .showcase-card h3 {
            font-size: 20px !important;
            font-weight: 700 !important;
            color: #fff !important;
            margin-bottom: 1rem !important;
        }
        
        .showcase-card p {
            font-size: 15px !important;
            color: #aaa !important;
            line-height: 1.7 !important;
        }
        
        /* FOOTER */
        .modern-footer {
            background: #1a1a1a;
            padding: 4rem 3rem 2rem 3rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .footer-container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            margin-bottom: 3rem;
        }
        
        .footer-col h4 {
            color: #fff !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            text-transform: uppercase;
            margin-bottom: 1.5rem !important;
        }
        
        .footer-col a {
            display: block;
            color: #888;
            text-decoration: none;
            font-size: 14px;
            margin-bottom: 0.75rem;
            transition: color 0.3s;
        }
        
        .footer-col a:hover {
            color: #c9302c;
        }
        
        .footer-bottom {
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            text-align: center;
        }
        
        .footer-bottom p {
            color: #666 !important;
            font-size: 14px !important;
            margin: 0.5rem 0 !important;
        }
        
        .footer-location {
            color: #555 !important;
        }
        
        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a1a 0%, #151515 100%) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
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
            gap: 12px;
        }
        
        .logo-text h1 {
            font-size: 22px !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #ff4444 0%, #c9302c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 !important;
        }
        
        .logo-text p {
            font-size: 12px !important;
            color: #666 !important;
            margin: 0 !important;
        }
        
        .sidebar-divider {
            height: 1px;
            background: rgba(255, 255, 255, 0.05);
            margin: 1.5rem 0;
        }
        
        .sidebar-title {
            font-size: 11px !important;
            font-weight: 700 !important;
            color: #888 !important;
            text-transform: uppercase;
            margin-bottom: 1rem !important;
        }
        
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(61, 61, 61, 0.3) !important;
            color: #aaa !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 8px !important;
            padding: 12px 16px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            text-align: left !important;
            margin-bottom: 8px !important;
            width: 100% !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(61, 61, 61, 0.5) !important;
            color: #fff !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #c9302c 0%, #a02622 100%) !important;
            color: #fff !important;
            border-color: transparent !important;
        }
        
        .sidebar-stats {
            background: rgba(61, 61, 61, 0.2);
            border-radius: 8px;
            padding: 1.5rem;
            margin: 2rem 0;
        }
        
        .sidebar-stat-item {
            text-align: center;
            margin-bottom: 1.5rem;
        }
        
        .sidebar-stat-item:last-child {
            margin-bottom: 0;
        }
        
        .stat-value {
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #ff4444 0%, #c9302c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .stat-desc {
            color: #666;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .sidebar-spacer {
            flex: 1;
            min-height: 40px;
        }
        
        .sidebar-footer {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .info-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 12px 0;
            color: #666;
            font-size: 12px;
        }
        
        /* BUTTONS */
        .main .stButton > button {
            background: linear-gradient(135deg, #c9302c 0%, #a02622 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        .main .stButton > button:hover {
            transform: translateY(-2px);
        }
        
        .main .stButton > button[kind="secondary"] {
            background: rgba(61, 61, 61, 0.5) !important;
            color: #aaa !important;
            border: 1.5px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        .main .stButton > button[kind="secondary"]:hover {
            background: rgba(61, 61, 61, 0.8) !important;
            border-color: rgba(201, 48, 44, 0.5) !important;
        }
        
        /* SELECT BOXES */
        .main [data-testid="stSelectbox"] label {
            font-size: 14px !important;
            font-weight: 600 !important;
            color: #fff !important;
            margin-bottom: 8px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background: rgba(61, 61, 61, 0.5) !important;
            border: 1.5px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 8px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #fff !important;
        }
        
        /* FILE UPLOADER */
        [data-testid="stFileUploader"] {
            background: rgba(61, 61, 61, 0.3) !important;
            border: 2px dashed rgba(255, 255, 255, 0.2) !important;
            border-radius: 12px !important;
            padding: 3rem 2rem !important;
            text-align: center;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: rgba(201, 48, 44, 0.5) !important;
        }
        
        [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, #c9302c 0%, #a02622 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 32px !important;
            font-weight: 600 !important;
        }
        
        /* DOWNLOAD BUTTON */
        .main .stDownloadButton > button {
            background: linear-gradient(135deg, #5cb85c 0%, #4cae4c 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
        }
        
        /* TOOL CARD */
        .tool-card {
            background: rgba(61, 61, 61, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 2.5rem;
            margin-bottom: 3rem;
        }
        
        .tool-card h3 {
            font-size: 24px !important;
            font-weight: 700 !important;
            color: #fff !important;
            margin-bottom: 1rem !important;
        }
        
        .tool-card p {
            font-size: 15px !important;
            color: #aaa !important;
            line-height: 1.7 !important;
        }
        
        /* INFO BOX */
        .info-box {
            background: rgba(45, 45, 45, 0.5);
            border-left: 4px solid #c9302c;
            border-radius: 8px;
            padding: 1.5rem;
        }
        
        .info-box h4 {
            font-size: 13px !important;
            font-weight: 700 !important;
            color: #fff !important;
            margin-bottom: 1rem !important;
            text-transform: uppercase;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
            color: #aaa !important;
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
        }
        
        /* SUCCESS MESSAGE */
        .success-msg {
            background: rgba(92, 184, 92, 0.1);
            color: #5cb85c;
            padding: 1rem 1.5rem;
            border-left: 4px solid #5cb85c;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* FEATURE GRID */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .feature-card {
            background: rgba(61, 61, 61, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
        }
        
        .feature-card:hover {
            border-color: rgba(201, 48, 44, 0.5);
            transform: translateY(-4px);
        }
        
        .feature-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 1.5rem auto;
            background: rgba(201, 48, 44, 0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .feature-card h4 {
            font-size: 18px !important;
            font-weight: 700 !important;
            color: #fff !important;
            margin-bottom: 0.75rem !important;
        }
        
        .feature-card p {
            font-size: 14px !important;
            color: #aaa !important;
        }
        
        /* WIP CONTAINER */
        .wip-container {
            background: rgba(61, 61, 61, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 4rem 2rem;
            text-align: center;
            margin: 2rem 0;
        }
        
        .wip-icon {
            width: 100px;
            height: 100px;
            margin: 0 auto 2rem auto;
            background: rgba(201, 48, 44, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
        }
        
        .wip-container h2 {
            font-size: 36px !important;
            font-weight: 700 !important;
            color: #fff !important;
            margin-bottom: 0.75rem !important;
        }
        
        .wip-container h3 {
            font-size: 20px !important;
            font-weight: 400 !important;
            color: #888 !important;
            margin-bottom: 1rem !important;
        }
        
        .wip-container p {
            font-size: 16px !important;
            color: #aaa !important;
        }
        
        /* TABS */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            color: #888;
            padding: 12px 24px;
        }
        
        .stTabs [aria-selected="true"] {
            color: #fff;
            border-bottom: 2px solid #c9302c;
        }
        
        /* EXPANDER */
        .streamlit-expanderHeader {
            background: rgba(61, 61, 61, 0.3) !important;
            border-radius: 8px !important;
            color: #fff !important;
        }
        
        .streamlit-expanderContent {
            background: rgba(45, 45, 45, 0.3) !important;
            color: #aaa !important;
        }
        
        /* TEXT COLORS */
        .main * {
            color: #ccc !important;
        }
        
        .main h1, .main h2, .main h3 {
            color: #fff !important;
        }
        
        /* PAGE HEADER */
        .page-header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
        }
        
        .page-title {
            font-size: 42px !important;
            font-weight: 800 !important;
            color: #fff !important;
            margin-bottom: 1rem !important;
        }
        
        .page-description {
            font-size: 17px !important;
            color: #999 !important;
            max-width: 700px;
            margin: 0 auto;
        }
        
        /* CONVERSION PANEL */
        .conversion-panel {
            background: rgba(61, 61, 61, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        }
        
        /* TOOL HEADER */
        .tool-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .tool-icon {
            font-size: 40px;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(201, 48, 44, 0.1);
            border-radius: 10px;
        }
        
        .tool-subtitle {
            color: #888 !important;
            font-size: 14px !important;
        }
        
        /* FILE READY */
        .file-ready {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(92, 184, 92, 0.1);
            border-left: 4px solid #5cb85c;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            color: #5cb85c !important;
        }
        
        .file-ready strong {
            color: #fff !important;
        }
        
        /* RESPONSIVE */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 36px !important;
            }
            
            .header-link {
                display: none;
            }
            
            .features-showcase {
                grid-template-columns: 1fr;
            }
        }
        </style>
    """, unsafe_allow_html=True)