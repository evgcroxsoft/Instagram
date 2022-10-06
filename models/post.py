# ________________________________________________________POST MODEL__________________________________________________________________________________

from sqlalchemy import Column, Enum, ForeignKey, Integer, PickleType, String

from models.account import Account

from .abstract import DataBase
from .enum import PostStatus


class Post(DataBase):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(PostStatus))
    media = Column(PickleType)
    account_nickname = Column(String, ForeignKey(Account.nickname))
