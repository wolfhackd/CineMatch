

from fastapi import HTTPException

from models.models import Movie
from modules.movies.movies_repository import MoviesRepository

class MoviesService:
    def __init__(self, repository: MoviesRepository):
        self.repository = repository

    def list_movies(self):
        return self.repository.get_all()
    
    def get_film_by_id(self, id: str):
        return self.repository.get_by_id(id)
    
    def create_movie(self, movie: Movie):
        if movie.title is None or movie.description is None:
            raise HTTPException(status_code=400, detail="Title and description are required")
        if movie.title == "" or movie.description == "":
            raise HTTPException(status_code=400, detail="Title and description are required")
        return self.repository.create_film(movie)