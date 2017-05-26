from app.__init__ import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Document):
    username = db.StringField()
    password_hash = db.StringField()
    email = db.StringField()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


