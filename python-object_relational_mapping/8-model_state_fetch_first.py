#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

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

    # Query the first State object ordered by id
    state = session.query(State).order_by(State.id).first()

    # Display result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
