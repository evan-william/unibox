import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word
from converters.excel_csv import convert_excel_to_csv, convert_csv_to_excel
from converters.html_markdown_to_pdf import convert_markdown_to_pdf, convert_html_to_pdf, convert_url_to_pdf

def render():
    """Render Document Tools page with modern professional UI"""
    
    # Page header
    st.markdown("<h2 style='margin-bottom: 1rem; text-align: center; font-size: 42px; font-weight: 800;'>Document Converter</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 17px; margin-bottom: 3rem;'>Convert your documents between different formats with high quality and precision</p>", unsafe_allow_html=True)
    
    # Conversion selector
    col_left, col_center, col_right = st.columns([1, 10, 1])
    
    with col_center:
        col1, col2, col3 = st.columns([5, 1, 5])
        
        with col1:
            from_format = st.selectbox(
                "Convert from",
                ["Word (DOCX)", "PDF", "Excel (XLSX)", "CSV", "Markdown (MD)", "HTML"],
                key="from_format"
            )
        
        with col2:
            st.markdown("<div style='text-align: center; padding-top: 32px; font-size: 28px; color: #ff4757; font-weight: bold;'>→</div>", unsafe_allow_html=True)
        
        with col3:
            to_options = get_conversion_options(from_format)
            to_format = st.selectbox(
                "Convert to",
                to_options,
                key="to_format"
            )
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # Render conversion interface
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
    
    # Features section
    st.markdown("""
        <div class='features-section'>
            <div class='features-header'>
                <h2>Why Choose UniBox for Documents?</h2>
                <p>Professional-grade document conversion with advanced features</p>
            </div>
            <div class='feature-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                        </svg>
                    </div>
                    <h4>Secure Processing</h4>
                    <p>Your files are processed securely with end-to-end encryption and never stored on our servers</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                        </svg>
                    </div>
                    <h4>High Quality Output</h4>
                    <p>Advanced conversion algorithms ensure the best possible output quality with preserved formatting</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 16 14"/>
                        </svg>
                    </div>
                    <h4>Lightning Fast</h4>
                    <p>Experience blazing-fast conversion speeds without any sign-up or payment required</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                        </svg>
                    </div>
                    <h4>Format Preservation</h4>
                    <p>Maintain document structure, fonts, images, and layouts across different formats</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>
                    </div>
                    <h4>Batch Processing</h4>
                    <p>Convert multiple documents at once to save time and streamline your workflow</p>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff4757" stroke-width="2">
                            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                            <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                            <line x1="12" y1="22.08" x2="12" y2="12"/>
                        </svg>
                    </div>
                    <h4>No Software Needed</h4>
                    <p>100% online tool - no installation, registration, or downloads required to get started</p>
                </div>
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
                <h3>Word to PDF Converter</h3>
                <p>
                    Convert Microsoft Word documents (.docx) to PDF format 
                    with precise formatting and layout preservation. Perfect for sharing 
                    professional documents that look exactly as intended.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>Preserves formatting</li>
                    <li>Maintains layout</li>
                    <li>High quality output</li>
                    <li>Fast processing</li>
                    <li>Professional results</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Word document",
        type=["docx"],
        help="Drag and drop your .docx file here or click to browse",
        key="word_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to PDF", use_container_width=True, key="convert_word"):
                with st.spinner("Converting your document..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="Download PDF",
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
                <h3>PDF to Word Converter</h3>
                <p>
                    Convert PDF files to editable Microsoft Word documents 
                    while maintaining structure and formatting. Extract text, images, 
                    and tables with high accuracy for easy editing.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>Editable output</li>
                    <li>Text extraction</li>
                    <li>Layout preserved</li>
                    <li>Table support</li>
                    <li>Image retention</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your PDF file",
        type=["pdf"],
        help="Drag and drop your .pdf file here or click to browse",
        key="pdf_to_word"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to Word", use_container_width=True, key="convert_pdf"):
                with st.spinner("Processing your PDF..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.docx"
                        st.download_button(
                            label="Download Word Document",
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
                <h3>Excel to CSV Converter</h3>
                <p>
                    Convert Excel spreadsheets to CSV format for universal 
                    compatibility and easy data sharing. Perfect for importing 
                    data into databases or other applications.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>Universal format</li>
                    <li>Data preserved</li>
                    <li>Lightweight output</li>
                    <li>Easy sharing</li>
                    <li>Database ready</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Excel file",
        type=["xlsx", "xls"],
        help="Drag and drop your Excel file here or click to browse",
        key="excel_to_csv"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to CSV", use_container_width=True, key="convert_excel"):
                with st.spinner("Converting..."):
                    csv_bytes = convert_excel_to_csv(uploaded_file)
                    
                    if csv_bytes:
                        st.success("Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.csv"
                        st.download_button(
                            label="Download CSV",
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
                <h3>CSV to Excel Converter</h3>
                <p>
                    Convert CSV files to Excel format with proper formatting 
                    and improved readability. Add formulas, charts, and 
                    professional styling to your data.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>Professional format</li>
                    <li>Easy to edit</li>
                    <li>Formula support</li>
                    <li>Clean layout</li>
                    <li>Chart ready</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"],
        help="Drag and drop your .csv file here or click to browse",
        key="csv_to_excel"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to Excel", use_container_width=True, key="convert_csv"):
                with st.spinner("Converting..."):
                    excel_bytes = convert_csv_to_excel(uploaded_file)
                    
                    if excel_bytes:
                        st.success("Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.xlsx"
                        st.download_button(
                            label="Download Excel",
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
                <h3>Markdown to PDF Converter</h3>
                <p>
                    Convert Markdown files to professionally formatted 
                    PDF documents with beautiful styling, syntax highlighting, 
                    and support for tables and code blocks.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>Styled output</li>
                    <li>Code highlighting</li>
                    <li>Table support</li>
                    <li>Professional look</li>
                    <li>GitHub style</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Markdown file",
        type=["md", "markdown"],
        help="Drag and drop your .md file here or click to browse",
        key="md_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to PDF", use_container_width=True, key="convert_md"):
                with st.spinner("Converting..."):
                    pdf_bytes = convert_markdown_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="Download PDF",
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
                <h3>HTML to PDF Converter</h3>
                <p>
                    Convert HTML files or websites to PDF documents 
                    with full CSS support and layout preservation. Perfect for 
                    archiving web pages or creating offline documentation.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Key Features</h4>
                <ul>
                    <li>CSS preserved</li>
                    <li>Layout intact</li>
                    <li>Website support</li>
                    <li>High fidelity</li>
                    <li>JavaScript render</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Upload HTML File", "Website URL"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "Upload your HTML file",
            type=["html", "htm"],
            help="Drag and drop your .html file here or click to browse",
            key="html_file"
        )
        
        if uploaded_file:
            st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_html"):
                    with st.spinner("Converting..."):
                        pdf_bytes = convert_html_to_pdf(uploaded_file)
                        
                        if pdf_bytes:
                            st.success("Conversion completed successfully!")
                            
                            output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                            st.download_button(
                                label="Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )
    
    with tab2:
        url_input = st.text_input(
            "Website URL",
            placeholder="https://example.com",
            help="Enter the complete URL including https://",
            key="url_input"
        )
        
        if url_input:
            st.markdown(f"<div class='success-msg'>URL ready: {url_input}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_url"):
                    with st.spinner("Converting website to PDF..."):
                        pdf_bytes = convert_url_to_pdf(url_input)
                        
                        if pdf_bytes:
                            st.success("Conversion completed successfully!")
                            
                            from urllib.parse import urlparse
                            domain = urlparse(url_input).netloc or "website"
                            output_filename = f"{domain}.pdf"
                            
                            st.download_button(
                                label="Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )