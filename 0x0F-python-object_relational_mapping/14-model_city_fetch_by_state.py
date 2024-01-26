#!/usr/bin/python3

"""
script that prints all City objects
from the database hbtn_0e_14_usa
"""

import sys
from model_city import Base, City
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

    cities = session.query(State.name, City.id, City.name).join(
            City, State.id == City.state_id).order_by(City.id).all()

    for state_name, city_id, city_name in cities:
        print("{:d}: {:s} {:s}".format(city.state.name, city.id, city.name))

    session.commit()

    session.close()
