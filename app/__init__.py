from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_mongoengine import MongoEngineSessionInterface
from flask_login import LoginManager

UPLOAD_FOLDER = './static/doc'
db = MongoEngine()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    bootstrap = Bootstrap(app)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
    app.config['SECRET_KEY'] = 'hard to guess'
    app.config['MONGODB_SETTINGS'] = {  # 配置MongoDB
        'db': 'web',
        'host': '127.0.0.1',
        'port': 27017,
        'username':'pipi',
        'password':'123456'
    }
    app.session_interface = MongoEngineSessionInterface(db)
    db.init_app(app)

    app.secret_key = 's3cr3t'
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