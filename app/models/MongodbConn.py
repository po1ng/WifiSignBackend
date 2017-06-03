# code=utf-8
import pymongo


class MongoPipeline:
    host = "127.0.0.1"
    port = 27017

    mongo_db ="zhihu"
    #     mongo_db = ""



    def open_connection(self, mongo_db,host = None,username = None,
                        password = None,ip = None):
        self.host = host
        if self.host != None:
            command =  'mongodb://' + username + ':' + password + '@' + ip + ':27017'
            self.client = pymongo.MongoClient(command)
            self.db = self.client[mongo_db]
        else:
            self.client = pymongo.MongoClient(self.host, self.port)
            self.db = self.client[mongo_db]

    def close_connection(self):
        self.client.close()

    def process_item(self, item, collection_name):
        try:
            self.db[collection_name].insert(item)
            return item
        except Exception as e:
            pass
            #print e
            
    def update_item(self,query, item, collection_name):
            try:
                self.db[collection_name].update(query,item,False,True)
                # print('更新完成')
                return item
            except Exception as e:
                pass
                #print e    

    def pageget(self, start, limit, collection_name):
        collection = self.db[collection_name]
        return collection.find().limit(limit).skip(start)

    def getIds(self, collection_name,find_dir):
        collection = self.db[collection_name]
        return collection.find(find_dir,no_cursor_timeout=True)

    def getIds_one(self, collection_name,find_dir):
            collection = self.db[collection_name]
            return collection.find_one(find_dir)    
    
    def GetNation(self, collection_name, k_dir):
        return self.db[collection_name].find_one(k_dir)

    def existsornot(self, collection_name, item):
        ting = self.db[collection_name].find(item)
        if ting == None:
            return 0
        else:
            return 1


if __name__ == "__main__":
    pass


