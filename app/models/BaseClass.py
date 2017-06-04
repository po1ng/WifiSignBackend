from app.models.MongodbConn import MongoPipeline

class BaseClass():
    # class_id,班级;class_num,课程编号
    def __init__(self, class_id):

        self.list_students = self.calculate_students(class_id=class_id)
        self.list_sign_students = self.calculate_sign_student(class_id)
        self.list_unsign_students = self.calculate_unsign_student(self.list_students,
                                                                  self.list_sign_students)
        self.total_student_num = len(self.list_students)
        self.sign_student_num = len(self.list_sign_students)
        self.unsign_student_num = self.total_student_num - self.sign_student_num

    # 该班级所有学生的名单
    def calculate_students(self,class_id):
        conn = MongoPipeline()
        conn.open_connection('web_info',username='pipi',password='123456',ip='localhost')
        students = conn.getIds('info',{"class_num":class_id})
        student_num = None
        list_students = []
        for student in students:
            list_students.append(student['name'])
        return list_students

    # 该班级，某一天，某一堂课签到学生的名单
    def calculate_sign_student(self,class_id):
        conn = MongoPipeline()
        conn.open_connection('web_info', username='pipi', password='123456', ip='localhost')
        students = conn.getIds('info',{'class_num':class_id})
        sign_student = []
        for student in students:
            if 'connect_status'in student and student['connect_status'] == 1:
                sign_student.append(student['name'])

        return sign_student

    # 返回没有签到的学生的名单
    def calculate_unsign_student(self,list_students,list_sign_students):
        list_unsign_students = list(set(list_students) - (set(list_students)&set(list_sign_students)))
        return list_unsign_students






if __name__ == '__main__':
    one = BaseClass(21,5,'2017-05-20')
    num = one.total_student_num
    print(num)
    print(one.list_students)
    print(one.sign_student_num)
    print(one.list_sign_students)
    print(one.list_unsign_students)
    print(one.unsign_student_num)
    judge = '万仕贤' in one.list_unsign_students
    print(judge)

