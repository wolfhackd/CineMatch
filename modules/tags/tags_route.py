
from fastapi import APIRouter, Depends

from models.models import Tags
from modules.tags.tags_controller import TagsController
from modules.tags.tags_dependencies import get_tags_controller




router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def list_tags(controller: TagsController = Depends(get_tags_controller)):
    return controller.list_tags()

@router.post("/")
async def create_tag(tag: Tags, controller: TagsController = Depends(get_tags_controller)):
    return controller.create_tag(tag)