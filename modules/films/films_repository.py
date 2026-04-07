
from sqlalchemy.orm import selectinload
from sqlmodel import select
from models.models import Filme, FilmeTags


class FilmsRepository:
    def __init__(self, session):
        self.session = session
    
    def create_film(self, filme: Filme):
        self.session.add(filme)
        self.session.commit()
        self.session.refresh(filme)
        return filme
    
    def get_by_id(self, id):
        statement = select(Filme).where(Filme.id == id).options(selectinload(Filme.tags))
        return self.session.exec(statement).first()

    def get_all(self):
        statement = select(Filme).options(selectinload(Filme.tags))
        return self.session.exec(statement).all()
        