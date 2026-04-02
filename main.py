# uvicorn main:app --reload
from contextlib import asynccontextmanager

from fastapi import FastAPI
from config.database import create_db_and_tables
from modules.films.films_router import router as films_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    print("🚀 Banco conectado e tabelas sincronizadas!")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(films_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    create_db_and_tables()
    print("Banco conectado e tabelas sincronizadas!")