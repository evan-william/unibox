from pdf2docx import Converter
import os
import streamlit as st

def convert_pdf_to_word(pdf_file):
    """
    Convert PDF to Word document
    Uses pdf2docx library for accurate conversion
    """
    try:
        # Save PDF temporarily
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.read())
        
        # Convert PDF to DOCX
        cv = Converter("temp.pdf")
        cv.convert("temp.docx", start=0, end=None)
        cv.close()
        
        # Read converted DOCX
        with open("temp.docx", "rb") as f:
            docx_data = f.read()
        
        # Cleanup temporary files
        try:
            os.remove("temp.pdf")
            os.remove("temp.docx")
        except:
            pass
            
        return docx_data
        
    except Exception as e:
        st.error(f"❌ Conversion failed: {str(e)}")
        # Cleanup on error
        try:
            if os.path.exists("temp.pdf"):
                os.remove("temp.pdf")
            if os.path.exists("temp.docx"):
                os.remove("temp.docx")
        except:
            pass
        return None