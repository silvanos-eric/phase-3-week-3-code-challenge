"""
This module contains the database models for the application.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

__all__ = [
    'Base',
    'session',
]

# The database engine.
engine = create_engine('sqlite:///concerts.db')

# The base class to be used by all models.
Base = declarative_base()

# The session maker.
Session = sessionmaker(bind=engine)

# The session to be used by the application.
session = Session()
