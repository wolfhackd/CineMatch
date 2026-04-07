

from fastapi import HTTPException

from models.models import Filme
from modules.films.films_service import FilmsService


class FilmsController:
    def __init__(self, service: FilmsService):
        self.service = service

    def list_films(self):
        return self.service.list_films()
    
    def get_film_by_id(self, id: str):
        if id is None or id == "":
            raise HTTPException(status_code=400, detail="Id is required")
        return self.service.get_film_by_id(id)
    
    def create_film(self, filme: Filme):
        try:
            return self.service.create_film(filme)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")