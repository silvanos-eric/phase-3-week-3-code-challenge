from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Band, Concert, Venue

if __name__ == '__main__':
    engine = create_engine('sqlite:///concerts.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch a band, venue and concert from the database
    band = session.query(Band).first()
    venue = session.query(Venue).first()
    concert = session.query(Concert).first()

    import ipdb
    ipdb.set_trace()
