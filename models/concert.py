from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Concert(Base):
    __tablename__ = 'concerts'

    date = Column(Date, nullable=False)

    band_id = Column(Integer, ForeignKey('bands.id'), primary_key=True)
    venue_id = Column(Integer, ForeignKey('bands.id'), primary_key=True)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
