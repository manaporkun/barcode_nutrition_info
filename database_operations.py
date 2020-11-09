import pymongo


class MongoDB:

    def __init__(self, db_name, table_name):
        self.client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.gjh1q.mongodb.net/{}?retryWrites=true&w=majority".format('orkunmanap', 'yyuKFj15rIG7Yx0l', db_name))
        self.db = self.client[db_name]
        self.column = self.db[table_name]

    def get(self, query):
        return self.column.find(query)

    def push(self, data):
        return self.column.insert(data)
    
    def delete(self, query):
        return self.column.delete_one(query)

    def if_exists_db(self, db_name):
        dblist = self.client.list_database_names()
        return True if db_name in dblist else False

    def if_exists_table(self, table_name):
        collist = self.db.list_collection_names()
        return True if table_name in collist else False
