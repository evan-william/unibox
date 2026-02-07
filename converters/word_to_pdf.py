import subprocess
import os
import platform
import streamlit as st

def convert_word_to_pdf(docx_file):
    """
    Convert Word document to PDF
    Compatible with both Windows and Linux (Streamlit Cloud)
    """
    # Save uploaded file temporarily
    with open("temp_input.docx", "wb") as f:
        f.write(docx_file.getbuffer())

    try:
        # Check platform and use appropriate conversion method
        if platform.system() == "Windows":
            # Windows: Use docx2pdf (requires MS Word)
            from docx2pdf import convert
            convert("temp_input.docx", "temp_input.pdf")
        else:
            # Linux (Streamlit Cloud): Use LibreOffice
            subprocess.run([
                'lowriter', 
                '--headless', 
                '--convert-to', 'pdf', 
                'temp_input.docx'
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Read converted PDF
        with open("temp_input.pdf", "rb") as f:
            pdf_data = f.read()
            
        # Cleanup temporary files
        try:
            os.remove("temp_input.docx")
            os.remove("temp_input.pdf")
        except:
            pass
            
        return pdf_data

    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        # Cleanup on error
        try:
            os.remove("temp_input.docx")
            if os.path.exists("temp_input.pdf"):
                os.remove("temp_input.pdf")
        except:
            pass
        return None