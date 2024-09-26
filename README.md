# Phase 3 Week 3 Code Challenge

## Table of Contents

- [Phase 3 Week 3 Code Challenge](#phase-3-week-3-code-challenge)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Models](#models)
    - [Band](#band)
    - [Venue](#venue)
    - [Concert](#concert)
  - [Alembic Migrations](#alembic-migrations)
  - [Usage](#usage)
  - [License](#license)

This project is a simple concert tracking app built using Python, SQLAlchemy, and Alembic for migrations. The app tracks bands, venues, and concerts, allowing you to see which bands are playing at which venues, and much more.

## Features

- **Band management**: Track bands with details like their name and hometown.
- **Venue management**: Keep a list of venues, including their names and cities.
- **Concert management**: Organize concerts by band, venue, and date.
- **SQLAlchemy ORM**: Database models for bands, venues, and concerts.
- **Alembic migrations**: Manage your database schema with version control.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/silvanos-eric/phase-3-week-3-code-challenge.git
   cd phase-3-week-3-code-challenge
   ```

2. Create and activate a virtual environment:

   ```bash
   pipenv --python 3.8.13
   pipenv shell
   ```

3. Install dependencies:

   ```bash
   pipenv install
   ```

4. Set up the database:
   ```bash
   alembic upgrade head
   ```

## Project Structure

```bash
.
├── alembic.ini
├── concerts.db
├── debug.py
├── LICENSE
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 5a0aa7f8ad00_initial_migration.py
│       ├── 6889b7c70cdd_create_concert_model.py
│       ├── bcfe55f29da1_create_band_model.py
│       └── dd388c9e49ce_create_venue_model.py
├── models
│   ├── band.py
│   ├── base.py
│   ├── concert.py
│   ├── __init__.py
│   └── venue.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── seed.py

```

## Models

### Band

- `id`: Integer, primary key
- `name`: String, required
- `hometown`: String, optional
- Relationships:
  - A band can have many concerts.

### Venue

- `id`: Integer, primary key
- `title`: String, required
- `city`: String, optional
- Relationships:
  - A venue can have many concerts.

### Concert

- `id`: Integer, primary key
- `date`: Date, required
- `band_id`: ForeignKey to `Band`
- `venue_id`: ForeignKey to `Venue`
- Relationships:
  - A concert belongs to one band and one venue.

## Alembic Migrations

This project uses Alembic to manage database migrations. The initial migrations set up the schema for the `bands`, `venues`, and `concerts` tables.

To create a new migration after modifying models:

```bash
alembic revision --autogenerate -m "description"
```

To apply the migrations:

```bash
alembic upgrade head
```

## Usage

Once the database is set up, you can interact with the models through SQLAlchemy sessions. Here are a few examples of what you can do:

- **Add a new band**:

  ```python
  from models import Band, session
  new_band = Band(name='The Rolling Stones', hometown='London')
  session.add(new_band)
  session.commit()
  ```

- **Schedule a concert**:

  ```python
  from models import Band, Venue
  band = session.query(Band).first()
  venue = session.query(Venue).first()
  band.play_in_venue(venue, '2024-10-10')
  ```

- **Find a band with the most performances**:
  ```python
  Band.most_performances()
  ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.