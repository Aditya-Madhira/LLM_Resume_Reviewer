import streamlit as st
import requests

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")

st.title("PDF Uploader and Submitter")

# 1. Upload PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# 2. Submit Button
if st.button("Submit"):
    if uploaded_file is not None:
        # Read the file as bytes
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        # Send POST request to FastAPI backend
        response = requests.post("http://localhost:8000/post-endpoint", files=files)
        if response.status_code == 200:
            st.success(response.json().get("message", "Success!"))
        else:
            st.error(f"Error: {response.status_code}")
    else:
        st.warning("Please upload a PDF file before submitting.")

        