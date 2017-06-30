from .forms import LoginForm,RegistrationForm
from flask import redirect
from flask import render_template
from flask import url_for
from flask import flash
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models.BaseUser import User
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
        user = User.objects(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect('/main_page/student/'+user.username)
    return render_template('login.html',form=form,user = current_user)


@auth_Blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
                    class_number=form.class_number.data,
                    nickname=form.nickname.data)
        user.password = form.password.data
        user.save()
        flash('注册成功！可以登录了！')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_Blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return render_template('index.html')

