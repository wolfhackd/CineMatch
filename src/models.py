import uuid
from enum import Enum as PyEnum
from sqlmodel import  Field, SQLModel, create_engine

class Filme(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title: str
    description: str

class Tags(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    tag: str
# Relacinamento muitos para muitos
class FilmeTags(SQLModel, table=True):
    filme_id: uuid.UUID = Field(foreign_key="filme.id", primary_key=True)
    tag_id: uuid.UUID = Field(foreign_key="tags.id", primary_key=True)

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    name: str

class TipoInteracao(str, PyEnum):
    CURTIU = "curtiu"
    NAO_CURTIU = "nao_curtiu"
    ASSISTIR_DEPOIS = "assistir_depois"
    VISUALIZOU = "visualizou"

class InteracoesUsuario(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    tag_id: uuid.UUID = Field(foreign_key="tags.id")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    tipo_interacao: TipoInteracao = Field(index=True)
    peso: int # Não tenho certeza se isso foi criado

db_url = "postgresql://admin:admin@localhost:5433/cinematch_vibe"
engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Banco conectado e tabelas criadas!")