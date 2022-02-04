# %%
import transaction
from utils_sql import get_db_connection, Employee, zap_employees, find_employee

#%%
zap_employees()
# %%
# say hello to John and Jim
john = Employee(name="John")
jim = Employee(name="Jim")

#%%
# get a db connection
connection, root = get_db_connection()

#%%
# add employees to the database
employees = [john, jim]

#%%
# can we establish a relation between jim and john?
john.relation.append(jim)
john.relation_type.append("friend")

#%%
jim.relation.append(john)

jim.relation_type.append("friend")
#%%
# print employees relations
print(f"John has {john.relation[0].name} as {john.relation_type[0]}")
print(f"Jim has {jim.relation[0].name} as {jim.relation_type[0]}")
#%%
root.employees = employees
#%%
transaction.commit()
#%%

#%%
# Say hello to jane
jane = Employee(name="Jane")
jane
#%%
# add jane to humans in the database
employees.append(jane)
#%%
root.employees = employees
#%%
transaction.commit()
connection.close()
#%%
#%%
# get a db connection
connection, root = get_db_connection()
#%%
employees = root.employees
#%%
jim = find_employee("Jim", employees)
jane = find_employee("Jane", employees)
#%%
# jim and jane got married
jane.relation.append(jim)
jane.relation_type.append("spouse")
jane._p_changed = 1
#%%
transaction.commit()

#%%
jim.relation.append(jane)
jim.relation_type.append("spouse")
jim._p_changed = 1
#%%
print(f"Jane has {jane.relation[0].name} as {jane.relation_type[0]}")
#%%
# store data in the database
transaction.commit()
# %%
# close database connection
connection.close()
#%%

