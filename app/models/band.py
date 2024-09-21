from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, session
from models.concert import Concert
from datetime import datetime


class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String)

    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f"Band(id={self.id}, name={self.name}, hometown={self.hometown})"

    def play_in_venue(self, venue, date):
        new_concert = Concert(band_id=self.id,
                              venue_id=venue.id,
                              date=datetime.strptime(date, "%Y-%m-%d").date())
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        bands = session.query(Band).all()
        return max(bands, key=lambda band: len(band.concerts))
