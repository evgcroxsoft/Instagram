# ________________________________________________________LIKE SCHEMAS__________________________________________________________________________________

from datetime import date

from pydantic import BaseModel

from models.enum import LikeStatus


class LikeBaseScheme(BaseModel):
    status: LikeStatus

    class Config:
        orm_mode = True


class LikeRetrieveScheme(LikeBaseScheme):
    post_id: int
    created_at: date
    updated_at: date | None

    class Config:
        orm_mode = True
