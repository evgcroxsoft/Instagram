#________________________________________________________ACCOUNT MODEL__________________________________________________________________________________

from sqlalchemy import Boolean, Column, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from .abstract import DataBase
from .enum import AccountStatus

class Account(DataBase):
    __tablename__ = 'accounts'

    nickname = Column(String(20), primary_key=True, nullable=False)
    avatar = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    status = Column(Enum(AccountStatus), default=AccountStatus.LIMITED)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))

    post = relationship('Post', backref='accounts', cascade='all, delete')
    subscribe = relationship('Subscribe', backref='accounts', cascade='all, delete')


