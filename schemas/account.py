# ________________________________________________________ACCOUNT SCHEMAS__________________________________________________________________________________

from datetime import date

from pydantic import BaseModel

from models.enum import AccountStatus


class AccountBaseScheme(BaseModel):
    nickname: str
    avatar: str | None = None
    description: str
    status: AccountStatus

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
