

from models.models import Tags
from modules.tags.tags_repository import TagsRepository


class TagsService:
    def __init__(self, repository: TagsRepository):
        self.repository = repository
    

    def list_tags(self):
        return self.repository.get_all()
    
    def create_tag(self, tag: Tags):
        return self.repository.create_tag(tag)