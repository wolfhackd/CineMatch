


from fastapi import APIRouter, Depends
from models.models import User
from modules.user.user_controller import UserController
from modules.user.user_dependencies import get_user_controller


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def crate_user(user: User, controller: UserController = Depends(get_user_controller)):
    return controller.create_user(user)


@router.get("/")
async def list_users(controller: UserController = Depends(get_user_controller)):
    return controller.list_users()