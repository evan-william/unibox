import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word
from converters.excel_csv import convert_excel_to_csv, convert_csv_to_excel
from converters.html_markdown_to_pdf import convert_markdown_to_pdf, convert_html_to_pdf, convert_url_to_pdf

def render():
    """Render Document Tools page with CloudConvert-style UI"""
    
    # Hero Section
    st.markdown("""
        <div class='hero-section'>
            <h1 class='hero-title'>Document Converter</h1>
            <p class='hero-subtitle'>
                Convert between popular document formats with precision.
                Support for PDF, Word, Excel, CSV, Markdown and HTML files
                with advanced conversion technology.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Tool selection - simpler approach
    st.markdown("### Select Conversion Type")
    
    conversion_type = st.selectbox(
        "Choose conversion",
        [
            "Word to PDF",
            "PDF to Word",
            "Excel to CSV",
            "CSV to Excel",
            "Markdown to PDF",
            "HTML to PDF"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("")
    
    # Render appropriate converter based on selection
    if conversion_type == "Word to PDF":
        render_word_to_pdf()
    elif conversion_type == "PDF to Word":
        render_pdf_to_word()
    elif conversion_type == "Excel to CSV":
        render_excel_to_csv()
    elif conversion_type == "CSV to Excel":
        render_csv_to_excel()
    elif conversion_type == "Markdown to PDF":
        render_markdown_to_pdf()
    elif conversion_type == "HTML to PDF":
        render_html_to_pdf()

def get_conversion_options(from_format):
    """Get available conversion formats based on source format"""
    conversions = {
        "Word (DOCX)": ["PDF"],
        "PDF": ["Word (DOCX)"],
        "Excel (XLSX)": ["CSV"],
        "CSV": ["Excel (XLSX)"],
        "Markdown (MD)": ["PDF"],
        "HTML": ["PDF"]
    }
    return conversions.get(from_format, ["PDF"])

def render_word_to_pdf():
    """Word to PDF conversion interface"""
    
    uploaded_file = st.file_uploader(
        "📄 Select Word Document",
        type=["docx"],
        help="Upload a .docx file to convert to PDF"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        # Options section
        with st.expander("⚙️ Conversion Options"):
            st.info("Word to PDF conversion preserves all formatting, fonts, and layout.")
        
        st.markdown("")
        
        # Convert button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Convert to PDF", use_container_width=True, type="primary"):
                with st.spinner("Converting document..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="📥 Download PDF",
                            data=pdf_bytes,
                            file_name=output_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )
    
    # Format info
    render_format_info("Word (DOCX)", "PDF")

def render_pdf_to_word():
    """PDF to Word conversion interface"""
    
    uploaded_file = st.file_uploader(
        "📄 Select PDF Document",
        type=["pdf"],
        help="Upload a .pdf file to convert to Word"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        with st.expander("⚙️ Conversion Options"):
            st.info("PDF to Word conversion extracts text and preserves layout structure.")
        
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Convert to Word", use_container_width=True, type="primary"):
                with st.spinner("Processing document..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.docx"
                        st.download_button(
                            label="📥 Download Word Document",
                            data=docx_bytes,
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )
    
    render_format_info("PDF", "Word (DOCX)")

def render_excel_to_csv():
    """Excel to CSV conversion interface"""
    
    uploaded_file = st.file_uploader(
        "📊 Select Excel File",
        type=["xlsx", "xls"],
        help="Upload an Excel file to convert to CSV"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        with st.expander("⚙️ Conversion Options"):
            st.info("Excel to CSV conversion extracts data from the first sheet by default.")
        
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Convert to CSV", use_container_width=True, type="primary"):
                with st.spinner("Converting spreadsheet..."):
                    csv_bytes = convert_excel_to_csv(uploaded_file)
                    
                    if csv_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.csv"
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv_bytes,
                            file_name=output_filename,
                            mime="text/csv",
                            use_container_width=True
                        )
    
    render_format_info("Excel (XLSX)", "CSV")

def render_csv_to_excel():
    """CSV to Excel conversion interface"""
    
    uploaded_file = st.file_uploader(
        "📊 Select CSV File",
        type=["csv"],
        help="Upload a CSV file to convert to Excel"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        with st.expander("⚙️ Conversion Options"):
            st.info("CSV to Excel conversion creates a formatted spreadsheet with proper data types.")
        
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Convert to Excel", use_container_width=True, type="primary"):
                with st.spinner("Creating spreadsheet..."):
                    excel_bytes = convert_csv_to_excel(uploaded_file)
                    
                    if excel_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.xlsx"
                        st.download_button(
                            label="📥 Download Excel",
                            data=excel_bytes,
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.document",
                            use_container_width=True
                        )
    
    render_format_info("CSV", "Excel (XLSX)")

def render_markdown_to_pdf():
    """Markdown to PDF conversion interface"""
    
    uploaded_file = st.file_uploader(
        "📝 Select Markdown File",
        type=["md", "markdown"],
        help="Upload a .md file to convert to PDF"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        
        with st.expander("⚙️ Conversion Options"):
            st.info("Markdown to PDF conversion includes GitHub-style formatting with syntax highlighting.")
        
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Convert to PDF", use_container_width=True, type="primary"):
                with st.spinner("Rendering markdown..."):
                    pdf_bytes = convert_markdown_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✓ Conversion completed successfully!")
                        
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                        st.download_button(
                            label="📥 Download PDF",
                            data=pdf_bytes,
                            file_name=output_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )
    
    render_format_info("Markdown (MD)", "PDF")

def render_html_to_pdf():
    """HTML/URL to PDF conversion interface"""
    
    tab1, tab2 = st.tabs(["📄 Upload HTML File", "🌐 Website URL"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "Select HTML File",
            type=["html", "htm"],
            help="Upload an HTML file to convert to PDF",
            key="html_file"
        )
        
        if uploaded_file:
            st.markdown(f"<div class='success-msg'>✓ File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
            
            with st.expander("⚙️ Conversion Options"):
                st.info("HTML to PDF conversion preserves CSS styling and layout.")
            
            st.markdown("")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔄 Convert to PDF", use_container_width=True, key="convert_html", type="primary"):
                    with st.spinner("Converting HTML..."):
                        pdf_bytes = convert_html_to_pdf(uploaded_file)
                        
                        if pdf_bytes:
                            st.success("✓ Conversion completed successfully!")
                            
                            output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf"
                            st.download_button(
                                label="📥 Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )
    
    with tab2:
        url_input = st.text_input(
            "🌐 Website URL",
            placeholder="https://example.com",
            help="Enter a website URL to convert to PDF"
        )
        
        if url_input:
            st.markdown(f"<div class='success-msg'>✓ URL ready: {url_input}</div>", unsafe_allow_html=True)
            
            with st.expander("⚙️ Conversion Options"):
                st.info("Website to PDF conversion captures the full page with JavaScript rendering.")
            
            st.markdown("")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔄 Convert to PDF", use_container_width=True, key="convert_url", type="primary"):
                    with st.spinner("Capturing website..."):
                        pdf_bytes = convert_url_to_pdf(url_input)
                        
                        if pdf_bytes:
                            st.success("✓ Conversion completed successfully!")
                            
                            from urllib.parse import urlparse
                            domain = urlparse(url_input).netloc or "website"
                            output_filename = f"{domain}.pdf"
                            
                            st.download_button(
                                label="📥 Download PDF",
                                data=pdf_bytes,
                                file_name=output_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )
    
    render_format_info("HTML", "PDF")

def render_format_info(from_format, to_format):
    """Render format information cards"""
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    format_descriptions = {
        "Word (DOCX)": "Microsoft Word document format with rich formatting, images, and layout control.",
        "PDF": "Portable Document Format - universal, read-only document format that preserves layout across all devices.",
        "Excel (XLSX)": "Microsoft Excel spreadsheet format with support for formulas, charts, and multiple sheets.",
        "CSV": "Comma-Separated Values - simple text format for tabular data, universally compatible.",
        "Markdown (MD)": "Plain text format with simple syntax for formatting, widely used for documentation.",
        "HTML": "HyperText Markup Language - standard web page format with styling and scripting."
    }
    
    with col1:
        st.markdown(f"""
            <div class='format-info'>
                <h4>📄 {from_format}</h4>
                <p>{format_descriptions.get(from_format, "Document format")}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class='format-info'>
                <h4>📄 {to_format}</h4>
                <p>{format_descriptions.get(to_format, "Document format")}</p>
            </div>
        """, unsafe_allow_html=True)