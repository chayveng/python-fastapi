from sqlalchemy import Column, String, Integer
from app.core.database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String)