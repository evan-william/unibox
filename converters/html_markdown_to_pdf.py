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
    Convert Markdown to PDF with GitHub-style rendering
    """
    try:
        # Read markdown content
        md_content = md_file.read().decode('utf-8')
        
        # Convert markdown to HTML with extras (tables, code blocks, etc.)
        html_content = markdown2.markdown(
            md_content, 
            extras=[
                'tables', 
                'fenced-code-blocks', 
                'break-on-newline',
                'cuddled-lists',
                'header-ids',
                'strike',
                'task_list'
            ]
        )
        
        # Add GitHub-style CSS
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                @page {{
                    size: A4;
                    margin: 2cm;
                }}
                
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
                    line-height: 1.6;
                    color: #24292e;
                    max-width: 100%;
                    margin: 0;
                    padding: 20px;
                    font-size: 16px;
                }}
                
                /* Headers */
                h1, h2, h3, h4, h5, h6 {{
                    margin-top: 24px;
                    margin-bottom: 16px;
                    font-weight: 600;
                    line-height: 1.25;
                }}
                
                h1 {{
                    font-size: 2em;
                    border-bottom: 1px solid #eaecef;
                    padding-bottom: 0.3em;
                }}
                
                h2 {{
                    font-size: 1.5em;
                    border-bottom: 1px solid #eaecef;
                    padding-bottom: 0.3em;
                }}
                
                h3 {{ font-size: 1.25em; }}
                h4 {{ font-size: 1em; }}
                h5 {{ font-size: 0.875em; }}
                h6 {{ font-size: 0.85em; color: #6a737d; }}
                
                /* Paragraphs and text */
                p {{
                    margin-top: 0;
                    margin-bottom: 16px;
                }}
                
                /* Links */
                a {{
                    color: #0366d6;
                    text-decoration: none;
                }}
                
                a:hover {{
                    text-decoration: underline;
                }}
                
                /* Lists */
                ul, ol {{
                    padding-left: 2em;
                    margin-top: 0;
                    margin-bottom: 16px;
                }}
                
                li {{
                    margin-bottom: 0.25em;
                }}
                
                /* Code blocks */
                code {{
                    background-color: rgba(27,31,35,0.05);
                    border-radius: 3px;
                    font-size: 85%;
                    margin: 0;
                    padding: 0.2em 0.4em;
                    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
                }}
                
                pre {{
                    background-color: #f6f8fa;
                    border-radius: 3px;
                    font-size: 85%;
                    line-height: 1.45;
                    overflow: auto;
                    padding: 16px;
                    margin-bottom: 16px;
                }}
                
                pre code {{
                    background-color: transparent;
                    border: 0;
                    display: inline;
                    line-height: inherit;
                    margin: 0;
                    overflow: visible;
                    padding: 0;
                    word-wrap: normal;
                }}
                
                /* Tables */
                table {{
                    border-collapse: collapse;
                    border-spacing: 0;
                    width: 100%;
                    margin-bottom: 16px;
                    display: block;
                    overflow: auto;
                }}
                
                table th {{
                    font-weight: 600;
                    padding: 6px 13px;
                    border: 1px solid #dfe2e5;
                    background-color: #f6f8fa;
                }}
                
                table td {{
                    padding: 6px 13px;
                    border: 1px solid #dfe2e5;
                }}
                
                table tr {{
                    background-color: #fff;
                    border-top: 1px solid #c6cbd1;
                }}
                
                table tr:nth-child(2n) {{
                    background-color: #f6f8fa;
                }}
                
                /* Blockquotes */
                blockquote {{
                    margin: 0;
                    padding: 0 1em;
                    color: #6a737d;
                    border-left: 0.25em solid #dfe2e5;
                }}
                
                /* Horizontal rule */
                hr {{
                    height: 0.25em;
                    padding: 0;
                    margin: 24px 0;
                    background-color: #e1e4e8;
                    border: 0;
                }}
                
                /* Images */
                img {{
                    max-width: 100%;
                    box-sizing: content-box;
                    background-color: #fff;
                }}
                
                /* Badges (if any) */
                img[src*="shields.io"],
                img[src*="badge"] {{
                    display: inline-block;
                    margin: 2px;
                }}
                
                /* Task lists */
                input[type="checkbox"] {{
                    margin-right: 0.5em;
                }}
                
                /* Centering */
                div[align="center"] {{
                    text-align: center;
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
        import traceback
        st.error(traceback.format_exc())
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
