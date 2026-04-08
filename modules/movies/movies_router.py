import uuid

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.models import Movie
from modules.movies.movies_controller import MoviesController
from modules.movies.movies_dependencies import get_movies_controller

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)

class TagRead(BaseModel):
    id: uuid.UUID
    tag: str

    class Config:
        from_attributes = True

class movieReadWithTags(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    tags: list[TagRead] = []



@router.get("/", response_model=list[movieReadWithTags])
async def list_movies(controller: MoviesController = Depends(get_movies_controller)):
   return controller.list_movies()

@router.get('/{movie_id}', response_model=movieReadWithTags)
async def get_film(movie_id: uuid.UUID, controller: MoviesController = Depends(get_movies_controller)):
    return controller.get_movie_by_id(movie_id)

@router.post('/')
async def create_movie(movie: Movie, controller: MoviesController = Depends(get_movies_controller)):
    return controller.create_movie(movie)