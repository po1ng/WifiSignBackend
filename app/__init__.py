from flask import Flask
from .main_page import main_page
from .ppt_barrage import ppt_barrage
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = './static/doc'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹


app.config.from_object(__name__)
app.register_blueprint(main_page)
app.register_blueprint(ppt_barrage)