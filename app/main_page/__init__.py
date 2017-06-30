from flask import Blueprint

main_page = Blueprint('main_page',
                      __name__,
                      url_prefix='/main_page',
                      template_folder='templates',
                      static_folder='assets')

from . import views