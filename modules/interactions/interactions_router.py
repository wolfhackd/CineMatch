

import uuid

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from modules.interactions.interactions_controller import InteractionsController
from modules.interactions.interactions_dependencies import get_interactions_controller

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
    responses={404: {"description": "Not found"}},
)


class TagRequest(BaseModel):
    tag_id: str
# Tenho que arrumar pra receber mais de 
@router.put('/{movie_id}')
async def add_tag( movie_id: str,  data: TagRequest, controller: InteractionsController = Depends(get_interactions_controller)):
    return controller.add_tag_to_movie(movie_id, data.tag_id)


class moviesInteractions(BaseModel):
    user_id: uuid.UUID
    interaction_type: str

@router.post('/{movie_id}')
async def interactions( movie_id: str, data: moviesInteractions, controller: InteractionsController = Depends(get_interactions_controller)):
    return controller.interactions(movie_id, data.user_id, data.interaction_type)