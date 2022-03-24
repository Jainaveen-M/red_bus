from ast import For
import enum
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum
from datetime import datetime

from src.DataModel.user import User


Base = declarative_base()

class SeatStatus(enum.Enum):
    booked = "Booked"
    available = "Available"

class SeatType(enum.Enum):
    seater = "Seater"
    semi_sleeper = "Semi-Sleeper"
    sleeper = "Sleeper"

class PrepareSeatTable():
    def make_class(Base, table_name):
        class Seat(Base):
            __tablename__ = table_name
            __table_args__ = {'extend_existing': True}
            id = Column(Integer(), primary_key=True)
            type =Column(Enum(SeatType))
            status = Column(Enum(SeatStatus))
            fare_id = Column(Integer())       
        return Seat 