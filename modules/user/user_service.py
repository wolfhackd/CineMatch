

from models.models import User
from modules.user.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User):
        return self.repository.create_user(user)
    
    def list_users(self):
        return self.repository.get_all()
    