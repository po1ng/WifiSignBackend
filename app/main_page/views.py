from . import main_page
from app.models.BaseClass import BaseClass
from flask import  render_template

@main_page.route('/')
def main_page():
    Class = BaseClass(21,5,'2017-05-20')
    return render_template('index.html',Class=Class)

