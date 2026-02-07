import streamlit as st

def apply_custom_styles(dark_mode=False):
    """Apply professional styling with dark mode support"""
    
    # Color scheme based on mode
    if dark_mode:
        # DARK MODE COLORS
        main_bg = "#1a1a1a"
        main_text = "#ffffff"
        sidebar_bg = "#1a1a1a"
        sidebar_text = "#ffffff"
        card_bg = "#2a2a2a"
        card_text = "#ffffff"
        border_color = "#404040"
        button_bg = "#ffffff"
        button_text = "#000000"
        button_hover = "#cccccc"
        download_bg = "#1a1a1a"
        download_text = "#ffffff"
        download_border = "#ffffff"
        download_hover_bg = "#ffffff"
        download_hover_text = "#000000"
        info_bg = "#2a2a2a"
        selectbox_bg = "#1a1a1a"
        selectbox_text = "#ffffff"
    else:
        # LIGHT MODE COLORS
        main_bg = "#ffffff"
        main_text = "#000000"
        sidebar_bg = "#ffffff"
        sidebar_text = "#000000"
        card_bg = "#f8f8f8"
        card_text = "#000000"
        border_color = "#e0e0e0"
        button_bg = "#000000"
        button_text = "#ffffff"
        button_hover = "#333333"
        download_bg = "#ffffff"
        download_text = "#000000"
        download_border = "#000000"
        download_hover_bg = "#000000"
        download_hover_text = "#ffffff"
        info_bg = "#f5f5f5"
        selectbox_bg = "#ffffff"
        selectbox_text = "#000000"
    
    st.markdown(f"""
        <style>
        /* MAIN CONTENT */
        .main, .block-container, 
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section,
        [data-testid="stAppViewContainer"] > section > div {{
            background-color: {main_bg} !important;
        }}
        
        /* SIDEBAR */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            border-right: 1px solid {border_color};
        }}
        
        /* HIDE auto-generated navigation links */
        [data-testid="stSidebarNav"] {{
            display: none !important;
        }}
        
        /* SIDEBAR TEXT - Base styles */
        [data-testid="stSidebar"] *,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] div {{
            color: {sidebar_text} !important;
        }}
        
        /* SIDEBAR HEADERS */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {{
            color: {sidebar_text} !important;
        }}
        
        /* Sidebar markdown */
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] *,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
            color: {sidebar_text} !important;
        }}
        
        /* Sidebar selectbox */
        [data-testid="stSidebar"] [data-testid="stSelectbox"] *,
        [data-testid="stSidebar"] [data-testid="stSelectbox"] label,
        [data-testid="stSidebar"] [data-testid="stSelectbox"] [data-testid="stMarkdownContainer"] p {{
            color: {sidebar_text} !important;
        }}
        
        [data-testid="stSidebar"] [data-baseweb="select"] {{
            background-color: #2a2a2a !important;
        }}
        
        [data-testid="stSidebar"] [data-baseweb="select"] * {{
            color: #ffffff !important;
        }}
        
        /* SIDEBAR MODE SWITCHER BUTTON */
        [data-testid="stSidebar"] .stButton > button {{
            background-color: transparent !important;
            color: {sidebar_text} !important;
            border: 1px solid {sidebar_text} !important;
            font-size: 20px !important;
            padding: 8px !important;
            height: 40px !important;
            min-width: 40px !important;
            width: 40px !important;
        }}
        
        [data-testid="stSidebar"] .stButton > button:hover {{
            background-color: {'#2a2a2a' if dark_mode else '#f0f0f0'} !important;
        }}
        
        /* Remove Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* MAIN CONTENT TEXT */
        .main *,
        .main h1,
        .main h2,
        .main h3,
        .main p,
        .main span,
        .main div,
        .main label {{
            color: {main_text} !important;
        }}
        
        /* Headers */
        h1 {{
            font-weight: 700 !important;
            font-size: 32px !important;
            color: {main_text} !important;
        }}
        
        h2 {{
            font-weight: 600 !important;
            font-size: 24px !important;
            color: {main_text} !important;
        }}
        
        h3 {{
            font-weight: 600 !important;
            font-size: 20px !important;
            color: {main_text} !important;
        }}
        
        /* Buttons */
        .stButton > button {{
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: {button_bg} !important;
            color: {button_text} !important;
            border: none;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }}
        
        .stButton > button:hover {{
            background-color: {button_hover} !important;
        }}
        
        /* Download Button */
        .stDownloadButton > button {{
            width: 100%;
            border-radius: 4px;
            height: 48px;
            background-color: {download_bg} !important;
            color: {download_text} !important;
            border: 2px solid {download_border} !important;
            font-weight: 500;
            font-size: 15px;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }}
        
        .stDownloadButton > button:hover {{
            background-color: {download_hover_bg} !important;
            color: {download_hover_text} !important;
        }}
        
        /* File Uploader */
        [data-testid="stFileUploader"] {{
            background-color: {main_bg} !important;
            border: 2px dashed {border_color} !important;
            border-radius: 4px;
            padding: 30px;
        }}
        
        [data-testid="stFileUploader"]:hover {{
            border-color: {main_text} !important;
        }}
        
        [data-testid="stFileUploader"] label {{
            color: {main_text} !important;
            font-weight: 500;
        }}
        
        [data-testid="stFileUploader"] section {{
            background-color: {main_bg} !important;
            border: none !important;
        }}
        
        [data-testid="stFileUploader"] section * {{
            color: {main_text} !important;
        }}
        
        [data-testid="stFileUploader"] button {{
            color: {main_text} !important;
            background-color: {card_bg} !important;
        }}
        
        /* Tooltip/Help icon - Question mark in circle */
        [data-testid="stTooltipIcon"] svg {{
            color: {main_text} !important;
        }}

        [data-testid="stTooltipIcon"] circle {{
            stroke: {main_text} !important;
            fill: none !important;
        }}

        [data-testid="stTooltipIcon"] path {{
            fill: none !important;
            stroke: {main_text} !important;
        }}

        [data-testid="stTooltipIcon"] line {{
            stroke: {main_text} !important;
            stroke-width: 2 !important;
        }}

        /* Tooltip popup - Nuclear option to force white text */
        div[role="tooltip"],
        div[role="tooltip"] > div,
        div[role="tooltip"] span,
        div[role="tooltip"] p,
        [data-baseweb="tooltip"],
        [data-baseweb="tooltip"] *,
        .st-emotion-cache-ue6h4q,
        .st-emotion-cache-ue6h4q * {{
            background-color: #2d3748 !important;
            color: #ffffff !important;
        }}

        /* Selectbox in MAIN */
        .main [data-testid="stSelectbox"] {{
            background-color: {selectbox_bg} !important;
        }}
        
        .main [data-testid="stSelectbox"] label {{
            color: {main_text} !important;
            font-weight: 500;
        }}
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] {{
            background-color: {selectbox_bg} !important;
            border: 1px solid {border_color} !important;
        }}
        
        .main [data-testid="stSelectbox"] [data-baseweb="select"] * {{
            color: {selectbox_text} !important;
        }}
        
        /* Tool Card */
        .tool-card {{
            background-color: {card_bg} !important;
            padding: 32px;
            border-radius: 4px;
            border: 1px solid {border_color};
            margin-bottom: 24px;
        }}
        
        .tool-card h3 {{
            color: {card_text} !important;
            font-weight: 600;
            margin-bottom: 12px;
            font-size: 20px;
        }}
        
        .tool-card p {{
            color: {card_text} !important;
            font-size: 15px;
            line-height: 1.6;
        }}
        
        /* Info Box */
        .info-box {{
            background-color: {info_bg} !important;
            padding: 20px;
            border-left: 3px solid {main_text};
            border-radius: 4px;
        }}
        
        .info-box ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        
        .info-box li {{
            color: {main_text} !important;
            margin: 8px 0;
            font-size: 14px;
        }}
        
        /* WIP Container */
        .wip-container {{
            text-align: center;
            padding: 80px 40px;
            background-color: {card_bg} !important;
            border: 1px solid {border_color};
            border-radius: 4px;
            margin: 40px 0;
        }}
        
        .wip-container h2 {{
            color: {main_text} !important;
            font-weight: 600;
            margin-bottom: 16px;
            font-size: 24px;
        }}
        
        .wip-container h3 {{
            color: {main_text} !important;
            font-weight: 400;
            margin-bottom: 12px;
            font-size: 18px;
        }}
        
        .wip-container p {{
            color: {main_text} !important;
            font-size: 15px;
        }}
        
        /* Success Message */
        .success-msg {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
            padding: 16px;
            border-left: 3px solid {main_text};
            border-radius: 4px;
            font-weight: 500;
        }}
        
        /* Divider */
        hr {{
            border: none;
            border-top: 1px solid {border_color};
            margin: 24px 0;
        }}
        
        /* Streamlit messages */
        .stSuccess, .stInfo, .stWarning, .stError {{
            background-color: {card_bg} !important;
            border-left: 3px solid {main_text} !important;
        }}
        
        .stSuccess *, .stInfo *, .stWarning *, .stError * {{
            color: {main_text} !important;
        }}
        
        /* Expander */
        .streamlit-expanderHeader {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
        }}
        
        .streamlit-expanderContent {{
            background-color: {main_bg} !important;
        }}
        
        .streamlit-expanderContent * {{
            color: {main_text} !important;
        }}
        
        /* Markdown in main content */
        .main [data-testid="stMarkdownContainer"] p,
        .main [data-testid="stMarkdown"] p,
        [data-testid="stMarkdownContainer"] p {{
            color: {main_text} !important;
        }}
        </style>
    """, unsafe_allow_html=True)