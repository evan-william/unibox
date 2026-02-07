import streamlit as st
from converters.word_to_pdf import convert_word_to_pdf
from converters.pdf_to_word import convert_pdf_to_word

def render():
    """Render Document Tools page"""
    
    st.markdown("### 📄 Document Conversion Tools")
    st.markdown("Convert between different document formats with ease")
    st.markdown("---")
    
    # Tool selection
    tool = st.selectbox(
        "Select Tool",
        [
            "Word to PDF",
            "PDF to Word",
            "Excel to CSV",
            "CSV to Excel",
            "Markdown to PDF",
            "HTML to PDF"
        ]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render selected tool
    if tool == "Word to PDF":
        render_word_to_pdf()
    elif tool == "PDF to Word":
        render_pdf_to_word()
    else:
        render_wip(tool)

def render_word_to_pdf():
    """Word to PDF conversion interface"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='tool-card'>
                <h3>📄 ➜ 📕 Word to PDF</h3>
                <p style='color: #666;'>
                    Convert your Microsoft Word documents (.docx) to PDF format 
                    with high precision formatting preservation.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.info("✓ Preserves formatting\n\n✓ High quality output\n\n✓ Fast conversion")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload Word Document",
        type=["docx"],
        help="Supported format: .docx"
    )
    
    if uploaded_file:
        st.success(f"✓ File loaded: **{uploaded_file.name}**")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Convert to PDF", use_container_width=True):
                with st.spinner("⚙️ Converting with high precision..."):
                    pdf_bytes = convert_word_to_pdf(uploaded_file)
                    
                    if pdf_bytes:
                        st.success("✅ Conversion completed successfully!")
                        
                        # Download button
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
                <h3>📕 ➜ 📄 PDF to Word</h3>
                <p style='color: #666;'>
                    Convert PDF files to editable Microsoft Word documents (.docx) 
                    while maintaining layout and formatting.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.info("✓ Editable output\n\n✓ Layout preserved\n\n✓ Text extraction")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type=["pdf"],
        help="Supported format: .pdf"
    )
    
    if uploaded_file:
        st.success(f"✓ File loaded: **{uploaded_file.name}**")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🚀 Convert to Word", use_container_width=True):
                with st.spinner("⚙️ Processing PDF..."):
                    docx_bytes = convert_pdf_to_word(uploaded_file)
                    
                    if docx_bytes:
                        st.success("✅ Conversion completed successfully!")
                        
                        # Download button
                        output_filename = f"{uploaded_file.name.rsplit('.', 1)[0]}.docx"
                        st.download_button(
                            label="⬇️ Download Word Document",
                            data=docx_bytes,
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

def render_wip(tool_name):
    """Render Work In Progress page"""
    
    st.markdown(f"""
        <div class='wip-container'>
            <h2>🚧 {tool_name}</h2>
            <h3>Work In Progress</h3>
            <p>This feature is currently under development.</p>
            <p style='margin-top: 20px; font-size: 0.9em;'>
                Check back soon for updates!
            </p>
        </div>
    """, unsafe_allow_html=True)