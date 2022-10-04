# ________________________________________________________ABSTRACT MODEL__________________________________________________________________________________

from sqlalchemy import Column, Date

from database.db import Base, engine


class DataBase(Base):
    __abstract__ = True
    created_at = Column(Date)
    updated_at = Column(Date)


# create all tables
Base.metadata.create_all(bind=engine)
