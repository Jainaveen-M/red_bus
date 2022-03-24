from crypt import methods
import json
from sched import scheduler
from flask import Blueprint, jsonify, request
from src.DataController.booking_controller import BookingController
from src.DataModel.bus import Bus
from src.DataModel.route import Route
from src.DataModel.schedule import Schedule
from src.services.db import Session



booking_service = Blueprint('src/services/booking_service',__name__)



@booking_service.get('/get/buses')
def get_buses():
    db_session = Session()
    bus_list = db_session.query(Bus)
    result = []
    for bus in bus_list:
        result.append({"bus_id ": bus.id,"reg_no":bus.reg_no,"type":str(bus.type),"operator_id":bus.operator_id,"amenity_id":bus.amenity_id})
    return jsonify(result)

@booking_service.get('/get/schedule')
def get_schedule():
    db_session = Session()
    schedule = db_session.query(Schedule)
    result = []
    for s in schedule:
        result.append({"id ": s.id,"route_id":s.route_id,"bus_id":s.bus_id,"date":s.date,"driver_id":s.driver_id,"schedule_status":str(s.status)})
    return jsonify(result)

@booking_service.route('/available/buses',methods=['POST'])
def get_available_buses():
    data = request.json
    route_id = BookingController.get_routeId(data['source'],data['destination'])
    buses = BookingController.get_available_buses(route_id,data['date'])
    bus_list =[]
    for bus in buses:
        bus_list.append({"route_id":route_id,"bus_id":bus.id,"reg_no":bus.reg_no,"type":str(bus.type),"operator_id":bus.operator_id,"amenity_id":bus.amenity_id})
        
    return jsonify(bus_list)