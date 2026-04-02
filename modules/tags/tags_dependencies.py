

from fastapi import Depends

from config.database import get_db
from modules.tags.tags_controller import TagsController
from modules.tags.tags_repository import TagsRepository
from modules.tags.tags_service import TagsService


def get_tags_controller(session = Depends(get_db)):
    repo = TagsRepository(session)
    service = TagsService(repo)
    return TagsController(service)