from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    short_id = Column(String, unique=True, index=True)
    long_url = Column(String)