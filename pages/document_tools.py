import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word
from converters.excel_csv import convert_excel_to_csv, convert_csv_to_excel
from converters.html_markdown_to_pdf import convert_markdown_to_pdf, convert_html_to_pdf, convert_url_to_pdf

def render():
    """Render Document Tools page"""
    
    st.markdown("## Document Tools")
    st.markdown("Professional document format conversion")
    st.markdown("---")
    
    # Tool selection
    tool = st.selectbox(
        "Select Conversion Type",
        [
            "Word to PDF",
            "PDF to Word",
            "Excel to CSV",
            "CSV to Excel",
            "Markdown to PDF",
            "HTML to PDF"
        ]
    )
    
    st.markdown("")
    
    # Render selected tool
    if tool == "Word to PDF":
        render_word_to_pdf()
    elif tool == "PDF to Word":
        render_pdf_to_word()
    elif tool == "Excel to CSV":
        render_excel_to_csv()
    elif tool == "CSV to Excel":
        render_csv_to_excel()
    elif tool == "Markdown to PDF":
        render_markdown_to_pdf()
    elif tool == "HTML to PDF":
        render_html_to_pdf()

def render_word_to_pdf():
    """Word to PDF conversion interface"""
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>Word to PDF</h3>
                <p>
                    Convert Microsoft Word documents (.docx) to PDF format 
                    with precise formatting preservation.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Preserves formatting</li>
                    <li>High quality output</li>
                    <li>Fast processing</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload Word Document",
        type=["docx"],
        help="Supported: .docx"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("Convert to PDF", use_container_width=True):
                with st.spinner("Converting..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("Conversion completed")
                        
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
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>PDF to Word</h3>
                <p>
                    Convert PDF files to editable Microsoft Word documents 
                    while maintaining layout structure.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Editable output</li>
                    <li>Layout preserved</li>
                    <li>Text extraction</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type=["pdf"],
        help="Supported: .pdf"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("Convert to Word", use_container_width=True):
                with st.spinner("Processing..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("Conversion completed")
                        
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
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>Excel to CSV</h3>
                <p>
                    Convert Excel spreadsheets (.xlsx, .xls) to CSV format 
                    for universal compatibility.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Simple conversion</li>
                    <li>Data preserved</li>
                    <li>Universal format</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload Excel File",
        type=["xlsx", "xls"],
        help="Supported: .xlsx, .xls"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("Convert to CSV", use_container_width=True):
                with st.spinner("Converting..."):
                    csv_bytes = convert_excel_to_csv(uploaded_file)
                    
                    if csv_bytes:
                        st.success("Conversion completed")
                        
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
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>CSV to Excel</h3>
                <p>
                    Convert CSV files to Excel spreadsheet format 
                    with proper formatting.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Excel format</li>
                    <li>Data preserved</li>
                    <li>Easy to edit</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"],
        help="Supported: .csv"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("Convert to Excel", use_container_width=True):
                with st.spinner("Converting..."):
                    excel_bytes = convert_csv_to_excel(uploaded_file)
                    
                    if excel_bytes:
                        st.success("Conversion completed")
                        
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
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>Markdown to PDF</h3>
                <p>
                    Convert Markdown files to professionally formatted 
                    PDF documents.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Styled output</li>
                    <li>Professional look</li>
                    <li>Ready to share</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload Markdown File",
        type=["md", "markdown"],
        help="Supported: .md, .markdown"
    )
    
    if uploaded_file:
        st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
        st.markdown("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("Convert to PDF", use_container_width=True):
                with st.spinner("Converting..."):
                    pdf_bytes = convert_markdown_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("Conversion completed")
                        
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
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>HTML to PDF</h3>
                <p>
                    Convert HTML files or websites to PDF documents 
                    with CSS and layout preservation.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='info-box'>
                <ul>
                    <li>Layout preserved</li>
                    <li>CSS supported</li>
                    <li>Web to PDF</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Tab for URL or File upload
    tab1, tab2 = st.tabs(["Upload HTML File", "Website URL"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "Upload HTML File",
            type=["html", "htm"],
            help="Supported: .html, .htm",
            key="html_file"
        )
        
        if uploaded_file:
            st.markdown(f"<div class='success-msg'>File ready: {uploaded_file.name}</div>", unsafe_allow_html=True)
            st.markdown("")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_html"):
                    with st.spinner("Converting..."):
                        pdf_bytes = convert_html_to_pdf(uploaded_file)
                        
                        if pdf_bytes:
                            st.success("Conversion completed")
                            
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
            placeholder="Example: https://ilovepdf.com",
            help="Enter the website URL to convert to PDF"
        )
        
        if url_input:
            st.markdown(f"<div class='success-msg'>URL ready: {url_input}</div>", unsafe_allow_html=True)
            st.markdown("")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                if st.button("Convert to PDF", use_container_width=True, key="convert_url"):
                    with st.spinner("Converting website to PDF..."):
                        pdf_bytes = convert_url_to_pdf(url_input)
                        
                        if pdf_bytes:
                            st.success("Conversion completed")
                            
                            # Extract domain name for filename
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

def render_wip(tool_name):
    """Render Work In Progress page"""
    
    st.markdown(f"""
        <div class='wip-container'>
            <h2>{tool_name}</h2>
            <h3>In Development</h3>
            <p>This conversion tool is currently being developed.</p>
        </div>
    """, unsafe_allow_html=True)