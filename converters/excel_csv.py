import pandas as pd
import streamlit as st
from io import BytesIO

def convert_excel_to_csv(excel_file):
    """
    Convert Excel file to CSV
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_file)
        
        # Convert to CSV
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False, encoding='utf-8')
        csv_data = csv_buffer.getvalue()
        
        return csv_data
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        return None

def convert_csv_to_excel(csv_file):
    """
    Convert CSV file to Excel
    """
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        # Convert to Excel
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        
        excel_data = excel_buffer.getvalue()
        
        return excel_data
        
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        return None