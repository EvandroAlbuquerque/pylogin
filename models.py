from sqlalchemy import Column, Integer, String, ForeignKey
from settings.db import Base, engine


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(100))


Base.metadata.create_all(engine)