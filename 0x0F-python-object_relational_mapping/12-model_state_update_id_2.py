#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    updated_id = 2

    updated_state = session.query(State).filter_by(id=updated_id).first()

    if updated_state:
        updated_state.name = 'New Mexico'

    session.commit()

    print("{:d}: {:s}".format(updated_state.id, updated_state.name))
    session.close()
