from transformers import pipeline
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  
from fastapi import Form


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory = "templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/result", response_class=HTMLResponse)
async def homepage(request: Request, text_input: str = Form(...)):
    classifier = pipeline("summarization")
    summary = classifier(text_input)
    return templates.TemplateResponse(
        request=request, 
        name="result.html", 
        context={"text_input": text_input, "summary": summary[0]['summary_text']})

