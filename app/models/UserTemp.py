from flask_login import UserMixin


class UserTemp(UserMixin):
    def __init__(self, id):
        self.id = str(id)

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)