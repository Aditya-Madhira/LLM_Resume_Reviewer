# backend.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from io import BytesIO
from LLM_logic import GoogleLLM

app = FastAPI()

# Allow CORS from Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/resume-review")
async def receive_post(
    file: UploadFile = File(...),
    api_key: str = Form(...)
):
    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")

    # Read PDF contents
    contents = await file.read()
    try:
        reader = PdfReader(BytesIO(contents))
        text = "".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse PDF: {e}")

    # Initialize LLM and generate review
    llm = GoogleLLM(api_key=api_key)
    review = llm.generate(text)
    return {"message": "Review generated successfully", "content": review}
