from fastapi import FastAPI, Request
import pathlib
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
print ((BASE_DIR / "templates").exists())
app=FastAPI()
templates= Jinja2Templates(directory= str(BASE_DIR/"templates"))

#REST API

@app.get("/",response_class=HTMLResponse)
def home_view(request: Request):
    print (request)
    # return templates.TemplateResponse("home.html", {"request": request, "abc": 123}
    return templates.TemplateResponse(request, "home.html", {"abc": 123})


@app.post("/")
def home_detail_view():
    return {"hello":"world"}