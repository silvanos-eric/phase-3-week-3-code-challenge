from sqlalchemy import Column, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base, session


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

    def __repr__(self):
        """Return a string representation of the Concert object.

        The representation includes the concert ID, date, band ID, and venue ID.
        """
        return f"Concert(id={self.id}, date={self.date}, band_id={self.band_id}, venue_id={self.venue_id})"

    def is_hometown_show(self):
        """Check if a concert is a hometown show.

        The method checks if the venue for the concert is in the same
        city as the band's hometown. If it is, the method returns True,
        otherwise it returns False.
        """
        return self.venue.city == self.band.hometown

    def introduction(self):
        """Return a string that can be used as an introduction for a concert.

        The introduction includes the city of the venue, the name of the band,
        and the hometown of the band.
        """
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
