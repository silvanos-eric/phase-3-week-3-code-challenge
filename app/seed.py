"""
Script to seed the database with fake data.

The script creates a session to interact with the database, then creates 50
bands, 10 venues, and 90 concerts, and adds them to the database. The bands
and venues are created with fake data, and the concerts are created by
randomly matching bands and venues with a random date.

The script then commits the changes to the database and closes the session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Band, Venue, Concert
import random


def create_session():
    """Create a session to interact with the database."""
    DATABASE_URL = 'sqlite:///concerts.db'
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def seed_data():
    print('Seeding data...')
    """Seed the database with 50 bands, 10 venues, and 90 concerts."""
    session = create_session()
    fake = Faker()

    # Reset database
    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()

    # Create 50 bands with fake data
    bands = []
    for _ in range(50):
        band = Band(name=fake.company(), hometown=fake.city())
        bands.append(band)
        session.add(band)

    # Create 10 venues with fake data
    venues = []
    for _ in range(10):
        venue = Venue(title=fake.company() + " Hall", city=fake.city())
        venues.append(venue)
        session.add(venue)

    # Commit the changes
    session.commit()

    # Create 90 concerts by randomly matching bands and venues with a random date
    concerts = []
    for _ in range(150):
        random_band = random.choice(bands)
        random_venue = random.choice(venues)
        random_date = fake.date_this_year()

        # Check if the concert already exists
        existing_concert = session.query(Concert).filter_by(
            band_id=random_band.id, venue_id=random_venue.id,
            date=random_date).first()

        # If the concert doesn't exist, create it
        if existing_concert is None:
            concert = Concert(band_id=random_band.id,
                              venue_id=random_venue.id,
                              date=random_date)
            concerts.append(concert)

    # Add the concerts to the database and commit the changes
    session.add_all(concerts)
    session.commit()
    session.close()
    print("Seeding done.")


if __name__ == "__main__":
    seed_data()
