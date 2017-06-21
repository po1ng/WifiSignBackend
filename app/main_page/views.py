from app.main_page import main_page as main_page_Blueprint
from app.models.BaseClass import BaseClass
from flask import  render_template,abort
from flask import jsonify
from config import CLASS_NUMBER
from app.models.BaseUser import User
from flask_login import login_required

class_number = CLASS_NUMBER

@main_page_Blueprint.route('/')
def main_page():
    Class = BaseClass(class_number)
    return render_template('index.html',Class=Class)

@main_page_Blueprint.route('/student/<username>')
@login_required
def student(username):
    student = User.objects(username = username).first()
    if student is None:
        abort(404)
    return render_template('student_home.html',student = student)


@main_page_Blueprint.route('/teacher')
def teacher():
    Class = BaseClass(class_number)
    list_sign_students = Class.list_sign_students
    list_unsign_students = Class.list_unsign_students
    dic_all_students = {}
    for student in list_sign_students:
        dic_all_students[student] = 1
    for student in list_unsign_students:
        dic_all_students[student] = 0
    print(dic_all_students)
    return render_template('teacher.html',dic_all_students = dic_all_students)

@main_page_Blueprint.route('/data')
def data():
    Class = BaseClass(class_number)

    list_sign_students = Class.list_sign_students
    list_unsign_students = Class.list_unsign_students
    dic_all_students = {}
    for student in list_sign_students:
        dic_all_students[student] = 1
    for student in list_unsign_students:
        dic_all_students[student] = 0
    return jsonify(dic_all_students)