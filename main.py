from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random

topicos = ["Topico1", "Topico2", "Topico3","Topico4","Topico5"]

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    
    return template.TemplateResponse(
        "home.html",
        {"request": request, "nome": "Maurino"}
    )

@app.get("/topicos")
def get_topico():
    
    topico = random.choice(topicos)

    return {"topico": topico}