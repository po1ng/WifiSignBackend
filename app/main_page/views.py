from flask import abort
from flask import request
from flask import  render_template
from flask import jsonify
from flask_login import login_required
from app.models.BaseUser import User
from app.main_page import main_page as main_page_Blueprint
from app.models.BaseClass import BaseClass
from config import CLASS_NUMBER

class_number = CLASS_NUMBER


@main_page_Blueprint.route('/')
def main_page():
    Class = BaseClass(class_number)
    return render_template('index.html', Class=Class)


@main_page_Blueprint.route('/student/<username>')
@login_required
def student(username):
    student = User.objects(username=username).first()
    if student is None:
        abort(404)
    return render_template('student_home.html', student=student)


@main_page_Blueprint.route('/teacher')
def teacher():
    base_class = BaseClass(class_number)
    list_sign_students = base_class.list_sign_students
    list_unsign_students = base_class.list_unsign_students
    dic_all_students = {}
    for student in list_sign_students:
        dic_all_students[student] = 1
    for student in list_unsign_students:
        dic_all_students[student] = 0
    return render_template('teacher.html', dic_all_students=dic_all_students)


@main_page_Blueprint.route('/data')
def data():
    base_class = BaseClass(class_number)
    list_sign_students = base_class.list_sign_students
    list_unsign_students = base_class.list_unsign_students
    dic_all_students = {}
    for student in list_sign_students:
        dic_all_students[student] = 1
    for student in list_unsign_students:
        dic_all_students[student] = 0
    return jsonify(dic_all_students)


@main_page_Blueprint.route('/front/data')
def front_data():
    class_number = CLASS_NUMBER
    if request.args.get('class_number'):
        class_number = request.args.get('class_number')
    if type(class_number) is not None and type(class_number) is not int:
        class_number = int(class_number)
    base_class = BaseClass(class_number)
    list_sign_students = base_class.list_sign_students
    list_unsign_students = base_class.list_unsign_students
    dic_all_students = {}
    for student in list_sign_students:
        dic_all_students[student] = 1
    for student in list_unsign_students:
        dic_all_students[student] = 0
    jsonp = 'callback(%s)' % str(dic_all_students)

    return jsonp
