from . import auth as auth_Blueprint
from flask import render_template
from .forms import LoginForm


@auth_Blueprint.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    return render_template('login.html',form=form)
