# LLM Resume Reviewer

This project provides a simple way to get automated feedback on your resume using Google's Generative AI models.
It contains:

- **FastAPI backend** (`backend.py`) that accepts a PDF resume and a Google GenAI API key. The backend extracts text from the PDF and asks the Gemini model for an expert review.
- **Streamlit frontend** (`streamlit.py`) that lets you upload your resume and enter your API key. It calls the backend and shows the generated review in the browser.
- **LLM wrapper** (`LLM.py`) defining a small helper around the Gemini API.
- **Sample tests** (`mytest.py`) demonstrating how to mock the LLM when testing the API.

## Running the application

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn PyPDF2 google-generativeai streamlit pytest reportlab
   ```
2. Start the backend:
   ```bash
   uvicorn backend:app --reload
   ```
3. In a separate terminal, launch the Streamlit interface:
   ```bash
   streamlit run streamlit.py
   ```
4. Enter your Google GenAI API key and upload a PDF resume to receive feedback.

## Testing

Run the tests with:
```bash
pytest -q
```

## License

This project is provided as-is for educational purposes.

