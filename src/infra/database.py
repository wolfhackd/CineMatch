
from sqlalchemy import Engine, create_engine
from models.models import *

# print("Tabelas detectadas:", SQLModel.metadata.tables.keys())


class Database:
    _instance: Engine = None

    @classmethod
    def get_engine(cls):
        if(cls._instance is None):
           db_url = "postgresql://admin:admin@localhost:5433/cinematch_vibe"
           cls._instance= create_engine(db_url,echo=True,pool_size=5,max_overflow=10)

           SQLModel.metadata.create_all(cls._instance)

        return cls._instance
    
    
    

# Para usar em qualquer lugar do projeto:
# engine = Database.get_engine()