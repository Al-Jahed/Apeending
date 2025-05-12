import streamlit as st
import re
import pandas as pd
import docx
import pdfplumber

# ------------------------------
# Formatting Function
# ------------------------------
import re

def identify_questions(text):
    # This regex matches any number followed by a period, which is typical for the question numbering pattern
    question_pattern = r'\d+\.'
    
    # Find all occurrences of the question pattern
    questions = re.findall(question_pattern, text)
    
    # Return the number of questions identified
    return len(questions)

# Sample input text to test the function
sample_text = """
5.It is known (a) ----- all that one day all will pass away (b) ----- this earth. So, we have no escape (c) ----- death. One day, we all will roll down (d) ----- the lap of death. Because death is common (e) ----- all. So we should not mourn (f) ----- the dead. But those who die (g) ----- the country are immortal. Their memories do not sink (h) ----- oblivion. There is no medicine that can save a man (i) ----- death. So, we should always be ready (j) ----- death. 
6. If you want to derive the best (a) --- your education you must be fully aware (b) --- some basic things. You should never be indifferent (c) --- your study. In Fact, fostering a kind of passion (d) --- learning appears to be very important for achieving your goal. Again, you should never try to learn anything (e) --- context. You should also not run (f) --- substandard traditional guide books. As a matter of fact, confining yourself (g) --- poor quality note books discourages you to learn something deeply. But (h) --- learning a thing very deeply, you cannot achieve the required mastery (i) --- the learnt thing. Thus, you may fail to get the desired benefits (j) --- your learning. 
7. Life of common people besets (a) ----- a number of troubles. Price spiral has added new sufferings (b) ----- our life. Indeed, price of daily commodities has gone (c) ----- the ability of the common people. Lack (d) ----- supervision is responsible (e) ----- it. Some dishonest businessmen devoid (i) ----- morality hoard goods (g) ----- quick profit. The govt. should take punitive action (h) ----- those people. People from all walks (i) ----- life should also co-operate (j) ----- government.
"""

# Testing the function
identify_questions(sample_text)


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
