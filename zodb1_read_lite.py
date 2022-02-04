# %%
from utils_sql import get_db_connection, Employee, find_employee
import transaction

#%%
# get a db connection
connection, root = get_db_connection()

# Retrieving humans from the database
#%%
employees = root.employees
#%%

jim = find_employee("Jim", employees)
#%%
john = find_employee("John", employees)
#%%
jane = find_employee("Jane", employees)
jane
#%%
for employee in employees:
    print(
        f"{employee.name}'s relation, {employee.relation[0].name} as  {employee.relation_type[0]}"
    )
#%%
print(f"Jim has {jim.relation[1].name} as {jim.relation_type[1]}")
# %%
# close database connection
connection.close()

# %%
