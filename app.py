import streamlit as st
import openai
import fitz  # PyMuPDF library for PDF processing

st.title("Resume Parser with OpenAI GPT-3")

# Upload a resume file
uploaded_resume = st.file_uploader("Upload a resume (PDF or text)", type=["pdf", "txt"])

if uploaded_resume is not None:
    resume_text = ""

    # Check if the uploaded file is a PDF
    if uploaded_resume.type == "application/pdf":
        # Extract text from the PDF using PyMuPDF (Fitz)
        pdf_doc = fitz.open(stream=uploaded_resume.read(), filetype="pdf")
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            resume_text += page.get_text()

    else:
        # If it's not a PDF, assume it's plain text
        resume_text = uploaded_resume.read()

    # Display the extracted text
    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    if st.button("Parse Resume"):
        # Parse the extracted text with OpenAI GPT-3
        parsed_info = parse_resume(resume_text)  # You can reuse the parse_resume function from the previous code
        st.subheader("Parsed Information")
        st.write(parsed_info)
