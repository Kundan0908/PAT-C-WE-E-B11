# dictionary is a data type. -> mutable data type --> It stores item in a key value pair
# it is enclosed by {'key':'value'} and comma seprated.
# keys will be unique i.e.. it can never be duplicate while values can be duplicate

dict_ = {'name':'kundan','role':'tutor','profession':'tutor'}
# Adding key:value to a dictionary
dict_['experience'] = 6
# print(dict_)

# Accessing values of a dictionary
# print(dict_['profession'])

# Accessing all keys of a dictionary items
# for i in dict_:
#     print(i)

# Accessing all values of a dictionary items
# for i in dict_: # -> i will fetch one key at a time -->{'name':'kundan','role':'tutor','profession':'tutor','experience':6}
#  # print( dict_['name'])
#     print(dict_[i])

 # Accessing both key,value of a dictionary items
# for key,value in dict_.items():
#     print(key,value)

# Deleting items from a dictionary
dict_.__delitem__('profession')
del dict_['experience']
dict_.pop('role')
dict_.popitem()
# dict_.clear()
print(dict_)
