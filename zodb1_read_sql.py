# %%
from utils import get_db_connection, Employee, find_employee
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
# display jim's relations
jim.display_relations()
#%%
john = find_employee("John", employees)
#%%
# display john's relations
#%%
john.display_relations()
#%%
jane = find_employee("Jane", employees)
#%%
# display jane's relations
#%%
jane.display_relations()
#%%

connection.close()

# %%
