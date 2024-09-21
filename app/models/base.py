from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create interface between database and sqlalchemy
DATABASE_URL = 'sqlite:///concerts.db'
engine = create_engine(DATABASE_URL)

# Create a session class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Create the base class for models
Base = declarative_base()
