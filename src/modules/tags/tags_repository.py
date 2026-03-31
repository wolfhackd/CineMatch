

from sqlmodel import Session

from infra.models.models import Tags


class TagsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_tags(self):
        return self.db.select(Tags).all()
        
    def get_tag_by_id(self, tag_id: str):
        return self.db.select(Tags).filter(Tags.id == tag_id).first()
    
    def get_tag_by_tag(self, tag: str):
        return self.db.select(Tags).filter(Tags.tag == tag).first()
    
    def create_tag(self, tag: str):
        tag = Tags(tag=tag)
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        return tag