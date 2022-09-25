#________________________________________________________ACCOUNT MODEL__________________________________________________________________________________

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from .abstract import DataBase
from .enum import AccessType
from .subscriber import Subscriber, Subscribed


class Account(DataBase):
    __tablename__ = 'accounts'

    nickname = Column(String(20), primary_key=True, nullable=False)
    avatar = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    access_type = Column(Enum(AccessType), default='limited')
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    subscriber_id = Column(Integer, ForeignKey(Subscriber.id))
    subscribed_id = Column(Integer, ForeignKey(Subscribed.id))

