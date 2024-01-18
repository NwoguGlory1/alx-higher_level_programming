#!/usr/bin/python3
"""
script that lists all State objects from database:hbtn_0e_6_usa
via SQLAlchemy, not mysql connector now
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    code should not be executed when imported
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    """states = session.query(State).filter_by(states.name).first
    didn't work or California instead of states.name"""

for state in states:
    if 'a' in state.name:
        print("{:d}: {:s}".format(state.id, state.name))
