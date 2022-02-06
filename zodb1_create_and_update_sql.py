# %%
import transaction
from utils_sql import get_db_connection, Employee, zap_employees, find_employee

#%%
# open the database and delete all employees in the database if any
zap_employees()
# %%
# say hello to John and Jim
john = Employee(name="John")
john.say_hi()
#%%
jim = Employee(name="Jim")
jim.say_hi()
#%%
# get a db connection
connection, root = get_db_connection()

#%%
# add employees to the database
employees = [john, jim]

#%%
# can we establish a relation between jim and john?
john.add_relation(jim, "friend")

#%%
jim.add_relation(john, "friend")

# jim and john are now friends
#%%
# print employees relations
john.display_relations()
jim.display_relations()
#%%
root.employees = employees
#%%
transaction.commit()
#%%

#%%
# Say hello to jane
jane = Employee(name="Jane")
jane.say_hi()
#%%
# add jane to employees in the database
employees.append(jane)
#%%
root.employees = employees
#%%
# commit changes in transaction and close database
transaction.commit()
connection.close()
#%%
# let's open the database
# get a db connection
connection, root = get_db_connection()
#%%
employees = root.employees
#%%
# retrieve jim and john employees
jim = find_employee("Jim", employees)
jane = find_employee("Jane", employees)
#%%
# jim and jane get married
jane.add_relation(jim, "spouse")
# display jane's relations
jane.display_relations()
#%%
# commit changes to the database
transaction.commit()

#%%
jim.add_relation(jane, "spouse")
#%%
# display jim's relations
jim.display_relations()
#%%

#%%
# store data in the database
transaction.commit()
# %%
# close database connection
connection.close()
#%%

