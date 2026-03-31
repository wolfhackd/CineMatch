

from modules.films.films_repository import FilmsRepository


class FilmsService:
    def __init__(self, films_repository: FilmsRepository):
        self.repository = films_repository

    def get_films(self):
        return self.repository.get_films()
    
    def get_filme_by_id(self, filme_id: str):
        return self.repository.get_filme_by_id(filme_id)
    
    def get_filme_by_title(self, title: str):
        return self.repository.get_filme_by_title(title)
    
    def create_filme(self, title: str, description: str):
        filme_exists = self.repository.get_filme_by_title(title=title)
        if filme_exists:
            raise Exception("Filme ja cadastrado")
        return self.repository.create_filme(title, description)