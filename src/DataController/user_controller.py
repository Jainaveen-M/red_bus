from optparse import check_builtin
from tabnanny import check
from flask import session
from sqlalchemy import true
from src.DataModel.otp import OTP
from src.DataModel.user import User
from src.services.db import Session
from werkzeug.security import generate_password_hash, check_password_hash
import random

class UserController():
    def create_user(
    username=None,
    email=None,
    phone_number=None,
    password=None,
    gender=None,
    login_type=None,
    is_email_verified=None,
    date_created=None,
    ):
        print(f">>>>>>>> username : {username}  <<<<<<<<")
        db_session = Session()
        db_session.expire_on_commit = False
        new_user = User(username=username,email=email,phone_number=phone_number,password=password,gender=gender,login_type=login_type,is_email_verified=is_email_verified,date_created=date_created)
        db_session.add(new_user)
        db_session.commit()
        return new_user
    
    
    def update_user(
    username=None,
    email=None,
    phone_number=None,
    password=None,
    gender=None,
    login_type=None,
    is_email_verified=None,
    date_created=None,
    ):
        print(f">>>>>>>> username : {username}  <<<<<<<<")
        db_session = Session()
        db_session.expire_on_commit = False
        new_user = User(username=username,email=email,phone_number=phone_number,password=password,gender=gender,login_type=login_type,is_email_verified=is_email_verified,date_created=date_created)
        db_session.add(new_user)
        db_session.commit()
        return new_user
    
    
    def check_email(email=None):
        db_session =Session()
        check_email= None
        print("+++++ Check email +++++ {0}".format(email))
        try:
            check_email = db_session.query(User).filter(User.email==email).one()  
        except Exception as e:
            print(str(e))
        return check_email
    
    def check_username(username=None):
        db_session =Session()
        check_username= None
        print("+++++ Check username +++++ {0}".format(username))
        try:
            check_username = db_session.query(User).filter(User.username==username).one()  
        except Exception as e:
            print(str(e))
        return check_username
        
    
    def check_phoneNo(phone_number=None):
        db_session =Session()
        check_phoneNumber= None
        print("+++++ Check phone number +++++ {0}".format(phone_number))
        try:
            check_phoneNumber = db_session.query(User).filter(User.phone_number==phone_number).one()  
        except Exception as e:
            print(str(e))
        return check_phoneNumber
            
    def is_valid_email(email=None):
        if "@" in email:
            return True
        return False
    
    def validate_phoneNumber(phoneNumber):
        length= len(phoneNumber)
        if length==10:
            return True
        return False
    
    def generate_hashed_password(password=None):
        hashed_password = generate_password_hash(password)
        return hashed_password
    
    def check_password(hashed_password, password): 
        return check_password_hash(hashed_password, password)
            
    def send_OTP(user_id):
        otp = random.randint(100000,999999)
        db_session = Session()
        set_otp = OTP(user_id=user_id,otp=otp)
        db_session.add(set_otp)
        db_session.commit()
        return otp
        
    def verify_otp(user_id,otp):
        db_session = Session()
        verify_otp = db_session.query(OTP).where(OTP.user_id==user_id).order_by(OTP.otp_created.desc()).first()
        print(">>>>>>> {0}".format(verify_otp))
        return str(verify_otp.otp) == otp

    def validate_email_login(email,password):
        db_session = Session()
        check_email =None
        try:
            check_email = db_session.query(User).where(User.email==email).first()
            print(f">>>>>>> check email {check_email}")
        except Exception as e:
            print(str(e))
        if not (check_email is None):
            password_validation = check_password_hash(check_email.password,password,)
            return password_validation;
        return False;
    
    
    def validate_phoneNumber_login(phonenumber):
        db_session = Session()
        check_phoneNumber = None
        try:
            check_phoneNumber = db_session.query(User).where(User.phone_number==phonenumber).first()
            if not (check_phoneNumber is None):
                return check_phoneNumber
        except Exception as e:
            print(str(e))
        return check_phoneNumber