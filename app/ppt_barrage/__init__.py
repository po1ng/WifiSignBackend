from flask import Blueprint

ppt_barrages = Blueprint('ppt_barrage',__name__,url_prefix='/ppt_barrage',template_folder='templates',static_folder='static')

from . import  views