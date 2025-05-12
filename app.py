import streamlit as st
import re
import pandas as pd
from io import StringIO
import docx
import PyPDF2

st.title("Multi-format Text Processor with *** Insertion")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "docx", "pdf", "csv", "xlsx"])

def extract_text(file):
    file_type = file.name.split(".")[-1].lower()

    if file_type == "txt":
        return file.read().decode("utf-8")

    elif file_type == "docx":
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file_type == "pdf":
        pdf = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    elif file_type == "csv":
        df = pd.read_csv(file)
        return df.to_string(index=False)

    elif file_type == "xlsx":
        df = pd.read_excel(file)
        return df.to_string(index=False)

    else:
        return "Unsupported file type."



def format_text(text):
    # 1. Add *** before every number followed by a dot (e.g., 5., 12., 100.)
    text = re.sub(r'(?<!\*)\b(\d+\.)', r'***\1', text)

    # 2. Add *** after any full stop that is:
    #    - directly followed by whitespace and a number-dot (e.g., ". 6.")
    #    - or is at the very end of the text
    text = re.sub(r'(\.)(?=\s+\d+\.)', r'\1***', text)  # full stop before number-dot
    text = re.sub(r'(\.)(\s*)$', r'\1***', text)        # final full stop at end of text

    return text

if uploaded_file is not None:
    raw_text = extract_text(uploaded_file)
    formatted_text = format_text(raw_text)

    st.subheader("Formatted Output")
    st.text_area("Processed Text", formatted_text, height=400)

    st.download_button("Download Formatted Text", formatted_text, file_name="formatted.txt")
