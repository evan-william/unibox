import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word
from converters.excel_csv import convert_excel_to_csv, convert_csv_to_excel
from converters.html_markdown_to_pdf import convert_markdown_to_pdf, convert_html_to_pdf, convert_url_to_pdf

def render():
    """Render Document Tools page with modern UI"""
    
    # Page title
    st.markdown("<h2 style='margin-bottom: 1rem;'>Document Converter</h2>", unsafe_allow_html=True)
    
    # Conversion selector
    col1, col2, col3 = st.columns([5, 1, 5])
    
    with col1:
        from_format = st.selectbox(
            "Convert from",
            ["Word (DOCX)", "PDF", "Excel (XLSX)", "CSV", "Markdown (MD)", "HTML"],
            key="from_format"
        )
    
    with col2:
        st.markdown("<div style='text-align: center; padding-top: 32px; font-size: 24px; color: #666;'>→</div>", unsafe_allow_html=True)
    
    with col3:
        # Dynamic "to" options based on "from" selection
        to_options = get_conversion_options(from_format)
        to_format = st.selectbox(
            "Convert to",
            to_options,
            key="to_format"
        )
    
    st.markdown("<hr style='border: none; border-top: 1px solid #4d4d4d; margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Render conversion interface
    conversion_key = f"{from_format}_{to_format}"
    
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
        <div class='feature-grid'>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    </svg>
                </div>
                <h4>Secure Processing</h4>
                <p>Your files are processed securely and never stored on our servers</p>
            </div>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                    </svg>
                </div>
                <h4>High Quality</h4>
                <p>Advanced conversion algorithms ensure the best possible output quality</p>
            </div>
            <div class='feature-card'>
                <div class='feature-icon'>
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                    </svg>
                </div>
                <h4>Fast & Free</h4>
                <p>Lightning-fast conversion with no sign-up or payment required</p>
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
                <h3>Word to PDF</h3>
                <p>
                    Convert Microsoft Word documents (.docx) to PDF format 
                    with precise formatting and layout preservation.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>Preserves formatting</li>
                    <li>Maintains layout</li>
                    <li>High quality output</li>
                    <li>Fast processing</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Word document",
        type=["docx"],
        help="Drag and drop your .docx file here",
        key="word_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to PDF", use_container_width=True, key="convert_word"):
                with st.spinner("Converting your document..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
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
                <h3>PDF to Word</h3>
                <p>
                    Convert PDF files to editable Microsoft Word documents 
                    while maintaining structure and formatting.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>Editable output</li>
                    <li>Text extraction</li>
                    <li>Layout preserved</li>
                    <li>Table support</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your PDF file",
        type=["pdf"],
        help="Drag and drop your .pdf file here",
        key="pdf_to_word"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to Word", use_container_width=True, key="convert_pdf"):
                with st.spinner("Processing your PDF..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
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
                <h3>Excel to CSV</h3>
                <p>
                    Convert Excel spreadsheets to CSV format for universal 
                    compatibility and easy data sharing.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>Universal format</li>
                    <li>Data preserved</li>
                    <li>Lightweight output</li>
                    <li>Easy sharing</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Excel file",
        type=["xlsx", "xls"],
        help="Drag and drop your Excel file here",
        key="excel_to_csv"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to CSV", use_container_width=True, key="convert_excel"):
                with st.spinner("Converting..."):
                    csv_bytes = convert_excel_to_csv(uploaded_file)
                    
                    if csv_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
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
                <h3>CSV to Excel</h3>
                <p>
                    Convert CSV files to Excel format with proper formatting 
                    and improved readability.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>Professional format</li>
                    <li>Easy to edit</li>
                    <li>Formula support</li>
                    <li>Clean layout</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"],
        help="Drag and drop your .csv file here",
        key="csv_to_excel"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to Excel", use_container_width=True, key="convert_csv"):
                with st.spinner("Converting..."):
                    excel_bytes = convert_csv_to_excel(uploaded_file)
                    
                    if excel_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
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
                <h3>Markdown to PDF</h3>
                <p>
                    Convert Markdown files to professionally formatted 
                    PDF documents with beautiful styling.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>Styled output</li>
                    <li>Code highlighting</li>
                    <li>Table support</li>
                    <li>Professional look</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload your Markdown file",
        type=["md", "markdown"],
        help="Drag and drop your .md file here",
        key="md_to_pdf"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            if st.button("Convert to PDF", use_container_width=True, key="convert_md"):
                with st.spinner("Converting..."):
                    pdf_bytes = convert_markdown_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
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
                <h3>HTML to PDF</h3>
                <p>
                    Convert HTML files or websites to PDF documents 
                    with full CSS and layout support.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <h4>Features</h4>
                <ul>
                    <li>CSS preserved</li>
                    <li>Layout intact</li>
                    <li>Website support</li>
                    <li>High fidelity</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📄 Upload HTML File", "🌐 Website URL"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "Upload your HTML file",
            type=["html", "htm"],
            help="Drag and drop your .html file here",
            key="html_file"
        )
        
        if uploaded_file:
            st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_html"):
                    with st.spinner("Converting..."):
                        pdf_bytes = convert_html_to_pdf(uploaded_file)
                        
                        if pdf_bytes:
                            st.success("✓ Conversion completed successfully!")
                            
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
            st.markdown(f"<div class='success-msg'>✓ URL ready: {url_input}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 3, 2])
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_url"):
                    with st.spinner("Converting website to PDF..."):
                        pdf_bytes = convert_url_to_pdf(url_input)
                        
                        if pdf_bytes:
                            st.success("✓ Conversion completed successfully!")
                            
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