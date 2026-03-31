

from modules.tags.tags_repository import TagsRepository


class TagsService:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    def get_tags(self):
        return self.repository.get_tags()
    
    def get_tag_by_id(self, tag_id: str):
        return self.repository.get_tag_by_id(tag_id)
    
    def get_tag_by_tag(self, tag: str):
        return self.repository.get_tag_by_tag(tag)
    
    def create_tag(self, tag: str):
        tag_exists = self.repository.get_tag_by_tag(tag=tag)
        if tag_exists:
            raise Exception("Tag ja cadastrada")
        return self.repository.create_tag(tag)