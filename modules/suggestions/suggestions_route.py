



from fastapi import APIRouter, Depends

from modules.suggestions.suggestions_controller import SuggestionsController
from modules.suggestions.suggestions_dependencies import get_suggestions_controller


router = APIRouter(
    prefix="/suggestions",
    tags=["Suggestions"],
    responses={404: {"description": "Not found"}},
)

@router.post('/{user_id}')
async def get_suggestions( user_id: str, controller: SuggestionsController = Depends(get_suggestions_controller)):
    return controller.get_suggestions(user_id)