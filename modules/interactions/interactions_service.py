

from fastapi import HTTPException

from models.models import UserInteraction
from modules.movies.movies_repository import MoviesRepository
from modules.interactions.interactions_repository import InteractionsRepository
from modules.tags.tags_repository import TagsRepository


class InteractionsService:
    def __init__(self, movies_repository:MoviesRepository, tags_repository: TagsRepository, interactions_repository: InteractionsRepository):
        self.repository = interactions_repository
        self.movies_repository = movies_repository
        self.tags_repository = tags_repository

    def add_tag_to_film(self,film_id, tag_id):

        film = self.movies_repository.get_by_id(film_id)

        if not film or film is None:
            raise HTTPException(status_code=404, detail="Film not found")

        tag = self.tags_repository.get_by_id(tag_id)
        if not tag or tag is None:
            raise HTTPException(status_code=404, detail="Tag not found")

        return self.repository.add_tag_to_film(film_id, tag_id)
    
    def interactions(self, film_id, user_id, interaction_type):

        # Buscar o movie
        film = self.movies_repository.get_by_id(film_id)

        # Verificar se o movie existe
        if not film or film is None:
            raise HTTPException(status_code=404, detail="Film not found")

        if not film.tags:
            raise HTTPException(status_code=404, detail="Tags not found")
        # Pontuações e interações

        punctuation = {
            "like": 5,
            "dislike": -5,
            "viewed": 1
        }

        points = punctuation.get(interaction_type.lower(), 0)

        for tag in film.tags:

            existing = self.repository.get_interactions(user_id,tag.id)

            if existing:
                existing.weight += points
                self.repository.interactions(existing)
                
            else:
                new_record = UserInteraction(
                tag_id=tag.id, 
                user_id=user_id, 
                weight=points
            )
                self.repository.interactions(new_record)

        

        return {"status": "success", "tags_processed": len(film.tags)}

     
      
