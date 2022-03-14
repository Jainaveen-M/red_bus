from enum import Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Enum
from datetime import datetime
import enum


Base= declarative_base()

class Gender(enum.Enum):
    M = 'Male'
    F = 'Female'

class LoginType(enum.Enum):
    email = 'Email_login'
    phone = 'OTP_Login'   


class User(Base):
    __tablename__ = 'user'
    id=Column(Integer(),primary_key=True)
    username=Column(String(100))
    email=Column(String(100))
    phone_number=Column(String(100))
    password=Column(String(100))
    gender=Column(Enum(Gender))
    login_type=Column(Enum(LoginType))
    date_created=Column(DateTime(),default=datetime.utcnow)
    
    def __repr__(self):
         return f">>> id : {self.id} username : {self.username} email : {self.phone_number} password : {self.password} date_created : {self.date_created}"
    