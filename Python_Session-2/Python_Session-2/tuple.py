# tuple is a data type. -> immutable data type --> It can store elements/items of any other data type
# including another tuple aswell, it is enclosed by () and comma seprated.

# creating a tuple
tuple_ = ('fruits',3,True,2.99,['hello','world'])
new_tuple = ('new','tuple')
print(tuple_)

# Accessing a tuple
print(tuple_.count(['hello','world']))
print(tuple_.index(True))
print(tuple_.__add__(new_tuple))

# deleting a tuple
del tuple_ # Deletes entire tuple

# combination of 10, using 1,2,5,10
lst_1 = [1,2,3,4]
lst2_ = [3,4,5]
lst3_ = [5,6,7,4]
