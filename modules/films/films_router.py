import uuid

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.models import Filme
from modules.films.films_controller import FilmsController
from modules.films.films_dependencies import get_films_controller

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

class FilmeReadWithTags(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    tags: list[TagRead] = []



@router.get("/", response_model=list[FilmeReadWithTags])
async def list_films(controller: FilmsController = Depends(get_films_controller)):
   return controller.list_films()

@router.get('/{film_id}', response_model=FilmeReadWithTags)
async def get_film(film_id: uuid.UUID, controller: FilmsController = Depends(get_films_controller)):
    return controller.get_film_by_id(film_id)

@router.post('/')
async def create_film(film: Filme, controller: FilmsController = Depends(get_films_controller)):
    return controller.create_film(film)