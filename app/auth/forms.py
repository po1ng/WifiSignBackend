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
from wtforms.validators import Required
from app.models.BaseUser import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
                           Required(), Length(1, 64),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                           'Usernames must have only letters, '
                           'numbers, dots or underscores')])
    password = PasswordField('Password',
                             validators=[Required(),
                             EqualTo('password2', 'Password must match')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Register')
    class_number = StringField('Class Number',
                               validators=[Required(),
                               Regexp('^[0-9]',0,'Class number must have only numbers')])
    nickname = StringField('Nickname',
                           validators=[Required(), Length(1, 64),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                           'Nickname must have only letters, '
                           'numbers, dots or underscores')])

    def validate_email(self, field):
        if User.objects(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_nickname(self, field):
        if User.objects(nickname=field.data).first():
            raise ValidationError('Nickname already in use.')
