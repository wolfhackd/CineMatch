
from modules.suggestions.suggestions_service import SuggestionsService



class SuggestionsController:
    def __init__(self, service: SuggestionsService):
        self.service = service

    def get_suggestions(self, user_id: str):
        return self.service.generate_suggestions(user_id)