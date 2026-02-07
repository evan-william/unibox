import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the Streamlit app"""
    st.markdown("""
        <style>
        /* Main Container */
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e3a5f 0%, #2d5580 100%);
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
            color: #ffffff !important;
        }
        
        /* Remove default Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Button Styling */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        
        /* Download Button */
        .stDownloadButton > button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        
        /* File Uploader */
        [data-testid="stFileUploader"] {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        /* Cards/Containers */
        .tool-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        
        .tool-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        }
        
        /* WIP Container */
        .wip-container {
            text-align: center;
            padding: 80px 40px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin: 40px 0;
        }
        
        .wip-container h2 {
            color: #666;
            font-weight: 600;
            margin-bottom: 15px;
        }
        
        .wip-container p {
            color: #888;
            font-size: 1.1em;
        }
        
        /* Info boxes */
        .stAlert {
            border-radius: 8px;
        }
        
        /* Headers */
        h1 {
            color: #1e3a5f;
            font-weight: 700;
        }
        
        h2, h3 {
            color: #2d5580;
        }
        
        /* Selectbox */
        [data-testid="stSelectbox"] {
            background-color: rgba(255,255,255,0.1);
            border-radius: 8px;
        }
        
        /* Success/Error Messages */
        .stSuccess {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
            border-radius: 8px;
        }
        
        .stError {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            border-radius: 8px;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #667eea !important;
        }
        </style>
    """, unsafe_allow_html=True)