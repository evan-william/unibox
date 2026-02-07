import streamlit as st

def apply_custom_styles():
    """Apply professional black and white styling with proper visibility"""
    st.markdown("""
        <style>
        /* MAIN CONTENT - WHITE BACKGROUND */
        .main, .block-container, 
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section,
        [data-testid="stAppViewContainer"] > section > div {
            background-color: #ffffff !important;
        }
        
        /* SIDEBAR - BLACK BACKGROUND WITH WHITE TEXT */
        [data-testid="stSidebar"] {
            background-color: #1a1a1a !important;
            border-right: 1px solid #e0e0e0;
        }
        
        /* All sidebar text WHITE - FIXED */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        
        /* Sidebar markdown paragraphs */
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #cccccc !important;
        }
        
        /* Sidebar selectbox WHITE TEXT */
        [data-testid="stSidebar"] [data-testid="stSelectbox"] label {
            color: #ffffff !important;
        }
        
        [data-testid="stSidebar"] [data-baseweb="select"] {
            background-color: #2a2a2a !important;
        }
        
        [data-testid="stSidebar"] [data-baseweb="select"] * {
            color: #ffffff !important;
        }
        
        /* Remove Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* MAIN CONTENT TEXT - BLACK */
        .main h1,
        .main h2,
        .main h3,
        .main p,
        .main span,
        .main div,
        .main label {
            color: #000000 !important;
        }
        
        /* Headers in main content */
        h1 {
            font-weight: 700 !important;
            font-size: 32px !important;
            color: #000000 !important;
        }
        
        h2 {
            font-weight: 600 !important;
            font-size: 24px !important;
            color: #000000 !important;
        }
        
        h3 {
            font-weight: 600 !important;
            font-size: 20px !important;
            color: #000000 !important;
        }
        
        /* Main content paragraphs */
        .main [data-testid="stMarkdownContainer"] p {
            color: #333333 !important;
        }
        
        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: #000000 !important;
            color: #ffffff !important;
            border: none;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            background-color: #333333 !important;
        }
        
        /* Download Button */
        .stDownloadButton > button {
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 2px solid #000000 !important;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }
        
        .stDownloadButton > button:hover {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        
        /* File Uploader - WHITE BACKGROUND */
        [data-testid="stFileUploader"] {
            background-color: #ffffff !important;
            border: 2px dashed #cccccc !important;
            border-radius: 4px;
            padding: 30px;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #000000 !important;
        }
        
        [data-testid="stFileUploader"] label {
            color: #000000 !important;
            font-weight: 500;
        }
        
        [data-testid="stFileUploader"] section {
            background-color: #ffffff !important;
            border: none !important;
        }
        
        [data-testid="stFileUploader"] section * {
            color: #000000 !important;
        }
        
        [data-testid="stFileUploader"] button {
            color: #000000 !important;
            background-color: #f5f5f5 !important;
        }
        
        /* Selectbox in MAIN content - WHITE BACKGROUND with BLACK TEXT */
        .main [data-testid="stSelectbox"] {
            background-color: #ffffff !important;
        }
        
        .main [data-testid="stSelectbox"] label {
            color: #000000 !important;
            font-weight: 500;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {
            background-color: #ffffff !important;
            border: 1px solid #d0d0d0 !important;
        }
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #000000 !important;
        }
        
        /* Tool Card */
        .tool-card {
            background-color: #f8f8f8 !important;
            padding: 32px;
            border-radius: 4px;
            border: 1px solid #e0e0e0;
            margin-bottom: 24px;
        }
        
        .tool-card h3 {
            color: #000000 !important;
            font-weight: 600;
            margin-bottom: 12px;
            font-size: 20px;
        }
        
        .tool-card p {
            color: #333333 !important;
            font-size: 15px;
            line-height: 1.6;
        }
        
        /* Info Box */
        .info-box {
            background-color: #f5f5f5 !important;
            padding: 20px;
            border-left: 3px solid #000000;
            border-radius: 4px;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
            color: #000000 !important;
            margin: 8px 0;
            font-size: 14px;
        }
        
        /* WIP Container */
        .wip-container {
            text-align: center;
            padding: 80px 40px;
            background-color: #f8f8f8 !important;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            margin: 40px 0;
        }
        
        .wip-container h2 {
            color: #000000 !important;
            font-weight: 600;
            margin-bottom: 16px;
            font-size: 24px;
        }
        
        .wip-container h3 {
            color: #333333 !important;
            font-weight: 400;
            margin-bottom: 12px;
            font-size: 18px;
        }
        
        .wip-container p {
            color: #666666 !important;
            font-size: 15px;
        }
        
        /* Success Message */
        .success-msg {
            background-color: #f0f0f0 !important;
            color: #000000 !important;
            padding: 16px;
            border-left: 3px solid #000000;
            border-radius: 4px;
            font-weight: 500;
        }
        
        /* Divider */
        hr {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 24px 0;
        }
        
        /* Streamlit messages */
        .stSuccess, .stInfo, .stWarning, .stError {
            background-color: #f5f5f5 !important;
            border-left: 3px solid #000000 !important;
        }
        
        .stSuccess *, .stInfo *, .stWarning *, .stError * {
            color: #000000 !important;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background-color: #f5f5f5 !important;
            color: #000000 !important;
        }
        
        .streamlit-expanderContent {
            background-color: #ffffff !important;
        }
        
        .streamlit-expanderContent * {
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)