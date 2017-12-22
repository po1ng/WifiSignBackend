import datetime
import time
from flask import abort
from flask import request
from flask import  render_template
from flask import jsonify
from flask_login import login_required
from app.models.BaseUser import User
from app.main_page import main_page as main_page_Blueprint
from app.models.BaseClass import BaseClass
from app.models.StudentInfo import StudentInfo
from config import CLASS_NUMBER

class_number = CLASS_NUMBER


def get_date():
    today_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return today_date


def get_now_datetime():
    now_hour = time.strftime('%H')
    now_min = time.strftime('%M')
    now_sec = time.strftime('%S')
    now_time = datetime.time(int(now_hour), int(now_min), int(now_sec))
    return now_time


def get_class_num():
    now_time = get_now_datetime()
    info = {}
    class_time_start_1 = datetime.time(8, 0, 0)
    class_time_end_1 = datetime.time(10, 0, 0)
    class_time_start_2 = datetime.time(10, 5, 0)
    class_time_end_2 = datetime.time(12, 0, 0)
    class_time_start_3 = datetime.time(14, 30, 0)
    class_time_end_3 = datetime.time(16, 0, 0)
    class_time_start_4 = datetime.time(16, 0, 0)
    class_time_end_4 = datetime.time(18, 0, 0)
    if now_time > class_time_start_1 and now_time < class_time_end_1:
        info['class_num'] = '1'
    elif now_time > class_time_start_2 and now_time < class_time_end_2:
        info['class_num'] = '2'
    elif now_time > class_time_start_3 and now_time < class_time_end_3:
        info['class_num'] = '3'
    elif now_time > class_time_start_4 and now_time < class_time_end_4:
        info['class_num'] = '4'
    else:
        info['class_num'] = '5'
    return info['class_num']

@main_page_Blueprint.route('/')
def main_page():
    Class = BaseClass(class_number)
    return render_template('wa_admin.html', Class=Class)


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


@main_page_Blueprint.route('/student_connect_status/data')
def front_data():
    class_id = '12'
    if request.args.get('class_number'):
        class_id = request.args.get('class_number')
    today_date = get_date()
    class_num = get_class_num()
    dic_all_students = {}
    students_info_absent = StudentInfo.objects(class_id=class_id)
    for student_info_absent in students_info_absent:
        name = student_info_absent['name']
        dic_all_students[name] = 0
    students_info = StudentInfo.objects(class_id=class_id, class_num=class_num, date=today_date)
    for student_info in students_info:
        name = student_info['name']
        dic_all_students[name] = int(student_info['status'])
    jsonp = 'callback_teacher(%s)' % str(dic_all_students)

    return jsonp
