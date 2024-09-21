from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String)

    concerts = relationship('Concert', back_populates='band')
