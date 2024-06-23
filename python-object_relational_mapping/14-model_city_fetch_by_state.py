#!/usr/bin/python3
"""
    Script that prints all City objects from the database.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
