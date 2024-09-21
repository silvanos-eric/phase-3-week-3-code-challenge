from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String)

    concerts = relationship('Concert', back_populates='band')
