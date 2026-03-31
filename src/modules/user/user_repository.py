from sqlmodel import Session

from infra.models.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str):
        user = User(name=name)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_users(self):
        return self.db.select(User).all()
    
    def get_user_by_id(self, user_id: str):
        return self.db.select(User).filter(User.id == user_id).first()
    
    def get_user_by_name(self, name: str):
        return self.db.select(User).filter(User.name == name).first()