from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_root():
    path = "public/index.html"
    return path

# @app.get("/user/admin")
# def user_admin():
#     return("Admin") 

# @app.get("/user/{name}/{age}/{id}")
# def users(name: str = Path(min_length=2, max_length=20),
#           age: int = Path(ge=18, lt=111),
#           id: int = Path(ge=1)):
#     return {"name":name,"age":age,"id":id}

# @app.get("/users")
# def get_model(name: str = "undef", age: int = 18):
#     return {"user_name": name, "user_age": age}

# @app.get("/userss")
# def get_model(name, age: int = Query(ge=18)):
#     return {"user_name": name, "user_age": age}

# @app.get("#")
# def func_func():
#     return("#func#")
# 
# @app.get("#")
# def func_func():
#     return("#func#")
# 
# @app.get("#")
# def func_func():
#     return("#func#")
# 
# @app.get("#")
# def func_func():
#     return("#func#")
# 
# @app.get("#")
# def func_func():
#     return("#func#") 