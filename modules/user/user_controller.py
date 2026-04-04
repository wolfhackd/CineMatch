


from fastapi import HTTPException

from models.models import User
from modules.user.user_service import UserService


class UserController: 
    def __init__(self, service: UserService) -> None:
        self.service = service
    

    def create_user(self, user: User):
        if user is None or not user.name:
            raise HTTPException(status_code=400, detail="Invalid user data")
        if user.name == "":
            raise HTTPException(status_code=400, detail="Invalid user data")
        return self.service.create_user(user)
    
    def list_users(self):
        return self.service.list_users()