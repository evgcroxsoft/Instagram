# ________________________________________________________USER MODEL__________________________________________________________________________________


from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from .abstract import DataBase


class User(DataBase):
    __tablename__ = "users"

    id = Column(UUIDType(binary=False), primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)

    account = relationship("Account", backref="users", cascade="all, delete")
