import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word
from converters.excel_csv import convert_excel_to_csv, convert_csv_to_excel
from converters.html_markdown_to_pdf import convert_markdown_to_pdf, convert_html_to_pdf, convert_url_to_pdf

def render():
    """Render Document Tools page with ultra-modern UI"""
    
    # Page header with description
    st.markdown("""
        <div class='page-header'>
            <h1 class='page-title'>📄 Document Converter</h1>
            <p class='page-description'>
                Convert your documents between popular formats with precision and speed. 
                Perfect formatting preservation guaranteed.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Conversion selector with modern design
    col_left, col_center, col_right = st.columns([1, 8, 1])
    
    with col_center:
        st.markdown("<div class='conversion-panel'>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([5, 1, 5])
        
        with col1:
            from_format = st.selectbox(
                "📥 Convert from",
                ["Word (DOCX)", "PDF", "Excel (XLSX)", "CSV", "Markdown (MD)", "HTML"],
                key="from_format",
                help="Select the source file format"
            )
        
        with col2:
            st.markdown("""
                <div style='text-align: center; padding-top: 40px;'>
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2.5">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            to_options = get_conversion_options(from_format)
            to_format = st.selectbox(
                "📤 Convert to",
                to_options,
                key="to_format",
                help="Select the target file format"
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Render conversion interface based on selection
    if from_format == "Word (DOCX)" and to_format == "PDF":
        render_word_to_pdf()
    elif from_format == "PDF" and to_format == "Word (DOCX)":
        render_pdf_to_word()
    elif from_format == "Excel (XLSX)" and to_format == "CSV":
        render_excel_to_csv()
    elif from_format == "CSV" and to_format == "Excel (XLSX)":
        render_csv_to_excel()
    elif from_format == "Markdown (MD)" and to_format == "PDF":
        render_markdown_to_pdf()
    elif from_format == "HTML" and to_format == "PDF":
        render_html_to_pdf()
    
    # Enhanced features section
    st.markdown("""
        <div class='features-showcase-section'>
            <h2 style='text-align: center; margin-bottom: 3rem; font-size: 32px;'>Why Our Document Converter?</h2>
            <div class='feature-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        </svg>
                    </div>
                    <h4>Secure Processing</h4>
                    <p>Your files are processed securely with end-to-end encryption and automatically deleted after conversion</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                        </svg>
                    </div>
                    <h4>Perfect Quality</h4>
                    <p>Advanced conversion algorithms ensure the best possible output quality with formatting intact</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                        </svg>
                    </div>
                    <h4>Lightning Fast</h4>
                    <p>Cloud-powered processing means your documents convert in seconds, not minutes</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                        </svg>
                    </div>
                    <h4>Format Preservation</h4>
                    <p>Tables, images, fonts, and layouts are preserved perfectly across all conversions</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                            <polyline points="7 10 12 15 17 10"/>
                            <line x1="12" y1="15" x2="12" y2="3"/>
                        </svg>
                    </div>
                    <h4>Batch Support</h4>
                    <p>Convert multiple documents at once to save time on bulk conversions</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9302c" stroke-width="2">
                            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                        </svg>
                    </div>
                    <h4>100% Free</h4>
                    <p>No hidden costs, no subscriptions, no limits. Convert unlimited files completely free</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Popular conversions
    st.markdown("""
        <div class='popular-conversions'>
            <h3 style='text-align: center; margin-bottom: 2rem; color: #fff;'>Popular Document Conversions</h3>
            <div class='conversion-tags'>
                <span class='conversion-tag'>Word to PDF</span>
                <span class='conversion-tag'>PDF to Word</span>
                <span class='conversion-tag'>Excel to CSV</span>
                <span class='conversion-tag'>CSV to Excel</span>
                <span class='conversion-tag'>Markdown to PDF</span>
                <span class='conversion-tag'>HTML to PDF</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_conversion_options(from_format):
    """Get available conversion options based on source format"""
    options_map = {
        "Word (DOCX)": ["PDF"],
        "PDF": ["Word (DOCX)"],
        "Excel (XLSX)": ["CSV"],
        "CSV": ["Excel (XLSX)"],
        "Markdown (MD)": ["PDF"],
        "HTML": ["PDF"]
    }
    return options_map.get(from_format, [])

def render_word_to_pdf():
    """Word to PDF conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>📄</div>
                    <div>
                        <h3>Word to PDF Converter</h3>
                        <p class='tool-subtitle'>Convert .docx files to PDF format</p>
                    </div>
                </div>
                <p>
                    Transform your Microsoft Word documents into universally compatible PDF files. 
                    Our converter maintains all formatting, images, tables, and fonts with pixel-perfect precision.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>Preserves all formatting</li>
                    <li>Maintains document layout</li>
                    <li>High-quality output</li>
                    <li>Instant conversion</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📎 Drop your Word document here or click to browse",
        type=["docx"],
        help="Supported format: .docx",
        key="word_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"""
            <div class='file-ready'>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("🚀 Convert to PDF", use_container_width=True, key="convert_word"):
                with st.spinner("⚡ Converting your document..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✅ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="⬇️ Download PDF",
                            data=pdf_bytes,
                            file_name=output_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )

def render_pdf_to_word():
    """PDF to Word conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>📝</div>
                    <div>
                        <h3>PDF to Word Converter</h3>
                        <p class='tool-subtitle'>Convert PDF files to editable .docx</p>
                    </div>
                </div>
                <p>
                    Convert your PDF documents to fully editable Microsoft Word files. 
                    Perfect for editing, updating, and reusing content from PDF documents.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>Fully editable output</li>
                    <li>Text extraction</li>
                    <li>Layout preserved</li>
                    <li>Table recognition</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📎 Drop your PDF here or click to browse",
        type=["pdf"],
        help="Supported format: .pdf",
        key="pdf_to_word"
    )
    
    if uploaded_file:
        st.markdown(f"""
            <div class='file-ready'>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("🚀 Convert to Word", use_container_width=True, key="convert_pdf"):
                with st.spinner("⚡ Processing your PDF..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("✅ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.docx"
                        st.download_button(
                            label="⬇️ Download Word Document",
                            data=docx_bytes,
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

def render_excel_to_csv():
    """Excel to CSV conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>📊</div>
                    <div>
                        <h3>Excel to CSV Converter</h3>
                        <p class='tool-subtitle'>Convert .xlsx files to CSV format</p>
                    </div>
                </div>
                <p>
                    Export your Excel spreadsheets to CSV format for universal compatibility. 
                    Perfect for data analysis, imports, and cross-platform data sharing.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>Universal format</li>
                    <li>Data integrity</li>
                    <li>Lightweight files</li>
                    <li>Easy import/export</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📎 Drop your Excel file here or click to browse",
        type=["xlsx", "xls"],
        help="Supported formats: .xlsx, .xls",
        key="excel_to_csv"
    )
    
    if uploaded_file:
        st.markdown(f"""
            <div class='file-ready'>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("🚀 Convert to CSV", use_container_width=True, key="convert_excel"):
                with st.spinner("⚡ Converting..."):
                    csv_bytes = convert_excel_to_csv(uploaded_file)
                    
                    if csv_bytes:
                        st.success("✅ Conversion completed!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.csv"
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_bytes,
                            file_name=output_filename,
                            mime="text/csv",
                            use_container_width=True
                        )

def render_csv_to_excel():
    """CSV to Excel conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>📈</div>
                    <div>
                        <h3>CSV to Excel Converter</h3>
                        <p class='tool-subtitle'>Convert CSV to .xlsx format</p>
                    </div>
                </div>
                <p>
                    Transform CSV files into professional Excel spreadsheets with formatting. 
                    Perfect for data visualization, reporting, and advanced analysis.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>Professional format</li>
                    <li>Easy editing</li>
                    <li>Formula support</li>
                    <li>Clean layout</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📎 Drop your CSV file here or click to browse",
        type=["csv"],
        help="Supported format: .csv",
        key="csv_to_excel"
    )
    
    if uploaded_file:
        st.markdown(f"""
            <div class='file-ready'>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("🚀 Convert to Excel", use_container_width=True, key="convert_csv"):
                with st.spinner("⚡ Converting..."):
                    excel_bytes = convert_csv_to_excel(uploaded_file)
                    
                    if excel_bytes:
                        st.success("✅ Conversion completed!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.xlsx"
                        st.download_button(
                            label="⬇️ Download Excel",
                            data=excel_bytes,
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.document",
                            use_container_width=True
                        )

def render_markdown_to_pdf():
    """Markdown to PDF conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>📋</div>
                    <div>
                        <h3>Markdown to PDF Converter</h3>
                        <p class='tool-subtitle'>Convert .md files to PDF</p>
                    </div>
                </div>
                <p>
                    Transform Markdown documents into beautifully formatted PDFs. 
                    Perfect for documentation, README files, and technical writing.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>GitHub-style rendering</li>
                    <li>Code highlighting</li>
                    <li>Table support</li>
                    <li>Professional output</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📎 Drop your Markdown file here or click to browse",
        type=["md", "markdown"],
        help="Supported formats: .md, .markdown",
        key="md_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"""
            <div class='file-ready'>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("🚀 Convert to PDF", use_container_width=True, key="convert_md"):
                with st.spinner("⚡ Converting..."):
                    pdf_bytes = convert_markdown_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✅ Conversion completed!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="⬇️ Download PDF",
                            data=pdf_bytes,
                            file_name=output_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )

def render_html_to_pdf():
    """HTML/URL to PDF conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <div class='tool-header'>
                    <div class='tool-icon'>🌐</div>
                    <div>
                        <h3>HTML/Web to PDF Converter</h3>
                        <p class='tool-subtitle'>Convert HTML files or websites to PDF</p>
                    </div>
                </div>
                <p>
                    Convert HTML documents or entire websites into PDF files. 
                    Perfect for archiving web pages, creating reports, and saving online content.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>✨ Features</h4>
                <ul>
                    <li>CSS preserved</li>
                    <li>Layout intact</li>
                    <li>URL support</li>
                    <li>High fidelity</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📄 Upload HTML File", "🌐 Enter Website URL"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "📎 Drop your HTML file here or click to browse",
            type=["html", "htm"],
            help="Supported formats: .html, .htm",
            key="html_file"
        )
        
        if uploaded_file:
            st.markdown(f"""
                <div class='file-ready'>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    <span>File ready: <strong>{uploaded_file.name}</strong> ({uploaded_file.size / 1024:.1f} KB)</span>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("🚀 Convert to PDF", use_container_width=True, key="convert_html"):
                    with st.spinner("⚡ Converting..."):
                        pdf_bytes = convert_html_to_pdf(uploaded_file)
                        
                        if pdf_bytes:
                            st.success("✅ Conversion completed!")
                            
                            output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                            st.download_button(
                                label="⬇️ Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )
    
    with tab2:
        url_input = st.text_input(
            "🔗 Website URL",
            placeholder="https://example.com",
            help="Enter the complete URL including https://",
            key="url_input"
        )
        
        if url_input:
            st.markdown(f"""
                <div class='file-ready'>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5cb85c" stroke-width="2.5">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    <span>URL ready: <strong>{url_input}</strong></span>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("🚀 Convert to PDF", use_container_width=True, key="convert_url"):
                    with st.spinner("⚡ Converting website to PDF..."):
                        pdf_bytes = convert_url_to_pdf(url_input)
                        
                        if pdf_bytes:
                            st.success("✅ Conversion completed!")
                            
                            from urllib.parse import urlparse
                            domain = urlparse(url_input).netloc or "website"
                            output_filename = f"{domain}.pdf"
                            
                            st.download_button(
                                label="⬇️ Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )