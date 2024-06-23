#!/usr/bin/python3
"""
    Script that changes the name of a State object from the database.
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
    q = session.query(State).where(State.id.ilike(2))
    state = q.one()
    if state:
        state.name = "New Mexico"
        session.commit()
