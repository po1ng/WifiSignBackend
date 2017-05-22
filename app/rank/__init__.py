from flask import Blueprint

rank = Blueprint('rank',__name__,url_prefix='/rank',template_folder='templates')

from . import views