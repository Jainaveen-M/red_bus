from crypt import methods
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import declarative_base
from src.DataController.seat_controller import SeatController
from src.DataModel.schedule import Schedule
from src.DataModel.seat import PrepareSeatTable

from src.services.db import Session

seat_service = Blueprint('src/services/seat_service',__name__)

@seat_service.route('/get/seat/info',methods=['POST'])
def get_available_seat():
    data = request.json
    db_session = Session()
    Base = declarative_base()
    print('++++ data {0}'.format(type(data['bus_id'])))
    table_name = 'b'+str(data["bus_id"])+'_r' + str(data["route_id"])+'_d'+ str(data["date"])+"_seat"
    print("tablee name +++++ {0}".format(table_name))
    table = PrepareSeatTable.make_class(Base,table_name)
    seat = db_session.query(table)
    s_list =[]
    for s in seat:
        s_list.append({"id":s.id,"type":str(s.type),"status":str(s.status),"fare_id":s.fare_id})
    return jsonify({"table_name":table_name,"seats":s_list})


@seat_service.route('/book/seat/<seat_table>')
def book_seat(seat_table):
    data = request.json
    SeatController.bookSeat(seat_table,data['seatId'])
    return jsonify({"status":"success","message":"booked successfully"})
    
    