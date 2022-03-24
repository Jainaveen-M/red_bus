from src.DataModel.bus import Bus
from src.DataModel.route import Route
from src.DataModel.schedule import Schedule
from src.services.db import Session,engine


class BookingController():
    def get_routeId(source,destination):
        db_session = Session(bind=engine)
        print("+++++++ {0} +++++ {1}".format(source,destination))
        route = db_session.query(Route).filter(source==Route.source).where(destination == Route.destination).one()
        return route.id
    
    def get_available_buses(route_id,date):
        db_session = Session(bind=engine)
        buses = db_session.query(Schedule).filter(Schedule.route_id==route_id).where(Schedule.date==date).all()
        b =[]
        for i in buses:
            temp = db_session.query(Bus).filter(Bus.id == i.bus_id).one()
            b.append(temp)
        return b

        
        