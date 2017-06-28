from app import db
from datetime import datetime


class Students(db.Document):
    student_name = db.StringField(required = True,max_length = 20)
    student_id = db.IntField(required = True)
    class_num = db.IntField(required = True)
    time_start = db.StringField()
    time_end = db.StringField()
    tip = db.StringField()

