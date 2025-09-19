from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path  # Add this import
import random

topicos = ["Topico1", "Topico2", "Topico3","Topico4"]

app = FastAPI()

static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

index_file = Path(__file__).parent / "index.html"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse(
        "home.html",
        {"request": request, "name": "Maurino"}
    )

@app.get("/topicos")
def get_topic():
    topico = random.choice(topicos)
    return {"topico": topico}