#________________________________________________________SUBSCRIBERS MODELS__________________________________________________________________________________

from tokenize import String
from sqlalchemy import Column, ForeignKey, Integer
from .abstract import DataBase


class Subscriber(DataBase):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    account_id = Column(String, ForeignKey('accounts.nickname'))


class Subscribed(DataBase):
    __tablename__ = 'subscribed'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    account_id = Column(String, ForeignKey('accounts.nickname'))