import streamlit as st
import aspose.words as aw
import docx2txt

st.title("Resume Parser with OpenAI GPT-3")
#this is the merge commit
# Upload a resume file
uploaded_resume = st.file_uploader("Upload a resume (PDF or text)", type=["pdf", "txt", "docx"], accept_multiple_files=True)

if uploaded_resume is not None:
    resume_text = ""

    # Check if the uploaded file is a PDF
    if uploaded_resume.type == "application/pdf":
        doc = aw.Document(uploaded_resume)
        doc.save("Output1.docx")
        my_text = docx2txt.process("./Output1.docx")
        st.write(my_text)
        
