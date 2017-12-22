from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from app import login_manager
from app import db


class User(UserMixin, db.Document):

    username = db.StringField()
    password_hash = db.StringField()
    email = db.StringField()
    class_id = db.StringField()
    nickname = db.StringField()
    last_seen = db.DateTimeField(default=datetime.now())

    def ping(self):
        self.last_seen = datetime.now()
        user = User.objects(username=self.username)
        user.update(last_seen=self.last_seen)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()