from app.models.MongodbConn import MongoPipeline


class RankList(object):

    def __init__(self, date, class_id, class_num):
        self.rank_day_time = self.day_class_time(date, class_id, class_num)

    # date，日期;class_id，班级序号;class_num，课程编号
    def day_class_time(self, date, class_id, class_num):
        conn = MongoPipeline()
        conn.open_connection('qiandao_last_info')
        students_info = conn.getIds('info', {'date':date, 'class_id':class_id,
                                            'class_num':class_num})
        students_time = {}
        for student in students_info:
            name = student['name']
            connect_time = student['connect_time']
            students_time[name] = connect_time

        sort_students_time = sorted(students_time.items(),
                                    key=lambda b:b[1],
                                    reverse=True)
        rank_students_time = {}
        for i, e in enumerate(sort_students_time):
            if i == 10:
                break
            rank_students_time[e[0]] = e[1]

        sort_rank_students = sorted(rank_students_time.items(),
                                    key=lambda b:b[1],
                                    reverse=True)
        return sort_rank_students


