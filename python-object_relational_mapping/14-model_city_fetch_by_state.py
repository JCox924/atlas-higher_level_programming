#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities(username, password, database):
    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database to get all City objects, sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).one()
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # The script should only execute when run directly, not when imported
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        fetch_cities(username, password, database)