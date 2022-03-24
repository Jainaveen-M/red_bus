import enum
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum


Base = declarative_base()

class BusType(enum.Enum):
    AC = 'AC'
    Non_Ac = 'Non_Ac'

class Bus(Base):
    __tablename__ = 'bus'
    id = Column(Integer(),unique=True,primary_key=True,autoincrement=True)
    reg_no = Column(String(100))
    type = Column(Enum(BusType))
    operator_id = Column(Integer())
    amenity_id = Column(Integer())
    
    