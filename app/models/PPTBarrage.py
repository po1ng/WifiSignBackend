from app import db

class Barrage(db.Document):
    barrage_text = db.StringField()
    barrage_time = db.StringField()
    ppt_name = db.StringField()