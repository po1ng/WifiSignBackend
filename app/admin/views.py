from app.admin import admin
from app.models.BaseClass import BaseClass
from app.models.StudentsBase import Students
from flask import render_template,request
from config import CLASS_NUMBER


class_number = CLASS_NUMBER

@admin.route('/')
def index():
    Class = BaseClass(class_number)
    return render_template('index.html', Class=Class)


@admin.route('/list',methods = ['POST','GET'])
def list():
    # student_name = '程东东'
    if request.method == 'POST':
        student_name = request.form['student_name']
    # if request.method == 'GET':
    #     student_name = request.args.get('student_name')
    student = Students.objects(student_name=student_name)
    print(student)
    print(type(student))

    list = {}
    for each in student:
        list[each['student_name']] = 0
        list[each['student_id']] = 0
        list[each['class_num']] = 0
        list[each['time_start']] = 0
        list[each['time_end']] = 0
        list[each['tip']] = 0

    jsonp = 'callback' + '(' + str(list) + ')'
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