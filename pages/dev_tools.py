import streamlit as st

def render():
    """Render Developer Tools page with modern professional UI"""
    
    # Page header
    st.markdown("<h2 style='margin-bottom: 1rem; text-align: center; font-size: 42px; font-weight: 800;'>Developer Tools</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 17px; margin-bottom: 3rem;'>Professional tools for developers to format, convert, and validate code</p>", unsafe_allow_html=True)
    
    # Tool selector
    col_left, col_center, col_right = st.columns([1, 10, 1])
    
    with col_center:
        col1, col2, col3 = st.columns([5, 1, 5])
        
        with col1:
            tool_category = st.selectbox(
                "Tool Category",
                ["Data Format", "Code Tools", "Utilities"],
                key="tool_category"
            )
        
        with col2:
            st.markdown("<div style='text-align: center; padding-top: 32px; font-size: 28px; color: #ff4757; font-weight: bold;'>→</div>", unsafe_allow_html=True)
        
        with col3:
            tools = get_dev_tools(tool_category)
            tool = st.selectbox(
                "Select Tool",
                tools,
                key="dev_tool"
            )
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Render WIP for all dev tools
    render_wip(tool, tool_category)
    
    # Features section
    st.markdown("""
        <div class='features-section'>
            <div class='features-header'>
                <h2>Essential Developer Tools</h2>
                <p>Streamline your development workflow with powerful utilities</p>
            </div>
            <div class='feature-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <polyline points="16 18 22 12 16 6"/>
                            <polyline points="8 6 2 12 8 18"/>
                        </svg>
                    </div>
                    <h4>Data Conversion</h4>
                    <p>Convert between JSON, XML, YAML, CSV and other data formats seamlessly with validation</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                        </svg>
                    </div>
                    <h4>Code Formatting</h4>
                    <p>Beautify and format your code with support for multiple programming languages and styles</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                        </svg>
                    </div>
                    <h4>Encoding Tools</h4>
                    <p>Base64 encoding, hash generation, and other security utilities for modern development</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                        </svg>
                    </div>
                    <h4>Performance Tools</h4>
                    <p>Minify JavaScript and CSS files to optimize load times and improve performance</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <polyline points="22 4 12 14.01 9 11.01"/>
                        </svg>
                    </div>
                    <h4>Validation</h4>
                    <p>Validate JSON, XML, and other data formats to ensure correctness and schema compliance</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <circle cx="12" cy="12" r="10"/>
                            <line x1="2" y1="12" x2="22" y2="12"/>
                            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
                        </svg>
                    </div>
                    <h4>API Testing</h4>
                    <p>Test REST APIs with custom headers, payloads, and authentication methods</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_dev_tools(category):
    """Get tools based on category"""
    tools = {
        "Data Format": [
            "JSON to CSV",
            "CSV to JSON",
            "XML to JSON",
            "JSON to XML",
            "YAML to JSON",
            "JSON to YAML"
        ],
        "Code Tools": [
            "Code Formatter",
            "SQL Formatter",
            "Minify JavaScript",
            "Minify CSS",
            "JSON Validator",
            "XML Validator"
        ],
        "Utilities": [
            "Base64 Encoder/Decoder",
            "Hash Generator",
            "API Tester",
            "Regular Expression Tester",
            "Diff Checker"
        ]
    }
    return tools.get(category, [])

def render_wip(tool_name, category):
    """Render Work In Progress page for dev tools"""
    
    # Icon mapping with SVG icons - ALL ON ONE LINE
    icon_map = {
        "Data Format": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>',
        "Code Tools": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
        "Utilities": '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
    }
    
    icon = icon_map.get(category, "")
    
    # Build HTML string with proper escaping
    wip_html = f"<div class='wip-container'><div class='wip-icon'>{icon}</div><h2>{tool_name}</h2><h3>Coming Soon</h3><p>This developer tool is currently under development and will be available soon. We're building powerful features to enhance your development workflow.</p></div>"
    
    st.markdown(wip_html, unsafe_allow_html=True)
    
    # Planned features in expander
    with st.expander("Planned Features", expanded=False):
        if "Data Format" in category:
            st.markdown("""
            **Advanced Data Conversion:**
            - Lightning-fast processing of large data files
            - Automatic validation of input and output formats
            - Beautiful, readable output formatting with syntax highlighting
            - Clear error messages with helpful suggestions
            - Batch processing to convert multiple files at once
            - Schema validation for JSON and XML formats
            - Custom formatting rules and options
            - Support for nested and complex data structures
            - Export with custom delimiters and encoding
            - Preview before download
            """)
        elif "Code Tools" in category:
            st.markdown("""
            **Professional Code Tools:**
            - Multi-language support: JavaScript, Python, SQL, CSS, HTML, Java, C++, and more
            - Custom formatting rules for indentation, spacing, and style preferences
            - Syntax highlighting with color-coded output for improved readability
            - Minify and beautify code with one click
            - Syntax error detection with line numbers and descriptions
            - Real-time preview as you type
            - Code comparison and diff viewer
            - Support for popular style guides (Airbnb, Google, Standard)
            - Comment preservation and formatting
            - Automatic code optimization suggestions
            """)
        elif "Utilities" in category:
            st.markdown("""
            **Essential Developer Utilities:**
            - Multiple hash algorithms: MD5, SHA-1, SHA-256, SHA-512, and more
            - Encode and decode support: Base64, URL encoding, HTML entities
            - File hashing for checksum verification and integrity
            - Secure client-side processing - no data sent to servers
            - API testing with custom headers, body, and authentication
            - Regular expression testing with pattern matching and groups
            - Diff checker for comparing text, code, and files
            - JSON and XML schema validation
            - Batch operations for processing multiple inputs
            - Export and download results
            """)