from app.models.MongodbConn import MongoPipeline

class BaseStudent(object):

    def __init__(self, name):
        self.student_info = self.query_basic_info(name=name)
        self.mac = self.student_info['mac']
        self.name = self.student_info['name']
        self.student_id = self.student_info['studentid']
        self.class_id = self.student_info['class_num']
        self.nickname = None

    def query_basic_info(self, name):
        conn = MongoPipeline()
        conn.open_connection('qiandao_mac_name')
        student_info = conn.getIds_one('info', {'name': name})
        return student_info



