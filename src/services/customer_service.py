
from queue import Empty
from flask import Blueprint, jsonify, request
from pymysql import NULL
from sqlalchemy import null
from src.DataModel.user import User
from sqlalchemy.orm.exc import NoResultFound
from src.DataController.user_controller import UserController
from src.services.db import Session

ct_service = Blueprint('src/services/customer_service',__name__)


#dummy user list
@ct_service.get('/')
def get_user_list():
    from src.services.db import Session,engine
    local_session = Session(bind=engine)
    user_list = local_session.query(User)
    json_list = []
    for user in user_list: 
        json_list.append({"id":user.id,"username":user.username,"email":user.email,"gender":str(user.gender),"phone_number":user.phone_number,"password":user.password,"is_email_verified":user.is_email_verified,"login_type":str(user.login_type)})
    return jsonify(json_list)

#dummy user creation
@ct_service.route('/user/create',methods=['POST'])
def create_user():
    try:
        from src.services.db import Session,engine
        data = request.json
        local_session = Session(bind=engine)
        user_list = local_session.query(User)
    
        for user in user_list:
            if data['username']==user.username:
                return jsonify({"status":"failed","message":"username alread taken"})
            if data['email']==user.email:
                return jsonify({"status":"failed","message":"Email is already registered"})
            if data['phone_number']==user.phone_number:
                return jsonify({"status":"failed","message":"Phone number is already registered"})
        if len(data['phone_number']) < 10:
            return jsonify({"status":"failed","message":"Your phone number must contains 10 character"})

        UserController.create_user(username=data['username'],email=data['email'],phone_number=data['phone_number'],password=data['password'],gender=data['gender'],is_email_verified=data['is_email_verified'],login_type=data['login_type'])
        return jsonify(data)
    except Exception as e:
        return jsonify({"Error":str(e)}),409    
    


# @ct_service.route('/user/update/<id>',methods=['PUT'])
# def update_user():
#     from src.services.db import Session
#     data = request.json
#     db_session = Session()
#     update_user = db_session.query(User).filter(User.id==id).one()
#     update_user.username = data['username']
#     db_session.commit()
#     return jsonify({"status":"succes","message":"User details updated successfully"})
    

@ct_service.route('/signup/email',methods=['POST'])
def signup_with_email():
    try:
        data = request.json
        check_email = UserController.check_email(data['email'])
        generate_password = UserController.generate_hashed_password(data['password'])
        print(">>>>>>>>> check email {0}".format(check_email))
        if not UserController.is_valid_email(data['email']):
            return jsonify({"Error":"Email is not valid"})
        elif not (check_email is None):
            return jsonify({"status":"failed","message":"Email is already taken"})
        elif len(data['password'])<8:
            return jsonify({"status":"failed","message":"Your password must contains atleast 8 characters"})
        else:
            new_user =UserController.create_user(email=data['email'],password=generate_password,is_email_verified=data['is_email_verified'],login_type=data['login_type'])
            return jsonify({"status":"success","message":"user created successfully","data":{"id":new_user.id}})
    except Exception as e:
         return jsonify({"Error":str(e)})
     
     
    
        

@ct_service.route('/signup/mobile',methods=['POST'])
def signup_with_mobile():
    try:
        data = request.json
        check_phoneNo = UserController.check_phoneNo(data['phone_number'])
        if UserController.validate_phoneNumber(data['phone_number']):
            return jsonify({"status":"failed","message":"phone number is not valid. It must contain 10 digits"})
        elif not (check_phoneNo is None):
            return jsonify({"status":"failed","message":"phone number is already taken"})
        else:
            new_user =UserController.create_user(phone_number=data['phone_number'],login_type=data['login_type'])
            print(">>>>>>>>  check phone number : {0}".format(new_user.id))
            view_otp = UserController.send_OTP(new_user.id)
            return jsonify({"status":"success","message":"user created successfully","data":{"id":new_user.id},"OTP":"Enter this OTP : "+str(view_otp)})
    except Exception as e:
        print(str(e))
    return jsonify({"Error":"Unknown"})



@ct_service.route('/send/otp/<userid>',methods=['GET'])
def send_code(userid):
    try:
        otp = UserController.send_OTP(userid)
        return jsonify({"OTP":otp})
    except Exception as e:
        return  jsonify({"Error":str(e)})
    

@ct_service.route('/verify/otp/<userid>',methods=['POST'])
def verify_otp(userid):
    try:
        data = request.json
        otp = UserController.verify_otp(user_id=userid,otp=data['otp'])
        otp_status = "success" if otp else "failed"
        otp_message = "OTP verified successfully" if otp else "OTP verified Failed"
        return jsonify({"otp_status":otp_status,"message":otp_message})
    except Exception as e:
        return  jsonify({"Error":str(e)})


@ct_service.route('/signup/details/<userid>',methods=['PUT'])
def signup_create_user(userid):
    try:
        data = request.json
        db_session = Session()
        db_session.query(User).filter(User.id==userid).update({"username":data['username'],"gender":data['gender']})
        db_session.commit()
        return jsonify({"status":"success","message":"user details updated successfully"})
    except Exception as e:
        print(str(e))
        db_session.rollback()
    return jsonify({"status":"failed","message":"user details not updated"})
        
 
 
@ct_service.route('/login/email',methods=['POST'])       
def loginwith_email():
    try:
        data = request.json
        validate_user = UserController.validate_email_login(data['email'],data['password'])
        if validate_user:
            return jsonify({"status":validate_user,"message":"user logged in successfully"})
    except Exception as e:
        print(str(e))       
    
    return jsonify({"status":"failed","message":"Error occured while login"}) 
        
 
        
@ct_service.route('/login/phone',methods=['POST'])       
def login_with_phone():
    try:
        data = request.json
        check_user= UserController.validate_phoneNumber_login(phonenumber=data['phone_number'])
        if not (check_user is None):
            otp = UserController.send_OTP(check_user.id)
            return jsonify({"status":"success","message":"OTP has send to the phone number "+check_user.phone_number,"OTP":otp,"user_id":check_user.id})      
    except Exception as e:
        print(str(e))             
    return jsonify({"status":"failed","message":"user does not exist"})
        
        
               
@ct_service.get('/home')
def home(userid):
    return "Welcome to redBus {0}".format(userid)
        
        
