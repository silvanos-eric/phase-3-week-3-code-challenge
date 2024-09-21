from sqlalchemy import Column, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)

    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    __tableargs__ = (UniqueConstraint('band_id',
                                      'venue_id',
                                      'date',
                                      name='uix_band_venue_date'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
