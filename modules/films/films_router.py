import uuid

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.models import Filme
from modules.films.films_controller import FilmsController
from modules.films.films_dependencies import get_films_controller

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


router = APIRouter(
    prefix="/films",
    tags=["Films"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[FilmeReadWithTags])
async def list_films(controller: FilmsController = Depends(get_films_controller)):
   return controller.list_films()

@router.post('/')
async def create_film(film: Filme, controller: FilmsController = Depends(get_films_controller)):
    return controller.create_film(film)

# Tenho que arrumar pra receber mais de um

class TagRequest(BaseModel):
    tag_id: str

@router.put('/{film_id}')
async def create_film( film_id: str,  data: TagRequest, controller: FilmsController = Depends(get_films_controller)):
    return controller.add_tag_to_film(film_id, data.tag_id)