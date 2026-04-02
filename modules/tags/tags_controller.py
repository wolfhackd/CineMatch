


from fastapi import HTTPException

from models.models import Tags
from modules.tags.tags_service import TagsService


class TagsController:
    def __init__(self, service: TagsService):
        self.service = service

    def list_tags(self):
        result = self.service.list_tags()
        if not result:
            raise HTTPException(status_code=404, detail="Tags not found")
        return result
    
    def create_tag(self, tag: Tags):
        if not tag.tag:
            raise HTTPException(status_code=400, detail="Tag is required")
        if tag.tag == "":
            raise HTTPException(status_code=400, detail="Tag is required")
        return self.service.create_tag(tag)