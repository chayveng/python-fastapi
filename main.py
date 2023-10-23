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
def greeting():
    return {"hello": "FastAPI"}

@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos
    


if __name__ == "__main__":
    print("FastAPI !!")
    # config = uvicorn.Config("./app/application.py:app", port=4060)
    # server = uvicorn.Server(config)
    uvicorn.run("app.run:app", host="127.0.0.1", port=4060)