from crypt import methods
from flask import Blueprint, jsonify, request
from src.DataController.booking_controller import BookingController
from src.DataController.seat_controller import SeatController
from src.DataModel.bus import Bus
from src.DataModel.schedule import Schedule

from src.services.db import Session

admin_service = Blueprint('src/services/admin_service',__name__)

# create a seats table
@admin_service.get('/create/seats')
def create_seats():
    db_session = Session()
    schedule = db_session.query(Schedule)
    li =[]
    j=0
    for i in schedule:
        table_name = 'b'+str(i.bus_id)+'_r' + str(i.route_id)+'_d'+ str(i.date)+'_seat'
        li.append(table_name)
        print("+++++ {0}".format(j))
        SeatController.creat_table(table_name)
        if j<5:
            SeatController.add_details(table_name,"seater")
        elif j<10:
            SeatController.add_details(table_name,"sleeper")
        else:
            SeatController.add_details(table_name,"semi_sleeper")
        j+=1
    return jsonify({"status": "success","message":li})

