from fastapi import FastAPI
import uvicorn

from fastapi import FastAPI, Depends

from app.core.database import SessionLocal
from sqlalchemy.orm import Session

from app.schemas.todo import Todo

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def method_name():
    return {"hello": "FastAPI"}


@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos