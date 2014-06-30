from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, Column, Index
Base = declarative_base()
class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True)
    timestamp = Column(DateTime)
    status = Column(Integer, default=1)
    def __init__(self, key, timestamp, status):
        self.key = key
        self.timestamp = timestamp
        self.status = status
