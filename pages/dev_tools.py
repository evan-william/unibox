import streamlit as st

def render():
    """Render Media Tools page with modern professional UI"""
    
    # Page header
    st.markdown("<h2 style='margin-bottom: 1rem; text-align: center; font-size: 42px; font-weight: 800;'>Media Converter</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 17px; margin-bottom: 3rem;'>Transform your media files between formats with professional quality</p>", unsafe_allow_html=True)
    
    # Conversion selector
    col_left, col_center, col_right = st.columns([1, 10, 1])
    
    with col_center:
        col1, col2, col3 = st.columns([5, 1, 5])
        
        with col1:
            media_type = st.selectbox(
                "Media Type",
                ["Image", "Video", "Audio"],
                key="media_type"
            )
        
        with col2:
            st.markdown("<div style='text-align: center; padding-top: 32px; font-size: 28px; color: #ff4757; font-weight: bold;'>→</div>", unsafe_allow_html=True)
        
        with col3:
            conversion_options = get_media_conversions(media_type)
            conversion = st.selectbox(
                "Conversion",
                conversion_options,
                key="conversion"
            )
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Render WIP for all media tools
    render_wip(conversion, media_type)
    
    # Features section
    st.markdown("""
        <div class='features-section'>
            <div class='features-header'>
                <h2>Powerful Media Conversion</h2>
                <p>Professional-grade tools for all your media conversion needs</p>
            </div>
            <div class='feature-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                            <circle cx="8.5" cy="8.5" r="1.5"/>
                            <polyline points="21 15 16 10 5 21"/>
                        </svg>
                    </div>
                    <h4>Image Processing</h4>
                    <p>Convert between PNG, JPG, WEBP and other formats with quality control and batch processing</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <polygon points="23 7 16 12 23 17 23 7"/>
                            <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                        </svg>
                    </div>
                    <h4>Video Conversion</h4>
                    <p>Transform video formats with custom resolution, compression, and quality settings</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M9 18V5l12-2v13"/>
                            <circle cx="6" cy="18" r="3"/>
                            <circle cx="18" cy="16" r="3"/>
                        </svg>
                    </div>
                    <h4>Audio Tools</h4>
                    <p>Convert audio files between formats with bitrate optimization and quality preservation</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                            <polyline points="7 10 12 15 17 10"/>
                            <line x1="12" y1="15" x2="12" y2="3"/>
                        </svg>
                    </div>
                    <h4>Batch Operations</h4>
                    <p>Process multiple media files simultaneously to save time and streamline your workflow</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <circle cx="12" cy="12" r="3"/>
                            <path d="M12 1v6m0 6v6m5.2-14.2l-4.2 4.2m0 6l-4.2 4.2m14.2-5.2h-6m-6 0H1m14.2 5.2l-4.2-4.2m0-6l-4.2-4.2"/>
                        </svg>
                    </div>
                    <h4>Quality Control</h4>
                    <p>Fine-tune output quality, resolution, bitrate, and compression for perfect results</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <polyline points="16 18 22 12 16 6"/>
                            <polyline points="8 6 2 12 8 18"/>
                        </svg>
                    </div>
                    <h4>Format Support</h4>
                    <p>Support for all major media formats including modern codecs and legacy formats</p>
                </div>
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
    
    # Icon mapping - NO newlines in SVG
    icon_map = {
        "Image": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
        "Video": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>',
        "Audio": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>'
    }
    
    icon = icon_map.get(media_type, "")
    
    # Use .format() instead of f-string to avoid issues
    wip_html = "<div class='wip-container'><div class='wip-icon'>{}</div><h2>{}</h2><h3>Coming Soon</h3><p>This media conversion tool is currently under development and will be available soon. We're working hard to bring you the best media conversion experience.</p></div>".format(icon, tool_name)
    
    st.markdown(wip_html, unsafe_allow_html=True)
    
    # Planned features in expander
    with st.expander("Planned Features", expanded=False):
        if "Image" in media_type:
            st.markdown("""
            **Advanced Image Processing:**
            - Batch conversion for processing multiple images simultaneously
            - Quality control with adjustable compression and quality settings
            - Smart format recommendations based on use case
            - Custom dimensions and aspect ratio control
            - Metadata preservation including EXIF data
            - Watermarking and overlay capabilities
            - Image optimization for web and mobile
            - Support for RAW image formats
            """)
        elif "Video" in media_type:
            st.markdown("""
            **Professional Video Tools:**
            - Support for MP4, AVI, MOV, MKV, WEBM and more
            - Custom resolution and bitrate selection
            - Compression without quality loss
            - Video trimming and cutting tools
            - Frame rate control for smooth playback
            - Audio track management
            - Subtitle embedding and extraction
            - Thumbnail generation
            """)
        elif "Audio" in media_type:
            st.markdown("""
            **High-Quality Audio Conversion:**
            - Lossless and lossy format support
            - Bitrate selection for quality control
            - Support for MP3, WAV, FLAC, AAC, OGG and more
            - Batch processing for multiple files
            - Metadata editing (artist, album, track info)
            - Audio normalization
            - Fade in/out effects
            - Audio trimming and splitting
            """)