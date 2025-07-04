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
        try:
            with st.spinner("Generating review..."):
                response = requests.post(
                    "http://localhost:8000/resume-review",
                    files=files,
                    data=data,
                    timeout=60
                )
                response.raise_for_status()
                review = response.json().get("content", "")
            st.success("Review generated successfully!")
            st.write(review)
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with backend: {e}")
