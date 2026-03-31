

from modules.films.films_service import FilmsService


class FilmsController:
    def __init__(self, films_service: FilmsService):
        self.service = films_service


    def list_films(self):
        return self.service.get_films()
    
    def get_filme_by_id(self, filme_id: str):
        if not filme_id:
            return {"error": "Precisa informar o id do filme"}
        return self.service.get_filme_by_id(filme_id)
    
    def get_filme_by_title(self, title: str):
        if not title:
            return {"error": "Precisa informar o title"}
        return self.service.get_filme_by_title(title)
    
    def create_filme(self, title: str, description: str):
        if not title or not description:
            return {"error": "Precisa informar o title e description"}
        return self.service.create_filme(title, description)