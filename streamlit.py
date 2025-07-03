import streamlit as st

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")

st.title("Resume Reviewer")

st.write(
    "Paste your resume text below and click **Analyze** to see it "
    "displayed with a basic word count."
)

text = st.text_area("Resume Text", height=300)

if st.button("Analyze"):
    if text.strip():
        st.subheader("You entered:")
        st.write(text)
        st.write(f"Word count: {len(text.split())}")
    else:
        st.warning("Please enter some text before analyzing.")
