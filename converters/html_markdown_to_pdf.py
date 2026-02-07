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
    Convert website URL to PDF using headless browser
    """
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        st.info(f"Loading webpage: {url}")
        
        import asyncio
        from playwright.async_api import async_playwright
        
        async def generate_pdf():
            async with async_playwright() as p:
                # Launch browser
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                # Navigate to URL and wait for page to load
                st.info("Rendering page with JavaScript...")
                await page.goto(url, wait_until='networkidle', timeout=60000)
                
                # Wait for content to render
                await page.wait_for_timeout(3000)
                
                # Generate PDF
                st.info("Converting to PDF...")
                pdf_bytes = await page.pdf(
                    format='A4',
                    print_background=True,
                    margin={
                        'top': '10mm',
                        'right': '10mm',
                        'bottom': '10mm',
                        'left': '10mm'
                    }
                )
                
                await browser.close()
                
                return pdf_bytes
        
        # Run async function
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        pdf_bytes = loop.run_until_complete(generate_pdf())
        
        return pdf_bytes
            
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return None