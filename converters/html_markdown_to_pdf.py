import pdfkit
import markdown2
import os
import streamlit as st
import requests
from io import BytesIO

def convert_markdown_to_pdf(md_file):
    """
    Convert Markdown to PDF
    """
    try:
        # Read markdown content
        md_content = md_file.read().decode('utf-8')
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(md_content)
        
        # Add basic CSS styling
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 40px auto;
                    padding: 20px;
                }}
                h1, h2, h3 {{ color: #333; }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Save HTML temporarily
        with open("temp_md.html", "w", encoding='utf-8') as f:
            f.write(html_with_style)
        
        # Convert HTML to PDF using wkhtmltopdf
        try:
            pdfkit.from_file("temp_md.html", "temp_md.pdf")
        except:
            # Fallback for systems without wkhtmltopdf
            from weasyprint import HTML
            HTML(string=html_with_style).write_pdf("temp_md.pdf")
        
        # Read PDF
        with open("temp_md.pdf", "rb") as f:
            pdf_data = f.read()
        
        # Cleanup
        try:
            os.remove("temp_md.html")
            os.remove("temp_md.pdf")
        except:
            pass
        
        return pdf_data
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        # Cleanup on error
        try:
            if os.path.exists("temp_md.html"):
                os.remove("temp_md.html")
            if os.path.exists("temp_md.pdf"):
                os.remove("temp_md.pdf")
        except:
            pass
        return None

def convert_html_to_pdf(html_file):
    """
    Convert HTML file to PDF
    """
    try:
        # Read HTML content
        html_content = html_file.read().decode('utf-8')
        
        # Save HTML temporarily
        with open("temp.html", "w", encoding='utf-8') as f:
            f.write(html_content)
        
        # Convert HTML to PDF using wkhtmltopdf
        try:
            pdfkit.from_file("temp.html", "temp.pdf")
        except:
            # Fallback for systems without wkhtmltopdf
            from weasyprint import HTML
            HTML(string=html_content).write_pdf("temp.pdf")
        
        # Read PDF
        with open("temp.pdf", "rb") as f:
            pdf_data = f.read()
        
        # Cleanup
        try:
            os.remove("temp.html")
            os.remove("temp.pdf")
        except:
            pass
        
        return pdf_data
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        # Cleanup on error
        try:
            if os.path.exists("temp.html"):
                os.remove("temp.html")
            if os.path.exists("temp.pdf"):
                os.remove("temp.pdf")
        except:
            pass
        return None

def convert_url_to_pdf(url):
    """
    Convert website URL to PDF
    """
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Configure pdfkit options for better rendering
        options = {
            'enable-local-file-access': None,
            'enable-javascript': None,
            'javascript-delay': 1000,
            'no-stop-slow-scripts': None,
            'load-error-handling': 'ignore',
            'load-media-error-handling': 'ignore',
            'encoding': 'UTF-8',
        }
        
        # Convert URL to PDF using wkhtmltopdf
        try:
            pdfkit.from_url(url, "temp_url.pdf", options=options)
        except:
            # Fallback: fetch HTML and use weasyprint
            st.info("Using alternative rendering method...")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            from weasyprint import HTML
            HTML(string=response.text, base_url=url).write_pdf("temp_url.pdf")
        
        # Read PDF
        with open("temp_url.pdf", "rb") as f:
            pdf_data = f.read()
        
        # Cleanup
        try:
            os.remove("temp_url.pdf")
        except:
            pass
        
        return pdf_data
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        # Cleanup on error
        try:
            if os.path.exists("temp_url.pdf"):
                os.remove("temp_url.pdf")
        except:
            pass
        return None