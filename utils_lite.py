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


def get_db_connection() -> Tuple:
    db = ZODB.config.databaseFromString(zodb_config)
    connection = db.open()
    root = connection.root
    return connection, root


class Employee(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.relation = []
        self.relation_type = []

    def add_relation(self, employee, relation_type: str):
        self.relation.append(employee)
        self.relation_type.append(relation_type)
        self._p_changed = 1

    def display_relations(self):
        for i in range(len(self.relation)):
            print(
                f"{self.name} has a relation with {self.relation[i].name} as {self.relation_type[i]} "
            )

    def say_hi(self):
        print(f"Hi, I'm {self.name}")


def find_employee(name: str, employees) -> Employee:
    return [item for item in employees if item.name == name][0]


def zap_employees():
    connection, root = get_db_connection()
    root.employees = []
    transaction.commit()
    connection.close()

