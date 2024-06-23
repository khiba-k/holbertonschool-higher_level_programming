#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    arg = sys.argv[4]
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
    q = session.query(State).where(State.name.ilike(arg))
    state = q.first()
    if state:
        print(state.id)
    else:
        print("Not found")
