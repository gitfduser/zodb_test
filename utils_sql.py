import ZODB.config
import persistent
from ast import List, Tuple
import relstorage


zodb_config = """
%import relstorage
<zodb main>
<relstorage>
    keep-history false
    cache-local-mb 0
    <sqlite3>
       data-dir Data/sqlite
    </sqlite3>
</relstorage>
</zodb>"""

def get_db_connection()->Tuple:
    db = ZODB.config.databaseFromString(zodb_config)
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








