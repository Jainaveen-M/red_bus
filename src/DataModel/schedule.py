import enum
from operator import index
from pymysql import Date
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum

from src.DataModel.user import LoginType


Base = declarative_base()

class ScheduleStatus(enum.Enum):
    upcoming = "upcoming"
    cancelled = "cancelled"
    completed = "completed"

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer(),unique=True,primary_key=True,autoincrement=True)
    route_id = Column(Integer())
    bus_id = Column(Integer())
    date = Column(DateTime())
    driver_id = Column(Integer())
    status = Column(Enum(ScheduleStatus))
    
    
    
    

    

    