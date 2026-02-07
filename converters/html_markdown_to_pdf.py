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

import markdown2
import os
import streamlit as st
import requests
from io import BytesIO
import base64

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
        
        from weasyprint import HTML
        pdf_bytes = HTML(string=html_with_style).write_pdf()
        
        return pdf_bytes
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        return None

def convert_html_to_pdf(html_file):
    """
    Convert HTML file to PDF
    """
    try:
        # Read HTML content
        html_content = html_file.read().decode('utf-8')
        
        from weasyprint import HTML
        pdf_bytes = HTML(string=html_content).write_pdf()
        
        return pdf_bytes
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        return None

def convert_url_to_pdf(url):
    """
    Convert website URL to PDF using Selenium
    """
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        st.info(f"Loading webpage: {url}")
        
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.support.ui import WebDriverWait
        import time
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # Initialize driver
        st.info("Starting browser...")
        driver = webdriver.Chrome(options=chrome_options)
        
        # Load the page
        st.info("Rendering page with JavaScript...")
        driver.get(url)
        
        # Wait for page to load
        time.sleep(5)  # Wait for JavaScript to execute
        
        # Execute print to PDF
        st.info("Converting to PDF...")
        pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
            "printBackground": True,
            "landscape": False,
            "paperWidth": 8.27,  # A4 width in inches
            "paperHeight": 11.69,  # A4 height in inches
            "marginTop": 0.4,
            "marginBottom": 0.4,
            "marginLeft": 0.4,
            "marginRight": 0.4,
        })
        
        driver.quit()
        
        # Decode base64 PDF
        pdf_bytes = base64.b64decode(pdf_data['data'])
        
        return pdf_bytes
            
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return None
