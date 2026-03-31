

from modules.tags.tags_service import TagsService


class TagsController:
    def __init__(self, tags_service: TagsService):
        self.repository = tags_service

    def create_tag(self, tag: str):
        return self.repository.create_tag(tag)

    def get_tags(self):
        return self.repository.get_tags()
    
    def get_tag_by_id(self, tag_id: str):
        return self.repository.get_tag_by_id(tag_id)
    
    def get_tag_by_tag(self, tag: str):
        if not tag:
            raise Exception("Tag não informada")
        return self.repository.get_tag_by_tag(tag)
    
