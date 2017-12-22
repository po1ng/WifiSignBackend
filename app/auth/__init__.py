from flask import Blueprint

auth = Blueprint('auth', __name__,
                 static_url_path='',
                 static_folder='static',
                 url_prefix='/auth')

from . import views