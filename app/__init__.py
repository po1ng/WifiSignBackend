import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_mongoengine import MongoEngineSessionInterface
from flask_login import LoginManager

UPLOAD_FOLDER = './static/doc'
db = MongoEngine()
login_manager = LoginManager()
app_secret_key = os.environ['APP_SECRET_KEY']
mongo_db = os.environ['MONGO_DB']
mongo_host = os.environ['MONGO_HOST']
mongo_port = os.environ['MONGO_PORT']
mongo_username = os.environ['MONGO_USERNAME']
mongo_password = os.environ['MONGO_PASSWORD']

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    bootstrap = Bootstrap(app)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
    app.config['SECRET_KEY'] = 'hard to guess'
    app.config['MONGODB_SETTINGS'] = {  # 配置MongoDB
        'db': mongo_db,
        'host': mongo_host,
        'port': int(mongo_port),
        'username':mongo_username,
        'password':mongo_password
    }
    app.session_interface = MongoEngineSessionInterface(db)
    db.init_app(app)

    app.secret_key = app_secret_key
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .main_page import main_page
    app.register_blueprint(main_page)
    from .ppt_barrage import ppt_barrage
    app.register_blueprint(ppt_barrage)
    from .admin import admin
    app.register_blueprint(admin)
    from .auth import auth
    app.register_blueprint(auth)

    return app