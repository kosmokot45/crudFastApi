from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_root():
    path = "public/index.html"
    return path

