# ________________________________________________________LIKE MODELS__________________________________________________________________________________

from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from .abstract import DataBase
from .enum import LikeStatus


class Like(DataBase):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    status = Column(Enum(LikeStatus))
    post_id = Column(Integer, ForeignKey("posts.id"))
    account_nickname = Column(String, ForeignKey("accounts.nickname"))
