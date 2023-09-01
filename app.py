import streamlit as st
# Set your OpenAI API key here
st.title("Resume Parser with OpenAI GPT-3")

# Upload a resume file
uploaded_resume = st.file_uploader("Upload a resume (PDF or text)", type=["pdf", "txt"])

if uploaded_resume is not None:
  resume_text = uploaded_resume.read()
  st.write(resume_text)
