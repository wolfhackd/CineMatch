

from fastapi import HTTPException

from modules.interactions.interactions_service import InteractionsService


class InteractionsController:
    def __init__(self, service: InteractionsService):
        self.service = service

    def add_tag_to_movie(self,film_id, tag_id):
        try:
            if film_id is None or tag_id is None:
                raise HTTPException(status_code=400, detail="Id and tag_id are required")
            if film_id == "" or tag_id == "":
                raise HTTPException(status_code=400, detail="Id and tag_id are required")
            return self.service.add_tag_to_film(film_id, tag_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")
        

    # def remove_tag_from_film
    # def list_movies_with_tags

    def interactions(self, film_id, user_id, interaction_type):
        try:
            if user_id is None or user_id == "":
                raise HTTPException(status_code=400, detail="User_id is required")
            if film_id is None or interaction_type is None or film_id == "" or interaction_type == "":
                raise HTTPException(status_code=400, detail="Id and tag_id are required")
            if interaction_type.lower() not in ['like','dislike','viewed']:
                raise HTTPException(status_code=400, detail="Interaction type is invalid")
            
            return self.service.interactions(film_id, user_id, interaction_type)
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error to save: {str(e)}")