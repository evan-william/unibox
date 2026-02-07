import streamlit as st
from pdf2docx import Converter
from docx import Document
from fpdf import FPDF
import io

# HALAMAN CONFIGURE
st.set_page_config(page_title="Universal Converter", page_icon="🔄", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .wip-container { text-align: center; padding: 50px; color: #666; }
    </style>
    """, unsafe_content_type=True)

# --- SIDEBAR NAV ---
st.sidebar.title("📌 Navigation")
st.sidebar.info("Select a tool category below:")

# MAIN NAV
category = st.sidebar.selectbox("Category", ["Document Tools", "Media Tools", "Dev & Data Tools"])

# Sub Navigation ---Category
if category == "Document Tools":
    tool = st.sidebar.selectbox("Select Tool", ["Word to PDF", "PDF to Word", "CSV to Excel (WIP)"])
elif category == "Media Tools":
    tool = st.sidebar.selectbox("Select Tool", ["PNG to JPG (WIP)", "MP3 to WAV (WIP)", "Video to GIF (WIP)"])
else:
    # WIP 3rd IDEA
    tool = st.sidebar.selectbox("Select Tool", ["JSON to CSV (WIP)", "Humanize AI (WIP)", "Code Formatter (WIP)"])

# --- LOGIC HANDLING ---

def word_to_pdf(docx_file):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, txt=para.text)
    
    # SAVE TO BUFFER, bisa didownlaod dari ram
    pdf_output = pdf.output(dest='S').encode('latin-1')
    return pdf_output

def pdf_to_word(pdf_file):
    # SAVE PDF KE DISK
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())
    
    cv = Converter("temp.pdf")
    cv.convert("temp.docx", start=0, end=None)
    cv.close()
    
    with open("temp.docx", "rb") as f:
        docx_data = f.read()
    return docx_data

# --- UI DISPLAY ---

st.title(f"🛠 {tool}")

if "WIP" in tool:
    st.markdown("""
        <div class="wip-container">
            <h2>🚧 Work In Progress</h2>
            <p>Fitur ini sedang dalam tahap pengembangan oleh Evan William.</p>
        </div>
    """, unsafe_content_type=True)

elif tool == "Word to PDF":
    st.write("Convert your .docx files to PDF format instantly.")
    uploaded_file = st.file_uploader("Upload Word Document", type=["docx"])
    
    if uploaded_file:
        if st.button("Convert Now"):
            with st.spinner("Converting..."):
                pdf_bytes = word_to_pdf(uploaded_file)
                st.success("Conversion Successful!")
                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_bytes,
                    file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}.pdf",
                    mime="application/pdf"
                )

elif tool == "PDF to Word":
    st.write("Convert your PDF files back to editable Word documents.")
    uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])
    
    if uploaded_file:
        if st.button("Convert Now"):
            with st.spinner("Processing PDF..."):
                docx_bytes = pdf_to_word(uploaded_file)
                st.success("Conversion Successful!")
                st.download_button(
                    label="📥 Download Word (.docx)",
                    data=docx_bytes,
                    file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )