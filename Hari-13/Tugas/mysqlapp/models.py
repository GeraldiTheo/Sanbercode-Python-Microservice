from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://geraldi:geraldi@localhost:3306/perpustakaan', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

if session:
    print('MYSQL Success')
    
class Customers(Base):
    __tablename__ = 'customers'
    userid = Column(Integer, primary_key= True)
    username = Column(String)
    namadepan = Column(String)
    namabelakang = Column(String)
    email = Column(String)
    
    def showUsers(self):
        data = session.query(Customers).all()
        return data
    
    def showUserById(self, key):
        data = session.query(Customers).filter(Customers.userid==key).one()
        return data
    
    def insertUser(self, **data):
        session.add(Customers(**data))
        session.commit()
        
    def updateUserById(self, key, username):
        datum = session.query(Customers).filter(Customers.userid == key).one()
        
        datum.userid = key
        datum.username = username
        
        session.commit()
    
    def deleteUserById(self, key):
        datum = session.query(Customers).filter(Customers.userid == key).one()
        session.delete(datum)
        session.commit()
    