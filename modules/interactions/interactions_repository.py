
from models.models import MovieTags, UserInteraction


class InteractionsRepository():
    def __init__(self, session):
        self.session = session

    def add_tag_to_film(self, film_id, tag_id):
        relation = MovieTags(movie_id=film_id, tag_id=tag_id)
        self.session.add(relation)
        self.session.commit()
        self.session.refresh(relation)
        return relation
    
    def get_by_id(self, id):
        return self.session.query(MovieTags).filter(MovieTags.id == id).first()
    
    def get_interactions(self, user_id,tag_id):
        return self.session.query(UserInteraction).filter(UserInteraction.user_id == user_id and UserInteraction.tag_id == tag_id).first()
    
    def interactions(self,UserInteraction):
        self.session.add(UserInteraction)
        self.session.commit()
        self.session.refresh(UserInteraction)
        return UserInteraction
    
