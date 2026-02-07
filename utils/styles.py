import streamlit as st

def apply_custom_styles():
    """Apply professional CloudConvert-inspired styling"""
    
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
        
        /* ===== MAIN LAYOUT ===== */
        .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 3rem 2rem 2rem 2rem !important;
            max-width: 1200px !important;
        }
        
        /* ===== SIDEBAR ===== */
        [data-testid="stSidebar"] {
            background: #1a1a2e !important;
            border-right: none !important;
            box-shadow: 4px 0 12px rgba(0,0,0,0.1);
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
            background: rgba(255,255,255,0.1);
            margin: 1.5rem 0;
        }
        
        .sidebar-title {
            font-size: 11px !important;
            font-weight: 600 !important;
            color: #888 !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 1rem !important;
        }
        
        /* ===== SIDEBAR BUTTONS ===== */
        [data-testid="stSidebar"] .stButton > button {
            background: transparent !important;
            color: #ccc !important;
            border: 1px solid transparent !important;
            border-radius: 8px !important;
            padding: 12px 16px !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            text-align: left !important;
            transition: all 0.2s ease !important;
            margin-bottom: 8px !important;
            width: 100% !important;
            display: flex !important;
            align-items: center !important;
            gap: 12px !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255,255,255,0.05) !important;
            color: #fff !important;
            border-color: rgba(255,255,255,0.1) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: rgba(74,144,226,0.2) !important;
            color: #4A90E2 !important;
            border-color: rgba(74,144,226,0.3) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            background: rgba(74,144,226,0.3) !important;
        }
        
        /* ===== SIDEBAR FOOTER ===== */
        .sidebar-spacer {
            flex: 1;
            min-height: 100px;
        }
        
        .sidebar-footer {
            margin-top: auto;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.1);
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
            background: white;
            border-radius: 16px;
            padding: 4rem 3rem;
            margin-bottom: 3rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .hero-section h1 {
            font-size: 48px !important;
            font-weight: 700 !important;
            color: #1a1a2e !important;
            margin-bottom: 1rem !important;
            line-height: 1.2 !important;
        }
        
        .hero-section p {
            font-size: 18px !important;
            color: #666 !important;
            max-width: 700px;
            margin: 0 auto 2rem auto !important;
            line-height: 1.6 !important;
        }
        
        /* ===== CONVERTER BOX ===== */
        .converter-box {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 800px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
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
            color: #1a1a2e !important;
            margin-bottom: 8px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background: white !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            padding: 4px !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"]:hover {
            border-color: #4A90E2 !important;
        }
        
        /* ===== FILE UPLOADER ===== */
        [data-testid="stFileUploader"] {
            background: white !important;
            border: 2px dashed #dee2e6 !important;
            border-radius: 12px !important;
            padding: 3rem 2rem !important;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #4A90E2 !important;
            background: #f0f7ff !important;
        }
        
        [data-testid="stFileUploader"] section {
            border: none !important;
            background: transparent !important;
        }
        
        [data-testid="stFileUploader"] button {
            background: #4A90E2 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 32px !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            transition: all 0.2s ease !important;
        }
        
        [data-testid="stFileUploader"] button:hover {
            background: #357ABD !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(74,144,226,0.3);
        }
        
        /* ===== BUTTONS ===== */
        .main .stButton > button {
            background: #4A90E2 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 2px 8px rgba(74,144,226,0.2);
        }
        
        .main .stButton > button:hover {
            background: #357ABD !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(74,144,226,0.4);
        }
        
        .main .stButton > button:active {
            transform: translateY(0);
        }
        
        /* ===== DOWNLOAD BUTTON ===== */
        .main .stDownloadButton > button {
            background: #28a745 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            transition: all 0.2s ease !important;
        }
        
        .main .stDownloadButton > button:hover {
            background: #218838 !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(40,167,69,0.4);
        }
        
        /* ===== TOOL CARD ===== */
        .tool-card {
            background: white;
            border-radius: 12px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            border: 1px solid #f0f0f0;
        }
        
        .tool-card h3 {
            font-size: 24px !important;
            font-weight: 700 !important;
            color: #1a1a2e !important;
            margin-bottom: 1rem !important;
        }
        
        .tool-card p {
            font-size: 16px !important;
            color: #666 !important;
            line-height: 1.6 !important;
        }
        
        /* ===== INFO BOX ===== */
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #4A90E2;
            border-radius: 8px;
            padding: 1.5rem;
        }
        
        .info-box h4 {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #1a1a2e !important;
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
            color: #666 !important;
            margin: 8px 0;
            font-size: 14px !important;
            padding-left: 24px;
            position: relative;
        }
        
        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #4A90E2;
            font-weight: bold;
        }
        
        /* ===== SUCCESS MESSAGE ===== */
        .success-msg {
            background: #d4edda;
            color: #155724;
            padding: 1rem 1.5rem;
            border-left: 4px solid #28a745;
            border-radius: 8px;
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
            background: white;
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        }
        
        .feature-icon {
            width: 60px;
            height: 60px;
            margin: 0 auto 1rem auto;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .feature-card h4 {
            font-size: 18px !important;
            font-weight: 700 !important;
            color: #1a1a2e !important;
            margin-bottom: 0.5rem !important;
        }
        
        .feature-card p {
            font-size: 14px !important;
            color: #666 !important;
            line-height: 1.5 !important;
        }
        
        /* ===== WIP CONTAINER ===== */
        .wip-container {
            background: white;
            border-radius: 12px;
            padding: 4rem 2rem;
            text-align: center;
            margin: 2rem 0;
        }
        
        .wip-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 1.5rem auto;
            background: #f8f9fa;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .wip-container h2 {
            font-size: 32px !important;
            font-weight: 700 !important;
            color: #1a1a2e !important;
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
            color: #666 !important;
        }
        
        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
            border-bottom: 2px solid #e9ecef;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            color: #666;
            padding: 12px 24px;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background: transparent;
            color: #4A90E2;
            border-bottom: 2px solid #4A90E2;
        }
        
        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            background: #f8f9fa !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            color: #1a1a2e !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: #e9ecef !important;
        }
        
        /* ===== MESSAGES ===== */
        .stSuccess, .stInfo, .stWarning, .stError {
            border-radius: 8px !important;
            padding: 1rem 1.5rem !important;
        }
        
        /* ===== FOOTER ===== */
        .main-footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.2);
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            color: rgba(255,255,255,0.8);
            font-size: 14px;
        }
        
        .footer-right {
            display: flex;
            gap: 2rem;
        }
        
        .footer-right a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: color 0.2s ease;
        }
        
        .footer-right a:hover {
            color: white;
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
            
            .converter-row {
                flex-direction: column;
            }
            
            .footer-content {
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }
        }
        </style>
    """, unsafe_allow_html=True)