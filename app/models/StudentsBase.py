from app import db


class Students(db.Document):
    number = db.IntField(required=True)
    student_name = db.StringField(required=True, max_length=30)
    student_id = db.IntField(required=True)
    date = db.StringField(required=True)
    time_start = db.StringField(required=True)
    time_end = db.StringField(required=True)
    time = db.StringField(required=True)
    remarks = db.StringField()