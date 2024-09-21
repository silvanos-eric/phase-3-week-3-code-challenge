from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String)

    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"Venue(id={self.id}, title={self.title}, city={self.city})"

    def concert_on(self, date):
        return next(
            (concert for concert in self.concerts
             if concert.date == datetime.strptime(date, "%Y-%m-%d").date()),
            None)

    def most_frequent_band(self):
        """Returns the band with the most concerts at this venue."""
        band_counts = {}
        for concert in self.concerts:
            band = concert.band
            if band not in band_counts:
                band_counts[band] = 0
            band_counts[band] += 1
        return max(band_counts, key=band_counts.get)
