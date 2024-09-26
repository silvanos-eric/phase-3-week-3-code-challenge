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
        """Return a string representation of the Venue object.

        The representation includes the venue ID, title, and city.
        """
        return f"Venue(id={self.id}, title={self.title}, city={self.city})"

    def concert_on(self, date):
        """Return the concert that is happening on the given date.

        If no concert is happening on the given date, return None.

        Parameters
        ----------
        date : str
            The date in the format 'YYYY-MM-DD'

        Returns
        -------
        Concert
            The concert happening on the given date, or None if no concert.
        """
        return next(
            (concert for concert in self.concerts
             if concert.date == datetime.strptime(date, "%Y-%m-%d").date()),
            None)

    def most_frequent_band(self):
        """Return the band that has the most concerts at this venue.

        Returns
        -------
        Band
            The band with the most concerts at this venue.
        """
        band_counts = {}
        for concert in self.concerts:
            band = concert.band
            if band not in band_counts:
                band_counts[band] = 0
            band_counts[band] += 1
        return max(band_counts, key=band_counts.get)
