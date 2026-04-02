from fastapi import Depends

from config.database import get_db
from modules.films.films_controller import FilmsController
from modules.films.films_repository import FilmsRepository
from modules.films.films_service import FilmsService


def get_films_controller(session = Depends(get_db)):
    repo = FilmsRepository(session)
    service = FilmsService(repo)
    return FilmsController(service)