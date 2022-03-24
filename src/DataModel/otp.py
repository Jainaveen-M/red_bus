from ast import For
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum
from datetime import datetime

from src.DataModel.user import User


Base = declarative_base()


class OTP(Base):
    __tablename__ = 'otp'
    id = Column(Integer(),unique=True,primary_key=True,autoincrement=True)
    otp = Column(Integer())
    user_id = Column(Integer(),ForeignKey(User.id))
    otp_created=Column(DateTime(),default=datetime.utcnow)
    
    
    def __repr__(self):
        return f">>>>>  user_id : {self.user_id}  otp : {self.otp}"
    
