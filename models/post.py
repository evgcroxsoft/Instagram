#________________________________________________________POST MODEL__________________________________________________________________________________

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from models.account import Account

from .abstract import DataBase
from .enum import StatusType

from sqlalchemy import PickleType


class Post(DataBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(StatusType))
    media = Column(PickleType)
    account_nickname = Column(Integer, ForeignKey(Account.nickname))