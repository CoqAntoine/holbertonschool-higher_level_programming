#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their states, sorted by cities.id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
