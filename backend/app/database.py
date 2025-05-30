from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:nievedelimon@db:5432/Laboratorio3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Añade esta función
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()