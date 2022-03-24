from ast import For
from sqlalchemy.orm import declarative_base
from sqlalchemy import BOOLEAN, Column, Integer, String, ForeignKey,DateTime,Enum
from datetime import datetime

from src.DataModel.user import User


Base = declarative_base()


class PrepareTable():
    def get_class(Base, table_name,column_name):
        class Demo(Base):
            def __init__(self):
                self.demo_c = column_name
                print("++++++++ {0}".format(self.demo_c))
            __tablename__ = table_name
            __table_args__ = {'extend_existing': True}
            id = Column(Integer(), primary_key=True)
            demo_1 = Column(String(45))
            
            
        return Demo 