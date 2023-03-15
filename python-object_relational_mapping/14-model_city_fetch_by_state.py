#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db_api = 'mysql+mysqldb://{}:{}@localhost/{}'
    usr = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(db_api.format(usr, pswd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = (session.query(City, State)
              .filter(City.state_id == State.id)
              .order_by(City.id).all())

    for cities, states in result:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
