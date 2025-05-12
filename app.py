import streamlit as st
import re

st.title("Text Formatter: Add *** Before Numbers and After Paragraphs")

uploaded_file = st.file_uploader("Upload your text file", type=["txt"])

if uploaded_file is not None:
    # Read and decode the text file
    raw_text = uploaded_file.read().decode("utf-8")

    # Add *** before question numbers like 6., 7., etc.
    formatted_text = re.sub(r'^(\d+\.)', r'***\1', raw_text, flags=re.MULTILINE)

    # Add *** at the end of paragraphs that end with a full stop
    formatted_text = re.sub(r'(\.)(\s*\n)', r'\1***\2', formatted_text)

    st.subheader("Formatted Output")
    st.text_area("Processed Text", formatted_text, height=400)

    # Optional: download button
    st.download_button("Download Formatted Text", formatted_text, file_name="formatted.txt")
