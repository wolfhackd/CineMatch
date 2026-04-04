
from models.models import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_all(self):
        return self.session.query(User).all()