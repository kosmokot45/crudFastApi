from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import models
from db import engine, sessionlocal
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    ...


@app.get("/add")
async def add_user(reques: Request, name: str = Form(...), salary: int = Form(...), db: Session = Depends(get_db)):
    ...


@app.get("/delete/{user_id}")
async def delete_user():
    ...


@app.get("/update/{user_id}")
async def update_user():
    ...


@app.get("/edit/{user_id}")
async def edit_user():
    ...
