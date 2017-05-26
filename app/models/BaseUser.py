from app import db
from flask_login import UserMixin

class User(UserMixin,db):
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()


