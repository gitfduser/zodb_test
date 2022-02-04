import ZODB
import ZODB.FileStorage
import persistent
from ast import List, Tuple

def get_db_connection()->Tuple:
    storage = ZODB.FileStorage.FileStorage("Data/mydata.fs")
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    return connection,root



class Being(persistent.Persistent):
    pass

class Employee(Being):
    def __init__(self, name):
        self.name = name
        self.relation = []
        self.relation_type = []








