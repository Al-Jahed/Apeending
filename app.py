import streamlit as st
import re
import pandas as pd
import docx
import pdfplumber

# ------------------------------
# Formatting Function
# ------------------------------
def format_text(text):
    # Step 1: Add a newline after each sentence-ending full stop (e.g., death.)
    text = re.sub(r'(\.\s*)', r'\1\n', text)
    
    # Step 2: Insert *** after a sentence-ending full stop and before a number with a full stop (e.g., 6.)
    text = re.sub(r'(\.\s*)\n(\d+\.)', r'\1\n***\n\n*** \2', text)
    
    return text

# ------------------------------
# File Reading Functions
# ------------------------------
def read_txt(file):
    return file.read().decode('utf-8')

def read_docx(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

def read_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def read_csv(file):
    df = pd.read_csv(file)
    return '\n'.join(df.astype(str).apply(' '.join, axis=1))

def read_xlsx(file):
    df = pd.read_excel(file)
    return '\n'.join(df.astype(str).apply(' '.join, axis=1))

# ------------------------------
# Streamlit App
# ------------------------------
st.title("Question Formatter with *** Marker")

uploaded_file = st.file_uploader("Upload your file", type=["txt", "docx", "pdf", "csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.type == "text/plain":
            raw_text = read_txt(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            raw_text = read_docx(uploaded_file)
        elif uploaded_file.type == "application/pdf":
            raw_text = read_pdf(uploaded_file)
        elif uploaded_file.type == "text/csv":
            raw_text = read_csv(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            raw_text = read_xlsx(uploaded_file)
        else:
            st.error("Unsupported file format")
            raw_text = ""
        
        if raw_text:
            formatted = format_text(raw_text)
            st.subheader("Formatted Output:")
            st.text_area("Result", formatted, height=400)
    except Exception as e:
        st.error(f"Error reading or formatting file: {e}")
