from app.models.MongodbConn import MongoPipeline

class PublicBoard():

    def __init__(self,content):
        self.content = content

    def leaving_messages(self):
        conn = MongoPipeline()
        conn.open_connection('public_message')

        dic_message = {}
        dic_message['content'] = self.content

