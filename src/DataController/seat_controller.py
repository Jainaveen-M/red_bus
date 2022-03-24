from operator import imod
from sqlalchemy.orm import declarative_base
from src.services.db import Inspect, Session, engine
from src.DataModel.seat import PrepareSeatTable
class SeatController():
    def check_table(table_name):
        print("table name : {0}".format(table_name))
        try:
            if Inspect.has_table(table_name):
                print("++++ present {0} ++++".format(table_name))
                return True
            else:
                print("+++++ Not present {0} ++++ ".format(table_name))
                return False
        except Exception as e:
            print(">>>>>>>>> {0}".format(str(e)))
            return False
        
    def creat_table(table_name):
        Base = declarative_base()
        PrepareSeatTable.make_class(Base,table_name)
        Base.metadata.create_all(engine)
        
    def add_details(table_name,type,fare):
        Base = declarative_base()
        db_session = Session()
        tname = PrepareSeatTable.make_class(Base,table_name)
        for i in range(1,31):
            new_user = tname(id = i,type = type, status = "available",fare = fare)
            db_session.add(new_user)   
        db_session.commit()
        
    def bookSeat(table_name,seatId):
        Base = declarative_base()
        db_session = Session()
        tname = PrepareSeatTable.make_class(Base,table_name)
        db_session.query(tname).where(tname.id==seatId).update({"status":"booked"})
        db_session.commit()
        
        
        