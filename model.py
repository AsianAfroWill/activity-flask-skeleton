from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
    throughput = Column(Integer)
    client = Column(String)
    path = Column(String)

    def __repr__(self):
        return "<Activity(timestamp='{}', throughput='{}', client='{}', " \
            "path='{}')>".format(
                self.timestamp, self.throughput, self.client, self.path)
