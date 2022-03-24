from crypt import methods
import json
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import declarative_base
from src.DataModel.demo import PrepareTable
from src.services.db import Session

demo_service = Blueprint('src/services/demo_service',__name__)


@demo_service.get('/demo')
def demo_ser():
    db_sessoin = Session()
    Base = declarative_base()
    table_name = PrepareTable.get_class(Base,"demo","demo_1")
    data = db_sessoin.query(table_name)
    li = []
    for i in data:
        li.append({"id":i.id,"demo_1":i.demo_1})
    return jsonify(li)

