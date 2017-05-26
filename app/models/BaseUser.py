from app.__init__ import db
from flask_login import UserMixin

class User(UserMixin,db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()


