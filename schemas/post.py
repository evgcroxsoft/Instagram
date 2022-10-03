#________________________________________________________POST SCHEMAS__________________________________________________________________________________

from datetime import date
from pydantic import BaseModel

from models.enum import PostStatus

class PostBaseScheme(BaseModel):
    status: PostStatus
    description: str | None = None
    media: list

    class Config:
        orm_mode = True


class PostRetrieveScheme(PostBaseScheme):
    created_at: date
    updated_at: date | None
    media: list

    class Config:
        orm_mode = True


class PostPaginationScheme(BaseModel):
    id: int
    description: str
    media: list
    likes: int
    dislikes: int

    class Config:
        orm_mode = True
