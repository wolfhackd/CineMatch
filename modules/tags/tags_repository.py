

from models.models import Tags


class TagsRepository:
    def __init__(self, session):
        self.session = session

    def create_tag(self, tag: Tags):
        self.session.add(tag)
        self.session.commit()
        self.session.refresh(tag)
        return tag
    
    def get_all(self):
        return self.session.query(Tags).all()