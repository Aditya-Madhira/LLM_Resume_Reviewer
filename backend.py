#code for fastapi

from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/post-endpoint")
async def receive_post(file: UploadFile = File(...)):
    # You can process the file here if needed
    return {"message": "got it"}