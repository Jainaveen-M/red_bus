from flask import Blueprint, jsonify
from src.DataModel.user import User


ct_service = Blueprint('dataController',__name__)



@ct_service.get('/')
def ctService():
    from main import Session,engine
    local_session = Session(bind=engine)
    user_list = local_session.query(User)
    json_list = []
    for user in user_list:
        json_list.append({"id":user.id,"username":user.username,"email":user.email,"Gender":str(user.gender)})
    return jsonify(json_list)
