import streamlit as st
import re
from io import StringIO
import pandas as pd
from docx import Document
import PyPDF2


# Function to extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to extract text from CSV
def extract_text_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    text = df.to_string(index=False)
    return text

# Function to extract text from Excel files (XLS/XLSX)
def extract_text_from_excel(excel_file):
    df = pd.read_excel(excel_file)
    text = df.to_string(index=False)
    return text

# Function to handle text file
def extract_text_from_txt(txt_file):
    text = txt_file.read().decode("utf-8")
    return text

# Function to identify the number of questions
def identify_questions(text):
    question_pattern = r'\d+\.'
    questions = re.findall(question_pattern, text)
    return len(questions)

# Streamlit app
def main():
    st.title("Question Identifier")

    # File uploader
    uploaded_file = st.file_uploader("Upload a file", type=["docx", "txt", "csv", "xls", "xlsx", "pdf"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension == 'docx':
            text = extract_text_from_docx(uploaded_file)
        elif file_extension == 'pdf':
            text = extract_text_from_pdf(uploaded_file)
        elif file_extension == 'csv':
            text = extract_text_from_csv(uploaded_file)
        elif file_extension in ['xls', 'xlsx']:
            text = extract_text_from_excel(uploaded_file)
        elif file_extension == 'txt':
            text = extract_text_from_txt(uploaded_file)

        # Count questions in the extracted text
        num_questions = identify_questions(text)
        
        st.write(f"There are {num_questions} questions in the provided file.")

if __name__ == "__main__":
    main()
