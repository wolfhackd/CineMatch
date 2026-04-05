

from fastapi import HTTPException

from models.models import Filme, FilmeTags
from modules.films.films_repository import FilmsRepository
from modules.tags.tags_repository import TagsRepository


class FilmsService:
    def __init__(self, repository: FilmsRepository, tags_repository: TagsRepository):
        self.repository = repository
        self.tags_repository = tags_repository

    def list_films(self):
        return self.repository.get_all()
    
    def create_film(self, filme: Filme):
        if filme.title is None or filme.description is None:
            raise HTTPException(status_code=400, detail="Title and description are required")
        if filme.title == "" or filme.description == "":
            raise HTTPException(status_code=400, detail="Title and description are required")
        return self.repository.create_film(filme)
    
    def add_tag_to_film(self,film_id, tag_id):
        # Chamar o film_id e vê se realmente existe
        film = self.repository.get_by_id(film_id)
        if not film or film is None:
            raise HTTPException(status_code=404, detail="Film not found")

        # Chamar o tag_id e vê se realmente existe
        # Tenho que chamar o repo certo
        tag = self.tags_repository.get_by_id(tag_id)
        if not tag or tag is None:
            raise HTTPException(status_code=404, detail="Tag not found")

        # Vincular a classe
        # Salvar no banco

        return self.repository.add_tag_to_film(film_id, tag_id)