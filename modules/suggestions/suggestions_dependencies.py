

from fastapi import Depends

from config.database import get_db
from modules.interactions.interactions_repository import InteractionsRepository
from modules.movies.movies_repository import MoviesRepository
from modules.suggestions.suggestions_controller import SuggestionsController
from modules.suggestions.suggestions_service import SuggestionsService
from modules.tags.tags_repository import TagsRepository


def get_suggestions_controller(session = Depends(get_db)):
   movies_repository = MoviesRepository(session)
   tags_repository = TagsRepository(session)
   interactions_repository = InteractionsRepository(session)
   service = SuggestionsService(movies_repository,interactions_repository,tags_repository
   )


   return SuggestionsController(service)