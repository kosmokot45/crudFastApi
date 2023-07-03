from fastapi import FastAPI, Path, Query
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

@app.get("/user/admin")
def user_admin():
    return("Admin") 

@app.get("/user/{name}/{age}/{id}")
def users(name: str = Path(min_length=2, max_length=20),
          age: int = Path(ge=18, lt=111),
          id: int = Path(ge=1)):
    return {"name":name,"age":age,"id":id}

@app.get("/users")
def get_model(name: str = "undef", age: int = 18):
    return {"user_name": name, "user_age": age}

@app.get("/userss")
def get_model(name, age: int = Query(ge=18)):
    return {"user_name": name, "user_age": age}