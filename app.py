from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from model import Base

engine = create_engine('postgresql://ubuntu:ubuntu@localhost:5432/postgres', echo=True)

def create_table():
    Base.metadata.create_all(engine)

create_table()
