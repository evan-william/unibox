# UniBox - Universal File Converter

A professional, modular file conversion platform built with Streamlit. Convert documents, media files, and data formats with a clean, intuitive interface.

## Overview

UniBox provides a unified platform for common file conversion tasks. Built with modularity and extensibility in mind, it offers both immediate utility through working converters and a framework for expanding functionality.

## Features

### Document Tools
- **Word to PDF** - Convert Microsoft Word documents (.docx) to PDF with precise formatting preservation
- **PDF to Word** - Convert PDF files to editable Word documents (.docx)
- Excel to CSV *(in development)*
- CSV to Excel *(in development)*
- Markdown to PDF *(in development)*
- HTML to PDF *(in development)*

### Media Tools *(in development)*
- Image format conversion (PNG, JPG, WEBP)
- Image resizing and optimization
- Video to GIF conversion
- Video compression
- Audio format conversion (MP3, WAV, FLAC)

### Developer Tools *(in development)*
- JSON/CSV bidirectional conversion
- XML and YAML format conversion
- Code formatters for multiple languages
- SQL query formatting
- Base64 encoding and decoding
- Hash generation (MD5, SHA-256, etc.)
- REST API testing interface

## Architecture

```
unibox/
├── app.py                      # Application entry point with routing
├── requirements.txt            # Python package dependencies
├── packages.txt               # System-level dependencies
├── converters/                # Conversion engine implementations
│   ├── pdf_to_word.py        # PDF → Word conversion logic
│   └── word_to_pdf.py        # Word → PDF conversion logic
├── document_tools.py          # Document conversion interface
├── media_tools.py            # Media conversion interface
├── dev_tools.py              # Developer tools interface
└── utils/
    └── styles.py             # Custom CSS styling
```

## Quick Start

### Local Development

**Prerequisites:**
- Python 3.8 or higher
- LibreOffice (required for Word to PDF conversion on Linux/macOS)

**Installation:**

```bash
# Clone the repository
git clone https://github.com/yourusername/unibox.git
cd unibox

# Install Python dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Deployment to Streamlit Cloud

1. Push your code to a GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" and select your repository
4. Set the main file path to `app.py`
5. Deploy

Streamlit Cloud will automatically install dependencies from `requirements.txt` and `packages.txt`.

## Usage

1. **Select a category** from the sidebar navigation
2. **Choose a conversion tool** from the dropdown menu
3. **Upload your file** using the file uploader
4. **Click convert** to process your file
5. **Download the result** using the download button

## Technical Implementation

### Conversion Engines

**PDF to Word:**
- Uses `pdf2docx` library for accurate text and layout extraction
- Preserves formatting, tables, and images where possible

**Word to PDF:**
- Platform-adaptive approach:
  - **Windows:** Uses `docx2pdf` with MS Word COM automation
  - **Linux/Cloud:** Uses LibreOffice in headless mode for conversion
- Maintains document formatting and metadata

### Styling

Custom CSS provides a professional black-and-white interface with:
- Responsive layout design
- Consistent visual hierarchy
- Accessible color contrast ratios
- Modern, minimal aesthetic

## Configuration

The application uses Streamlit's configuration system through `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#000000"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f5f5f5"
textColor = "#000000"

[server]
headless = true
enableCORS = false
```

## Roadmap

**Short-term:**
- Complete media conversion tools implementation
- Add batch file processing capabilities
- Implement drag-and-drop file upload

**Medium-term:**
- Developer tools suite completion
- Conversion quality settings and customization
- User conversion history and management

**Long-term:**
- RESTful API for programmatic access
- Additional file format support
- Advanced processing pipelines
- User authentication and storage

## Dependencies

**Core:**
- `streamlit` - Web application framework
- `pdf2docx` - PDF to Word conversion
- `docx2pdf` - Word to PDF conversion (Windows)
- `python-docx` - Word document manipulation

**System:**
- `LibreOffice` - Document conversion engine (Linux/macOS)

## Contributing

Contributions are welcome. Please ensure:
- Code follows existing style conventions
- New converters include error handling
- UI components maintain design consistency
- Documentation is updated accordingly

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

Built by Evan William

## Acknowledgments

- Streamlit team for the excellent framework
- pdf2docx contributors for PDF conversion capabilities
- LibreOffice project for cross-platform document processing