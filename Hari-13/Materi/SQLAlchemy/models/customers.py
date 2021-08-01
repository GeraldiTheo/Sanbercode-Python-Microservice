from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key= True)
    username = Column(string)
    namaLengkap = Column(string)
    email = Column(String)
    
    