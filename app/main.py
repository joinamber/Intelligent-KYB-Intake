from pathlib import Path
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from .workflow import analyze_submission

app = FastAPI(title="Intelligent KYB Intake - Lite MVP")

INDEX = Path(__file__).parent.parent / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return INDEX.read_text()

@app.post("/analyze")
async def analyze(
    merchant_name: str = Form(...),
    email_subject: str = Form("KYB documents"),
    files: list[UploadFile] = File(default=[]),
) -> JSONResponse:
    names = [f.filename or "unnamed" for f in files]
    result = analyze_submission(merchant_name, email_subject, names)
    return JSONResponse(result)
