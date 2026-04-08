from fastapi import Depends

from config.database import get_db
from modules.movies.movies_controller import MoviesController
from modules.movies.movies_repository import MoviesRepository
from modules.movies.movies_service import MoviesService
from modules.tags.tags_repository import TagsRepository


def get_movies_controller(session = Depends(get_db)):
    repo = MoviesRepository(session)
    service = MoviesService(repo)
    
    return MoviesController(service)