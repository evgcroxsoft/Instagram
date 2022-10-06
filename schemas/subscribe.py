# ________________________________________________________SUBSCRIBE SCHEMAS__________________________________________________________________________________

from datetime import date

from pydantic import BaseModel

from models.enum import SubcribeStatus


class SubscribeBaseScheme(BaseModel):
    status: SubcribeStatus
    subscriber: str

    class Config:
        orm_mode = True


class SubscribeRetrieveScheme(SubscribeBaseScheme):
    created_at: date
    updated_at: date | None

    class Config:
        orm_mode = True
