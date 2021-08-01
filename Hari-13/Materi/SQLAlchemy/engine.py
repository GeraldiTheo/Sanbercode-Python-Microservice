from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://geraldi:geraldi@localhost:3306/rentalfilm', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

if session:
    print("Connection Success")

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key =  True)
   namaid = Column(String)
   namalengkap = Column(String)
   email = Column(String)
   

# Search All   
result =  session.query(Customers).all()

for row in result:
    print(row.id, row.namaid, row.namalengkap, row.email)
    
# Search by id
# result = session.query(Customers).filter(Customers.id==2)

# for row in result:
#     print(row.id, row.namaid, row.namalengkap, row.email)
    

data = {
    "namaid" : 'RK',
    "namalengkap" : 'Ravi Kumar', 
    "email" : 'ravi@gmail.com'
}
# Manipulasi Data : Insert

# session.add(Customers(**data))
# session.commit()

# Manipulasi Data : Update

# result = session.query(Customers).filter(Customers.id == 31).one()
# print(result.id, result.namaid, result.namalengkap, result.email)

# result.namaid = 'Ravik'
# session.commit()

# Manipulasi Data : Delete

# result =  session.query(Customers).filter(Customers.id==31).one()
# print(result.id, result.namaid, result.namalengkap, result.email)
# session.delete(result)
# session.commit()

# result =  session.query(Customers).all()
# for row in result:
#     print(row.id, row.namaid, row.namalengkap, row.email)