import streamlit as st

def apply_custom_styles():
    """Apply professional black and white styling with proper visibility"""
    st.markdown("""
        <style>
        /* FORCE WHITE BACKGROUND EVERYWHERE */
        .main, .block-container, 
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section,
        [data-testid="stAppViewContainer"] > section > div {
            background-color: #ffffff !important;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #1a1a1a !important;
            border-right: 1px solid #e0e0e0;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        
        /* Remove Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* ALL TEXT BLACK ON WHITE */
        body, p, h1, h2, h3, h4, h5, h6, span, div, label, li {
            color: #000000 !important;
        }
        
        /* Headers */
        h1 {
            font-weight: 700 !important;
            font-size: 32px !important;
        }
        
        h2 {
            font-weight: 600 !important;
            font-size: 24px !important;
        }
        
        h3 {
            font-weight: 600 !important;
            font-size: 20px !important;
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
        
        /* File Uploader */
        [data-testid="stFileUploader"] {
            background-color: #f5f5f5 !important;
            border: 2px dashed #cccccc !important;
            border-radius: 4px;
            padding: 30px;
        }
        
        [data-testid="stFileUploader"] * {
            color: #000000 !important;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #000000 !important;
        }
        
        /* Selectbox */
        [data-testid="stSelectbox"] {
            color: #000000 !important;
        }
        
        [data-testid="stSelectbox"] * {
            color: #000000 !important;
            background-color: #ffffff !important;
        }
        
        [data-testid="stSelectbox"] label {
            font-weight: 500 !important;
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
        
        .info-box * {
            color: #000000 !important;
        }
        
        .info-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .info-box li {
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
        
        .wip-container * {
            color: #000000 !important;
        }
        
        .wip-container h2 {
            font-weight: 600;
            margin-bottom: 16px;
            font-size: 24px;
        }
        
        .wip-container h3 {
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
        
        /* Streamlit default messages */
        .stSuccess, .stInfo, .stWarning, .stError {
            background-color: #f5f5f5 !important;
            color: #000000 !important;
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
        
        .streamlit-expanderHeader * {
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