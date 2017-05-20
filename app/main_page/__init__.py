from flask import Blueprint

main_page = Blueprint('main_page',__name__,url_prefix='/main_page',template_folder='templates')

from . import views