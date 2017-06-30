from flask import render_template,request
from app.admin import admin
from app.models.BaseClass import BaseClass
from app.models.StudentsBase import Students
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
    students = Students.objects(student_name=student_name)
    students_dic = {}
    student_list = []
    for student in students:
        student_dic = {}
        student_dic['number'] = student['number']
        student_dic['student_name'] = student['student_name']
        student_dic['student_id'] = student['student_id']
        student_dic['date'] = student['date']
        student_dic['time_start'] = student['time_start']
        student_dic['time_end'] = student['time_end']
        student_dic['time'] = student['time']
        student_dic['remarks'] = student['remarks']
        student_list.append(student_dic)

    students_dic['list'] = student_list
    jsonp = 'callback(%s)' % str(students_dic)
    return jsonp
