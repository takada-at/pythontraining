from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, Column, Index
Base = declarative_base()
class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    col0 = Column(String(100), unique=True)
    col1 = Column(DateTime)
    col2 = Column(Integer, default=1)
