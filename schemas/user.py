#________________________________________________________USER SCHEMAS__________________________________________________________________________________

from datetime import date
from pydantic import BaseModel, EmailStr

class BaseUserScheme(BaseModel):
    email: EmailStr
    phone: str | None = None

    class Config:
        orm_mode = True

class UserCreateScheme(BaseUserScheme):
    hashed_password: str

    class Config:
        orm_mode = True

class UserUpdateScheme(BaseUserScheme):
    is_active: bool

    class Config:
        orm_mode = True

class UserRetrieveScheme(BaseUserScheme):
    created_at: date
    updated_at: date | None
    is_active: bool

    class Config:
        orm_mode = True