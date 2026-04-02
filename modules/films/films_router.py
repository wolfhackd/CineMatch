
from fastapi import APIRouter, Depends
from models.models import Filme
from modules.films.films_controller import FilmsController
from modules.films.films_dependencies import get_films_controller


router = APIRouter(
    prefix="/films",
    tags=["Films"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def list_films(controller: FilmsController = Depends(get_films_controller)):
   return controller.list_films()

@router.post('/')
async def create_film(film: Filme, controller: FilmsController = Depends(get_films_controller)):
    return controller.create_film(film)