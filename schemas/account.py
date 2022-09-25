#________________________________________________________USER SCHEMAS__________________________________________________________________________________

from datetime import date
from pydantic import BaseModel

from models.enum import AccessType

class AccountBaseScheme(BaseModel):
    nickname: str 
    avatar: str | None = None
    description: str
    access_type: AccessType

    class Config:
        orm_mode = True


class AccountUpdateScheme(AccountBaseScheme):
    is_active: bool

    class Config:
        orm_mode = True

class AccountRetrieveScheme(AccountBaseScheme):
    created_at: date
    updated_at: date | None
    is_active: bool

    class Config:
        orm_mode = True
