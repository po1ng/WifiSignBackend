from flask_wtf import Form
from wtforms import ValidationError
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import DataRequired
from app.models.BaseUser import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
                           DataRequired(), Length(1, 64),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                           'Usernames must have only letters, '
                           'numbers, dots or underscores')])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                             EqualTo('password2', 'Password must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    class_number = StringField('Class Number',
                               validators=[DataRequired(),
                               Regexp('^[0-9]',0,'Class number must have only numbers')])
    nickname = StringField('Nickname',
                           validators=[DataRequired(), Length(1, 64),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                           'Nickname must have only letters, '
                           'numbers, dots or underscores')])
    class_id = StringField(validators=[DataRequired()])

    def validate_email(self, email):
        if User.objects(email=email).first():
            return True

    def validate_nickname(self, nickname):
        if User.objects(nickname=nickname).first():
            return True
