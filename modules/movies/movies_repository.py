
from sqlalchemy.orm import selectinload
from sqlmodel import select
from models.models import Movie, Tags


class MoviesRepository:
    def __init__(self, session):
        self.session = session
    
    def create_film(self, movie: Movie):
        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie
    
    def get_by_id(self, id):
        statement = select(Movie).where(Movie.id == id).options(selectinload(Movie.tags))
        return self.session.exec(statement).first()
    
    def get_movies_by_tags(self, tag_ids):
        statement = (
            select(Movie)
            .where(Movie.tags.any(Tags.id.in_(tag_ids))) 
            .options(selectinload(Movie.tags))
        )
        return self.session.exec(statement).all()
        

   

    def get_all(self):
        statement = select(Movie).options(selectinload(Movie.tags))
        return self.session.exec(statement).all()
        