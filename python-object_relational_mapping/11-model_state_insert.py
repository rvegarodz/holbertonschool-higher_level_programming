#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db_api = 'mysql+mysqldb://{}:{}@localhost/{}'
    usr = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    state_nm = 'Louisiana'

    engine = create_engine(db_api.format(usr, pswd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = State(name = state_nm)
    session.add(obj)
    session.commit()
    results = session.query(State).distinct()
    for states in results:
        idx = "{}:"
        print(idx.format(states.id), states.name)
