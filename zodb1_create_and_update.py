# %%
import transaction
from utils import get_db_connection, Employee, zap_employees

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
root.employees = [john, jim]

#%%
# can we establish a relation between jim and john?
john.relation.append(jim)
john.relation_type.append("friend")

#%%
transaction.commit()
#%%

#%%
jim.relation.append(john)
jim.relation_type.append("friend")

#%%
transaction.commit()

#%%
# print humans' relations
print(f"John has {john.relation[0].name} as {john.relation_type[0]}")
print(f"Jim has {jim.relation[0].name} as {jim.relation_type[0]}")
#%%
# Say hello to jane
jane = Employee(name="Jane")
#%%
# jim and jane got married
jane.relation.append(jim)
jane.relation_type.append("spouse")
#%%
root.employees.append(jane)
#%%
#transaction.commit()

#%%
jim.relation.append(jane)
jim.relation_type.append("spouse")

#%%
transaction.commit()

# close database connection
connection.close()

# %%
