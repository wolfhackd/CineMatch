

from fastapi import HTTPException

from models.models import Filme
from modules.films.films_service import FilmsService


class FilmsController:
    def __init__(self, service: FilmsService):
        self.service = service

    def list_films(self):
        return self.service.list_films()
    
    def create_film(self, filme: Filme):
        try:
            return self.service.create_film(filme)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")
        
    def add_tag_to_film(self,film_id, tag_id):
        try:
            if film_id is None or tag_id is None:
                raise HTTPException(status_code=400, detail="Id and tag_id are required")
            if film_id == "" or tag_id == "":
                raise HTTPException(status_code=400, detail="Id and tag_id are required")
            return self.service.add_tag_to_film(film_id, tag_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")