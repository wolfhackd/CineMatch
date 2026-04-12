# uvicorn main:app --reload
from contextlib import asynccontextmanager

from fastapi import FastAPI
from config.database import create_db_and_tables
from modules.movies.movies_router import router as movies_router
from modules.tags.tags_route import router as tags_router
from modules.user.user_routes import router as user_router
from modules.interactions.interactions_router import router as interactions_router
from modules.suggestions.suggestions_route import router as suggestions_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    print("🚀 Banco conectado e tabelas sincronizadas!")
    yield

app = FastAPI(lifespan=lifespan)
# Routes
app.include_router(movies_router)
app.include_router(tags_router)
app.include_router(user_router)
app.include_router(interactions_router)
app.include_router(suggestions_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

