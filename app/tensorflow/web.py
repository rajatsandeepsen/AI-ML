from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse

app = APIRouter()

base_dir = Path(__file__).resolve().parent
model_path = base_dir / "model.tflite"
html_path = base_dir / "index.html"
load_html_path = base_dir / "load.html"


@app.get("/model.tflite")
def download_model() -> FileResponse:
    return FileResponse(
        path=model_path,
        filename=model_path.name,
        media_type="application/octet-stream",
    )


@app.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))


@app.get("/load", response_class=HTMLResponse)
def load() -> HTMLResponse:
    return HTMLResponse(content=load_html_path.read_text(encoding="utf-8"))
