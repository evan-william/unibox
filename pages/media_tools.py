import streamlit as st

def render():
    """Render Media Tools page with modern UI"""
    
    # Page title
    st.markdown("<h2 style='margin-bottom: 2rem; text-align: center;'>Media Converter</h2>", unsafe_allow_html=True)
    
    # Conversion selector
    st.markdown("<div style='max-width: 900px; margin: 0 auto;'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([5, 1, 5])
    
    with col1:
        media_type = st.selectbox(
            "Media Type",
            ["Image", "Video", "Audio"],
            key="media_type"
        )
    
    with col2:
        st.markdown("<div style='text-align: center; padding-top: 32px;'></div>", unsafe_allow_html=True)
    
    with col3:
        conversion_options = get_media_conversions(media_type)
        conversion = st.selectbox(
            "Conversion",
            conversion_options,
            key="conversion"
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border: none; border-top: 1px solid #4d4d4d; margin: 3rem 0;'>", unsafe_allow_html=True)
    
    # Render WIP for all media tools
    render_wip(conversion, media_type)
    
    # Features section
    st.markdown("""
        <div class='feature-grid'>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                        <circle cx="8.5" cy="8.5" r="1.5"/>
                        <polyline points="21 15 16 10 5 21"/>
                    </svg>
                </div>
                <h4>Image Processing</h4>
                <p>Convert between PNG, JPG, WEBP and other formats with quality control</p>
            </div>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <polygon points="23 7 16 12 23 17 23 7"/>
                        <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                    </svg>
                </div>
                <h4>Video Conversion</h4>
                <p>Transform video formats with custom resolution and compression settings</p>
            </div>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <path d="M9 18V5l12-2v13"/>
                        <circle cx="6" cy="18" r="3"/>
                        <circle cx="18" cy="16" r="3"/>
                    </svg>
                </div>
                <h4>Audio Tools</h4>
                <p>Convert audio files between formats with bitrate optimization</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_media_conversions(media_type):
    """Get conversion options based on media type"""
    conversions = {
        "Image": [
            "PNG to JPG",
            "JPG to PNG",
            "WEBP to PNG",
            "WEBP to JPG",
            "Image Resize",
            "Image Compress"
        ],
        "Video": [
            "MP4 to GIF",
            "Video Compress",
            "AVI to MP4",
            "MOV to MP4",
            "Video Resize"
        ],
        "Audio": [
            "MP3 to WAV",
            "WAV to MP3",
            "M4A to MP3",
            "Audio Compress"
        ]
    }
    return conversions.get(media_type, [])

def render_wip(tool_name, media_type):
    """Render Work In Progress page for media tools"""
    
    # Simple icons
    icon_map = {
        "Image": "🖼️",
        "Video": "🎬",
        "Audio": "🎵"
    }
    
    icon = icon_map.get(media_type, "⚙️")
    
    st.markdown(f"""
        <div class='wip-container'>
            <div class='wip-icon' style='font-size: 48px;'>
                {icon}
            </div>
            <h2>{tool_name}</h2>
            <h3>Coming Soon</h3>
            <p>This media conversion tool is currently under development and will be available soon.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Planned features in expander
    with st.expander("📋 Planned Features"):
        if "Image" in media_type:
            st.markdown("""
            - **Batch Conversion**: Process multiple images at once
            - **Quality Control**: Adjust compression and quality settings
            - **Format Optimization**: Smart format recommendations
            - **Resize & Crop**: Custom dimensions and aspect ratios
            - **Metadata Preservation**: Keep EXIF data when needed
            """)
        elif "Video" in media_type:
            st.markdown("""
            - **Multiple Formats**: Support for MP4, AVI, MOV, MKV, and more
            - **Quality Selection**: Choose resolution and bitrate
            - **Compression**: Reduce file size without quality loss
            - **Trimming**: Cut and trim video segments
            - **Frame Rate Control**: Adjust FPS for smooth playback
            """)
        elif "Audio" in media_type:
            st.markdown("""
            - **High-Quality Conversion**: Lossless and lossy formats
            - **Bitrate Selection**: Control audio quality and file size
            - **Format Compatibility**: MP3, WAV, FLAC, AAC, and more
            - **Batch Processing**: Convert multiple files simultaneously
            - **Metadata Editing**: Edit artist, album, and track info
            """)