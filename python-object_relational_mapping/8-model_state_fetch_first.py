#!/usr/bin/python3
"""
    Script that lists all State objects from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


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
    q = session.query(State)
    state = q.first()
    if state:
        print("{:d}: {:s}".format(state.id, state.name))
    else:
        print("Nothing")
