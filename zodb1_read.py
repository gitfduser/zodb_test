# %%
from utils import get_db_connection, Employee

#%%
def find_employee(name: str, employees):
    return [item for item in employees if item.name == name][0]


#%%
# get a db connection
connection, root = get_db_connection()

# Retrieving humans from the database
#%%
employees = root.employees
#%%

jim = find_employee("Jim", employees)
john = find_employee("John", employees)
jane = find_employee("Jane", employees)

for employee in employees:
    print(
        f"{employee.name}'s relation, {employee.relation[0].name} as  {employee.relation_type[0]}"
    )

# %%
# close database connection
connection.close()

# %%
