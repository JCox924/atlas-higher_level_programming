#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_a(username, password, database):
    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database to get all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state in the list
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to write the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    # The script should only execute when run directly, not when imported
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        delete_states_with_a(username, password, database)