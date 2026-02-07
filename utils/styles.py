import streamlit as st

def apply_custom_styles(dark_mode=True):
    """Apply CloudConvert-inspired professional styling"""
    
    # Color scheme based on mode
    if dark_mode:
        # DARK MODE COLORS (CloudConvert style)
        main_bg = "#2b2b2b"
        header_bg = "#3a3a3a"
        main_text = "#ffffff"
        secondary_text = "#b0b0b0"
        card_bg = "#3a3a3a"
        card_hover = "#454545"
        border_color = "#4a4a4a"
        button_primary = "#c94448"
        button_primary_hover = "#d45558"
        button_secondary = "#4a4a4a"
        button_secondary_hover = "#555555"
        input_bg = "#323232"
        select_bg = "#323232"
    else:
        # LIGHT MODE COLORS
        main_bg = "#f5f5f5"
        header_bg = "#ffffff"
        main_text = "#1a1a1a"
        secondary_text = "#666666"
        card_bg = "#ffffff"
        card_hover = "#f8f8f8"
        border_color = "#e0e0e0"
        button_primary = "#c94448"
        button_primary_hover = "#d45558"
        button_secondary = "#e0e0e0"
        button_secondary_hover = "#d0d0d0"
        input_bg = "#ffffff"
        select_bg = "#ffffff"
    
    st.markdown(f"""
        <style>
        /* RESET & BASE */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        /* HIDE STREAMLIT ELEMENTS */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        [data-testid="stSidebar"] {{display: none;}}
        
        /* MAIN CONTAINER */
        .main, .block-container, 
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > section,
        [data-testid="stAppViewContainer"] > section > div {{
            background-color: {main_bg} !important;
            max-width: 100% !important;
            padding: 0 !important;
        }}
        
        .block-container {{
            padding: 2rem 4rem !important;
            max-width: 1400px !important;
            margin: 0 auto !important;
        }}
        
        /* NAVBAR */
        .navbar-brand {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 24px;
            color: {main_text};
        }}
        
        .brand-icon {{
            font-size: 32px;
        }}
        
        .brand-text {{
            font-weight: 300;
            letter-spacing: -0.5px;
        }}
        
        .brand-text strong {{
            font-weight: 700;
        }}
        
        .navbar-divider {{
            height: 1px;
            background: {border_color};
            margin: 1.5rem 0 2rem 0;
        }}
        
        /* NAVIGATION BUTTONS */
        [data-testid="column"]:has(.navbar-brand) + [data-testid="column"] button,
        button[key="nav_doc"],
        button[key="nav_media"],  
        button[key="nav_dev"] {{
            background-color: transparent !important;
            color: {secondary_text} !important;
            border: none !important;
            font-size: 15px !important;
            font-weight: 500 !important;
            padding: 8px 16px !important;
            transition: all 0.2s ease !important;
            border-radius: 6px !important;
        }}
        
        [data-testid="column"]:has(.navbar-brand) + [data-testid="column"] button:hover,
        button[key="nav_doc"]:hover,
        button[key="nav_media"]:hover,
        button[key="nav_dev"]:hover {{
            background-color: {button_secondary} !important;
            color: {main_text} !important;
        }}
        
        /* MODE TOGGLE */
        button[key="mode_toggle"] {{
            background-color: transparent !important;
            border: 1px solid {border_color} !important;
            color: {main_text} !important;
            font-size: 18px !important;
            padding: 8px !important;
            width: 44px !important;
            height: 44px !important;
            min-width: 44px !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }}
        
        button[key="mode_toggle"]:hover {{
            background-color: {button_secondary} !important;
        }}
        
        /* HERO SECTION */
        .hero-section {{
            text-align: center;
            padding: 60px 20px;
            max-width: 900px;
            margin: 0 auto 40px auto;
        }}
        
        .hero-title {{
            font-size: 48px;
            font-weight: 700;
            color: {main_text};
            margin-bottom: 16px;
            line-height: 1.2;
        }}
        
        .hero-subtitle {{
            font-size: 18px;
            color: {secondary_text};
            line-height: 1.6;
            max-width: 700px;
            margin: 0 auto;
        }}
        
        /* CONVERTER SELECTOR */
        .converter-box {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 12px;
            padding: 40px;
            margin: 40px auto;
            max-width: 800px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        .converter-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .convert-label {{
            font-size: 16px;
            color: {secondary_text};
            font-weight: 500;
        }}
        
        .to-label {{
            font-size: 16px;
            color: {secondary_text};
            font-weight: 500;
        }}
        
        /* FILE UPLOAD AREA */
        .upload-area {{
            background: {input_bg};
            border: 2px dashed {border_color};
            border-radius: 8px;
            padding: 60px 40px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }}
        
        .upload-area:hover {{
            border-color: {button_primary};
            background: {card_hover};
        }}
        
        [data-testid="stFileUploader"] {{
            background-color: transparent !important;
            border: none !important;
            padding: 0 !important;
        }}
        
        [data-testid="stFileUploader"] section {{
            background-color: {input_bg} !important;
            border: 2px dashed {border_color} !important;
            border-radius: 8px !important;
            padding: 60px 40px !important;
            transition: all 0.3s ease !important;
        }}
        
        [data-testid="stFileUploader"] section:hover {{
            border-color: {button_primary} !important;
            background-color: {card_hover} !important;
        }}
        
        [data-testid="stFileUploader"] label {{
            color: {main_text} !important;
            font-size: 16px !important;
            font-weight: 600 !important;
        }}
        
        [data-testid="stFileUploader"] small {{
            color: {secondary_text} !important;
        }}
        
        [data-testid="stFileUploader"] button {{
            background-color: {button_primary} !important;
            color: white !important;
            border: none !important;
            padding: 12px 32px !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            transition: all 0.2s ease !important;
        }}
        
        [data-testid="stFileUploader"] button:hover {{
            background-color: {button_primary_hover} !important;
        }}
        
        /* PRIMARY BUTTON (Convert) */
        .stButton > button,
        button[kind="primary"],
        button[kind="secondary"] {{
            background-color: {button_primary} !important;
            color: white !important;
            border: none !important;
            padding: 14px 40px !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
            height: auto !important;
        }}
        
        .stButton > button:hover,
        button[kind="primary"]:hover,
        button[kind="secondary"]:hover {{
            background-color: {button_primary_hover} !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(201, 68, 72, 0.3) !important;
        }}
        
        /* SELECTBOX */
        [data-testid="stSelectbox"] {{
            margin: 0 !important;
        }}
        
        [data-testid="stSelectbox"] label {{
            color: {main_text} !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            margin-bottom: 8px !important;
        }}
        
        [data-testid="stSelectbox"] [data-baseweb="select"] {{
            background-color: {select_bg} !important;
            border: 1px solid {border_color} !important;
            border-radius: 6px !important;
            min-width: 200px !important;
        }}
        
        [data-testid="stSelectbox"] [data-baseweb="select"]:hover {{
            border-color: {button_primary} !important;
        }}
        
        [data-testid="stSelectbox"] [data-baseweb="select"] > div {{
            background-color: {select_bg} !important;
            color: {main_text} !important;
            font-size: 15px !important;
            font-weight: 500 !important;
            padding: 12px 16px !important;
        }}
        
        /* Dropdown menu */
        [data-baseweb="popover"] {{
            background-color: {card_bg} !important;
            border: 1px solid {border_color} !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
        }}
        
        [role="option"] {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
            padding: 12px 16px !important;
            font-size: 15px !important;
        }}
        
        [role="option"]:hover {{
            background-color: {card_hover} !important;
        }}
        
        /* TEXT & TYPOGRAPHY */
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
        
        h1 {{
            font-weight: 700 !important;
            font-size: 36px !important;
            margin-bottom: 16px !important;
        }}
        
        h2 {{
            font-weight: 600 !important;
            font-size: 28px !important;
            margin-bottom: 12px !important;
        }}
        
        h3 {{
            font-weight: 600 !important;
            font-size: 22px !important;
            margin-bottom: 10px !important;
        }}
        
        /* CARDS & SECTIONS */
        .feature-card {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 10px;
            padding: 24px;
            transition: all 0.3s ease;
        }}
        
        .feature-card:hover {{
            background: {card_hover};
            border-color: {button_primary};
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        }}
        
        .feature-card h3 {{
            color: {main_text} !important;
            font-size: 18px !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
        }}
        
        .feature-card p {{
            color: {secondary_text} !important;
            font-size: 14px !important;
            line-height: 1.5 !important;
        }}
        
        /* SUCCESS/INFO MESSAGES */
        .success-msg {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
            border-left: 4px solid #10b981 !important;
            padding: 16px 20px !important;
            border-radius: 6px !important;
            margin: 16px 0 !important;
        }}
        
        .info-box {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
            border-left: 4px solid {button_primary} !important;
            padding: 16px 20px !important;
            border-radius: 6px !important;
        }}
        
        /* OPTIONS SECTION */
        .options-section {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 10px;
            padding: 24px;
            margin: 30px 0;
        }}
        
        .options-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 16px;
            font-weight: 600;
            color: {main_text};
            margin-bottom: 20px;
        }}
        
        /* FORMAT INFO CARDS */
        .format-info {{
            background: {card_bg};
            border: 1px solid {border_color};
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .format-info h4 {{
            display: flex;
            align-items: center;
            gap: 8px;
            color: {main_text} !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
        }}
        
        .format-info p {{
            color: {secondary_text} !important;
            font-size: 14px !important;
            line-height: 1.5 !important;
        }}
        
        .format-link {{
            color: {button_primary} !important;
            text-decoration: none !important;
            font-weight: 500 !important;
        }}
        
        .format-link:hover {{
            text-decoration: underline !important;
        }}
        
        /* FOOTER */
        .footer-space {{
            height: 80px;
        }}
        
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: {header_bg};
            border-top: 1px solid {border_color};
            padding: 20px;
            text-align: center;
            color: {secondary_text};
            font-size: 14px;
        }}
        
        /* LOADING SPINNER */
        .stSpinner > div {{
            border-color: {button_primary} !important;
        }}
        
        /* TABS */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background-color: transparent;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background-color: {button_secondary} !important;
            color: {main_text} !important;
            border-radius: 6px !important;
            padding: 10px 20px !important;
            font-weight: 500 !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: {button_primary} !important;
            color: white !important;
        }}
        
        /* EXPANDER */
        .streamlit-expanderHeader {{
            background-color: {card_bg} !important;
            color: {main_text} !important;
            border: 1px solid {border_color} !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
        }}
        
        .streamlit-expanderHeader:hover {{
            background-color: {card_hover} !important;
        }}
        
        .streamlit-expanderContent {{
            background-color: {card_bg} !important;
            border: 1px solid {border_color} !important;
            border-top: none !important;
            border-radius: 0 0 6px 6px !important;
        }}
        
        /* INPUT FIELDS */
        input, textarea {{
            background-color: {input_bg} !important;
            color: {main_text} !important;
            border: 1px solid {border_color} !important;
            border-radius: 6px !important;
            padding: 12px 16px !important;
            font-size: 15px !important;
        }}
        
        input:focus, textarea:focus {{
            border-color: {button_primary} !important;
            outline: none !important;
        }}
        
        /* DOWNLOAD BUTTON */
        .stDownloadButton > button {{
            background-color: {button_primary} !important;
            color: white !important;
            border: none !important;
            padding: 14px 40px !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
        }}
        
        .stDownloadButton > button:hover {{
            background-color: {button_primary_hover} !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(201, 68, 72, 0.3) !important;
        }}
        
        /* RESPONSIVE */
        @media (max-width: 768px) {{
            .block-container {{
                padding: 1rem 2rem !important;
            }}
            
            .hero-title {{
                font-size: 32px !important;
            }}
            
            .converter-box {{
                padding: 24px !important;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)