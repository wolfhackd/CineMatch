

from sqlmodel import Session
from infra.models.models import Filme


class FilmsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_films(self):
        return self.db.select(Filme).all()
    
    def get_filme_by_id(self, filme_id: str):
        return self.db.select(Filme).filter(Filme.id == filme_id).first()
    
    def get_filme_by_title(self, title: str):
        return self.db.select(Filme).filter(Filme.title == title).first()
    
    def create_filme(self, title: str, description: str):
        filme = Filme(title=title, description=description)
        self.db.add(filme)
        self.db.commit()
        self.db.refresh(filme)
        return filme