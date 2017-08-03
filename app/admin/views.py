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
        student_dic['status'] = student['status']
        student_dic['date'] = student['date']
        students_dic['remarks'] = student['remarks']
        student_list.append(student_dic)

    students_dic['list'] = student_list
    jsonp = 'callback(%s)' % str(students_dic)
    return jsonp
