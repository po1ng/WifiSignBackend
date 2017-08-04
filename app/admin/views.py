import datetime
import time
from flask import render_template,request
from app.admin import admin
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

@admin.route('/')
def index():
    Class = BaseClass(class_number)
    return render_template('admin.html', Class=Class)


@admin.route('/list', methods=['POST', 'GET'])
def list_student():
    if request.method == 'GET':
        student_name = request.args.get('student_name')
    students = StudentInfo.objects(name=student_name)
    students_dic = {}
    student_list = []
    for student in students:
        student_dic = {}
        student_dic['name'] = student['name']
        student_dic['student_id'] = student['student_id']
        student_dic['class_id'] = student['class_id']
        student_dic['address_mac'] = student['address_mac']
        student_dic['connect_time'] = student['connect_time']
        student_dic['break_time'] = student['break_time']
        student_dic['date'] = student['date']
        student_dic['remarks'] = student['remarks']
        student_list.append(student_dic)

    students_dic['list'] = student_list
    jsonp = 'callback_info(%s)' % str(students_dic)
    return jsonp

@admin.route('/student_connect_status/data')
def data():
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
    jsonp = 'callback_admin(%s)' % str(dic_all_students)

    return jsonp
