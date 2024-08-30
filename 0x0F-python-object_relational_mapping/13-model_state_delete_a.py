#!/usr/bin/python3
""" a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa  """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.ilike("%a%")).all()
    for state in query:
        session.delete(state)
    session.commit()
