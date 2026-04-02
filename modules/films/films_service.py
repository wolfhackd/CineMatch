

from fastapi import HTTPException

from models.models import Filme
from modules.films.films_repository import FilmsRepository


class FilmsService:
    def __init__(self, repository: FilmsRepository):
        self.repository = repository

    def list_films(self):
        return self.repository.get_all()
    
    def create_film(self, filme: Filme):
        if filme.title is None or filme.description is None:
            raise HTTPException(status_code=400, detail="Title and description are required")
        if filme.title == "" or filme.description == "":
            raise HTTPException(status_code=400, detail="Title and description are required")
        return self.repository.create_film(filme)