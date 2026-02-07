# UniBox - Universal File Converter

A professional, modular file conversion platform built with Streamlit.

## Features

### 📄 Document Tools
- **Word to PDF** - Convert .docx to PDF with high precision ✅
- **PDF to Word** - Convert PDF to editable .docx ✅
- Excel to CSV (Coming Soon)
- CSV to Excel (Coming Soon)
- Markdown to PDF (Coming Soon)
- HTML to PDF (Coming Soon)

### 🎨 Media Tools (Coming Soon)
- PNG to JPG / JPG to PNG
- WEBP conversion
- Image Resizer
- Video to GIF
- Video Compressor
- Audio format conversion (MP3, WAV, etc.)

### ⚙️ Dev & Data Tools (Coming Soon)
- JSON to CSV / CSV to JSON
- XML/YAML conversion
- Code Formatter (multiple languages)
- SQL Formatter
- Base64 Encoder/Decoder
- Hash Generator
- API Tester

## Project Structure

```
unibox_project/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── packages.txt               # System dependencies (LibreOffice)
├── converters/                # Conversion logic modules
│   ├── __init__.py
│   ├── word_to_pdf.py        # Word to PDF converter
│   └── pdf_to_word.py        # PDF to Word converter
├── pages/                     # Page components
│   ├── __init__.py
│   ├── document_tools.py     # Document conversion UI
│   ├── media_tools.py        # Media conversion UI (WIP)
│   └── dev_tools.py          # Developer tools UI (WIP)
└── utils/                     # Utility modules
    ├── __init__.py
    └── styles.py             # Custom CSS styles

```

## Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Create a new GitHub repository
2. Upload all files maintaining the folder structure
3. Ensure `requirements.txt` and `packages.txt` are in the root directory

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Set main file path to: `app.py`
5. Click "Deploy"

### Step 3: Configure (if needed)

The app will automatically:
- Install Python dependencies from `requirements.txt`
- Install LibreOffice from `packages.txt` (required for Word to PDF conversion)

## Local Development

### Prerequisites
- Python 3.8+
- LibreOffice (for Word to PDF conversion on Linux)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd unibox_project

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Usage

1. Select a category from the sidebar (Document Tools, Media Tools, or Dev & Data Tools)
2. Choose your desired conversion tool
3. Upload your file
4. Click the convert button
5. Download your converted file

## Technical Details

- **Framework**: Streamlit
- **PDF to Word**: pdf2docx library
- **Word to PDF**: 
  - Windows: docx2pdf (requires MS Word)
  - Linux/Cloud: LibreOffice (headless mode)

## Future Enhancements

- [ ] Batch file conversion
- [ ] Drag & drop interface
- [ ] Conversion history
- [ ] Custom conversion settings
- [ ] API endpoint support
- [ ] Additional file format support

## Credits

Built with Streamlit by Evan William

## License

MIT License