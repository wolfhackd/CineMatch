
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
        return self.session.exec(select(Filme).where(Filme.id == id)).first()

    def get_all(self):
        statement = select(Filme).options(selectinload(Filme.tags))
        return self.session.exec(statement).all()
        # return self.session.exec(select(Filme).all())

    def add_tag_to_film(self, film_id, tag_id):
        relation = FilmeTags(filme_id=film_id, tag_id=tag_id)
        self.session.add(relation)
        self.session.commit()
        self.session.refresh(relation)
        return relation
        