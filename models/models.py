# from typing import List
import uuid
from enum import Enum as PyEnum
from sqlmodel import  Field, Relationship, SQLModel

class MovieTags(SQLModel, table=True):
    movie_id: uuid.UUID = Field(foreign_key="movie.id", primary_key=True)
    tag_id: uuid.UUID = Field(foreign_key="tags.id", primary_key=True)

class Movie(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    title: str
    description: str

    tags: list["Tags"] = Relationship(back_populates="movies", link_model=MovieTags)

class Tags(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    tag: str

    movies: list["Movie"] = Relationship(back_populates="tags", link_model=MovieTags)

# Relacinamento muitos para muitos

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    name: str

class InteractionType(str, PyEnum):
    LIKE = "like"
    DISLIKE = "dislike"
    VIEWED = "viewed"

class UserInteraction(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    tag_id: uuid.UUID = Field(foreign_key="tags.id")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    interaction_type: InteractionType = Field(index=True)
    weight: int 