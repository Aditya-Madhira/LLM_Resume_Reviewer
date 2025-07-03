# backend.py

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from io import BytesIO
from LLM import GoogleLLM  

app = FastAPI()

# Allow CORS from Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/review-resume")
async def receive_post(
    file: UploadFile = File(...),
    api_key: str = Form(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
    contents = await file.read()
    try:
        reader = PdfReader(BytesIO(contents))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                            text += page_text + "\n"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse PDF: {e}")

   
    llm = GoogleLLM(api_key=api_key)                                                                                                        
    prompt = f"Please review the following resume and provide a detailed analysis and suggestions for improvement:

{text}"                    
    review = llm.generate(prompt)                                                                                                             
    return {"message": "got it", "content": review}  
