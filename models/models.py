# from typing import List
import uuid
from enum import Enum as PyEnum
from sqlmodel import  Field, Relationship, SQLModel

class FilmeTags(SQLModel, table=True):
    filme_id: uuid.UUID = Field(foreign_key="filme.id", primary_key=True)
    tag_id: uuid.UUID = Field(foreign_key="tags.id", primary_key=True)

class Filme(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title: str
    description: str

    tags: list["Tags"] = Relationship(back_populates="filmes", link_model=FilmeTags)

class Tags(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    tag: str

    filmes: list["Filme"] = Relationship(back_populates="tags", link_model=FilmeTags)

# Relacinamento muitos para muitos

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
    peso: int 