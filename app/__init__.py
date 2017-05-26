from flask import Flask
from .main_page import main_page
from .ppt_barrage import ppt_barrage
from .auth import auth
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(__name__)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = './static/doc'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹

app.config['SECRET_KEY'] = 'hard to guess'
app.register_blueprint(auth)

app.config['MONGODB_SETTINGS'] = {           #配置MongoDB
    'db': 'web',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

app.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return None

             #蓝图注册
app.register_blueprint(main_page)
app.register_blueprint(ppt_barrage)


