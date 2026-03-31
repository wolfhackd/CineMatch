from modules.user.user_service import UserService

class UserController:
    def __init__(self,user_service: UserService):
        self.repository = user_service

    def create_user(self, name: str):
        user = self.service.create_user(name)
        if not user:
            return {"error": "Usuário já cadastrado"}
        return user
    
    def list_users(self):
        return self.service.get_users()
    
    def get_user_by_id(self, user_id: str):
        if not user_id:
            return {"error": "Precisa informar o id do usuário"}
        return self.service.get_user_by_id(user_id)