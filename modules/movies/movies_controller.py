

from fastapi import HTTPException

from models.models import Movie
from modules.movies.movies_service import MoviesService


class MoviesController:
    def __init__(self, service: MoviesService):
        self.service = service

    def list_movies(self):
        return self.service.list_movies()
    
    def get_movie_by_id(self, id: str):
        if id is None or id == "":
            raise HTTPException(status_code=400, detail="Id is required")
        return self.service.get_movie_by_id(id)
    
    def create_movie(self, movie: Movie):
        try:
            return self.service.create_movie(movie)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")