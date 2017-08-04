from flask import flash
from flask import jsonify
from .forms import LoginForm, RegistrationForm
from flask import render_template
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.utils import response_dict
from app.models.BaseUser import User
from app.constants import EMAIL_USED, NICKNAME_USED, SUCCESS
from . import auth as auth_Blueprint


@auth_Blueprint.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


@auth_Blueprint.route('/')
def index():
    return render_template('index.html')


@auth_Blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return '登录失败'
    return '登录成功'


@auth_Blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate:
        user = User(email=form.email.data,
                    username=form.username.data,
                    class_number=form.class_number.data,
                    nickname=form.nickname.data)
        user.password = form.password.data
        if form.validate_email(form.email.data):
            return jsonify(response_dict(EMAIL_USED))
        elif form.validate_nickname(form.nickname.data):
            return jsonify(response_dict(NICKNAME_USED))
        else:
            return jsonify(response_dict(SUCCESS))
    else:
        return '注册失败！'



@auth_Blueprint.route('/logout')
# @login_required
def logout():
    # logout_user()
    # flash('You have been logged out.')
    # return render_template('index.html')
    return 'hello logout'

