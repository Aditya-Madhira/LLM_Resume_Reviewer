# streamlit.py

import streamlit as st
import requests

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")
st.title("LLM Resume Reviewer")

# 1. Text input for API key
api_key = st.text_input("Enter your Google GenAI API Key", type="password")

# 2. File uploader for PDF
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file and api_key:
    if st.button("Submit"):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        data = {"api_key": api_key}
        # Send both file and api_key to FastAPI backend
        response = requests.post(
            "http://localhost:8000/review-resume",
            files=files,
            data=data
        )
        if response.ok:
            st.success("File uploaded and processed!")
            st.write(response.json()["content"])
        else:
            st.error(f"Error: {response.text}")
