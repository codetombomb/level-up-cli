#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Fact, fact_user

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///level_up_cli.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()