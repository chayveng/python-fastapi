import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLAlchemy setup
Base = declarative_base()

# Database setup
DATABASE_URL = "postgresql://postgres:h48EzLgaSmO6FXpS@localhost/example"
database = databases.Database(DATABASE_URL)
metadata = databases.DatabaseURL(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
