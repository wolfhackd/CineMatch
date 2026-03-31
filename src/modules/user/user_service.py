from modules.user.user_repository import UserRepository


class UserService: 
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def create_user(self, name: str):
        user_exists = self.repository.get_user_by_name(name=name)
        
        if user_exists:
            raise Exception("Usuário ja cadastrado")
            
        return self.repository.create_user(name=name)
    
    def get_users(self):
        return self.repository.get_users()
    
    def get_user_by_id(self, user_id: str):
        return self.repository.get_user_by_id(user_id=user_id)