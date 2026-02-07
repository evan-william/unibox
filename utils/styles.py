import streamlit as st

def apply_custom_styles():
    """Apply professional black and white styling"""
    st.markdown("""
        <style>
        /* Main Container */
        .main {
            background-color: #ffffff;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #1a1a1a;
            border-right: 1px solid #e0e0e0;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
        [data-testid="stSidebar"] label {
            color: #ffffff !important;
        }
        
        /* Remove Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Button Styling */
        .stButton > button {
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: #000000;
            color: #ffffff;
            border: none;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            background-color: #2a2a2a;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        
        /* Download Button */
        .stDownloadButton > button {
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: #ffffff;
            color: #000000;
            border: 2px solid #000000;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }
        
        .stDownloadButton > button:hover {
            background-color: #000000;
            color: #ffffff;
        }
        
        /* File Uploader */
        [data-testid="stFileUploader"] {
            background-color: #fafafa;
            border: 2px dashed #d0d0d0;
            border-radius: 4px;
            padding: 30px;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #000000;
        }
        
        /* Tool Card */
        .tool-card {
            background-color: #fafafa;
            padding: 32px;
            border-radius: 4px;
            border: 1px solid #e0e0e0;
            margin-bottom: 24px;
        }
        
        .tool-card h3 {
            color: #000000;
            font-weight: 600;
            margin-bottom: 12px;
            font-size: 20px;
        }
        
        .tool-card p {
            color: #666666;
            font-size: 15px;
            line-height: 1.6;
        }
        
        /* Info Box */
        .info-box {
            background-color: #f5f5f5;
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
            color: #333333;
            margin: 8px 0;
            font-size: 14px;
        }
        
        /* WIP Container */
        .wip-container {
            text-align: center;
            padding: 80px 40px;
            background-color: #fafafa;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            margin: 40px 0;
        }
        
        .wip-container h2 {
            color: #000000;
            font-weight: 600;
            margin-bottom: 16px;
            font-size: 24px;
        }
        
        .wip-container h3 {
            color: #666666;
            font-weight: 400;
            margin-bottom: 12px;
            font-size: 18px;
        }
        
        .wip-container p {
            color: #999999;
            font-size: 15px;
        }
        
        /* Headers */
        h1 {
            color: #000000;
            font-weight: 700;
            font-size: 32px;
        }
        
        h2 {
            color: #000000;
            font-weight: 600;
            font-size: 24px;
        }
        
        h3 {
            color: #000000;
            font-weight: 600;
        }
        
        /* Divider */
        hr {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 24px 0;
        }
        
        /* Success Message */
        .success-msg {
            background-color: #f0f0f0;
            color: #000000;
            padding: 16px;
            border-left: 3px solid #000000;
            border-radius: 4px;
            font-weight: 500;
        }
        
        /* Selectbox */
        [data-testid="stSelectbox"] > div > div {
            background-color: #fafafa;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
        }
        
        /* Text styling */
        p {
            color: #333333;
            font-size: 15px;
            line-height: 1.6;
        }
        
        /* Remove colorful alerts */
        .stSuccess, .stInfo, .stWarning, .stError {
            background-color: #f5f5f5 !important;
            color: #000000 !important;
            border-left: 3px solid #000000 !important;
            border-radius: 4px !important;
        }
        </style>
    """, unsafe_allow_html=True)