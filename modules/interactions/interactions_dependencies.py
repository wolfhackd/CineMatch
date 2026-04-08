

from fastapi import Depends

from config.database import get_db
from modules.movies.movies_repository import MoviesRepository
from modules.interactions.interactions_controller import InteractionsController
from modules.interactions.interactions_repository import InteractionsRepository
from modules.interactions.interactions_service import InteractionsService
from modules.tags.tags_repository import TagsRepository


def get_interactions_controller(session = Depends(get_db)):
    interactions_repository = InteractionsRepository(session)
    tags_repository = TagsRepository(session)
    movies_repository = MoviesRepository(session)
    service = InteractionsService(movies_repository,tags_repository, interactions_repository)
    return InteractionsController(service)