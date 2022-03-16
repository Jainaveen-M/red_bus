from enum import Enum
import uuid
from xmlrpc.client import Boolean, boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum
from datetime import datetime
import enum
from sqlalchemy.dialects.postgresql import UUID


Base= declarative_base()

class Gender(enum.Enum):
    M = 'Male'
    F = 'Female'

class LoginType(enum.Enum):
    email = 'Email_login'
    phone = 'OTP_Login'   


class User(Base):
    __tablename__ = 'user'
    id=Column(UUID(as_uuid=True),primary_key=True,unique=True,default=uuid.uuid4)
    username=Column(String(100))
    email=Column(String(100),unique=True)
    phone_number=Column(String(100),unique=True)
    password=Column(String(200))
    gender=Column(Enum(Gender))
    login_type=Column(Enum(LoginType))
    is_email_verified = Column(BOOLEAN,default=False)
    date_created=Column(DateTime(),default=datetime.utcnow)
    
    def __repr__(self):
         return f">>> id : {self.id} username : {self.username} email : {self.phone_number} password : {self.password} date_created : {self.date_created}"
    