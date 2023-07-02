from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse

app = FastAPI()

@app.get("/text", response_class=PlainTextResponse)
def get_text():
    return "Hello FastApi TextResponse"

# Analogue
# @app.get("/text")
# def get_text():
#     data = "Hello FastApi TextResponse"
#     return PlainTextResponse(content=data)

@app.get("/json", response_class=JSONResponse)
def get_json():
    data = {"message": "Hello FastApi JsonResponse"}
    return data['message']

@app.get("/html", response_class=HTMLResponse)
def read_root():
    return "<h2>Hello FastApi</h2>"