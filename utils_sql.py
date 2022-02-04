import ZODB.config
import persistent
from ast import List, Tuple
import relstorage
import transaction

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

class Employee(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.relation = []
        self.relation_type = []

def find_employee(name: str, employees) -> Employee:
    return [item for item in employees if item.name == name][0]

def zap_employees():
    connection, root = get_db_connection()
    root.employees=[]
    transaction.commit()
    connection.close()






