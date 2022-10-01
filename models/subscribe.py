#________________________________________________________SUBSCRIBE MODELS__________________________________________________________________________________

from sqlalchemy import Column, ForeignKey, Integer, Enum, String
from .abstract import DataBase
from .enum import SubcribeStatus


class Subscribe(DataBase):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    subscriber = Column(String, nullable=False)
    status = Column(Enum(SubcribeStatus), default=SubcribeStatus.NEW)
    account_nickname = Column(String, ForeignKey('accounts.nickname'))
