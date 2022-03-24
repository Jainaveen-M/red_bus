from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum


Base = declarative_base()

class Route(Base):
    __tablename__ = 'route'
    id = Column(Integer(),unique=True,primary_key=True,autoincrement=True)
    source = Column(String(100))
    destination = Column(String(100))
    
    

    

    