


from fastapi import Depends

from config.database import get_db
from modules.user.user_controller import UserController
from modules.user.user_repository import UserRepository
from modules.user.user_service import UserService


def get_user_controller(session = Depends(get_db)):
    repo = UserRepository(session)
    service = UserService(repo)
    return UserController(service)