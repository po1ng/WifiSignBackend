from flask import render_template,request
from app.admin import admin
from app.models.BaseClass import BaseClass
from app.models.StudentInfo import StudentInfo
from config import CLASS_NUMBER


class_number = CLASS_NUMBER


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
    dic_all_students = {}
    students_info = StudentInfo.objects(class_id=class_id)
    for student_info in students_info:
        name = student_info['name']
        dic_all_students[name] = int(student_info['status'])
    jsonp = 'callback_admin(%s)' % str(dic_all_students)

    return jsonp
