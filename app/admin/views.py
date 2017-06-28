from app.admin import admin
from app.models.BaseClass import BaseClass
from app.models.StudentsBase import Students
from flask import render_template,request
from config import CLASS_NUMBER


class_number = CLASS_NUMBER

@admin.route('/')
def index():
    Class = BaseClass(class_number)
    return render_template('admin.html', Class=Class)


@admin.route('/list',methods = ['POST','GET'])
def list():
    # student_name = '程东东'
    # if request.method == 'POST':
    #     student_name = request.form['student_name']
    if request.method == 'GET':
        student_name = request.args.get('student_name')
    students = Students.objects(student_name=student_name)
    print(students)
    print(type(students))

    students_dic = {}
    list = []
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
        list.append(student_dic)

    students_dic['list'] = list
    print(students_dic)

    jsonp = 'callback' + '(' + str(students_dic) + ')'
    return jsonp

# def save():
#     student_name = request.form['student_name']
#     student_id = request.form['student_id']
#     class_num = request.form['class_num']
#     tip = request.form['tip']
#
#     student = Students(
#                        student_name=student_name,
#                        student_id = student_id,
#                        class_num = class_num,
#                        tip = tip
#                        )
#     student.save()