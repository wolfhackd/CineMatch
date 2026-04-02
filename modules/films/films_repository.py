

from sqlmodel import select

from models.models import Filme


class FilmsRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        # return self.session.query(Filme).all()
        return self.session.exec(select(Filme)).all()
    
    def create_film(self, filme: Filme):
        self.session.add(filme)
        self.session.commit()
        self.session.refresh(filme)
        return filme