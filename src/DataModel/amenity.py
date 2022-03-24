
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum


Base = declarative_base()

class Amenity(Base):
    __tablename__ = 'amenity'
    id = Column(Integer(),unique=True,primary_key=True,autoincrement=True)
    wifi = Column(BOOLEAN,default=False)
    tv = Column(BOOLEAN,default=False)
    rest_room = Column(BOOLEAN,default=False)
    charging_point =Column(BOOLEAN,default=False)
    blankets = Column(BOOLEAN,default=False)
    water_bottle = Column(BOOLEAN,default=False)
    track_my_bus = Column(BOOLEAN,default=False)
    emg_contact_no = Column(BOOLEAN,default=False)
    bus_id =Column(BOOLEAN,default=False)

    

    