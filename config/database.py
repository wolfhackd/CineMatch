from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

db_url = "postgresql://admin:admin@localhost:5433/cinematch_vibe"
engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session