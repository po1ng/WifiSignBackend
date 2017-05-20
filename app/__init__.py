from flask import Flask
from .main_page import main_page

app = Flask(__name__)

app.config.from_object(__name__)
app.register_blueprint(main_page)