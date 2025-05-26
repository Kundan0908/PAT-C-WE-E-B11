# list is a data type. -> mutable data type --> It can store elements/items of any other data type
# including another list aswell, it is enclosed by [] and comma seprated

# creating a list
list_ = ['fruits',3,True,2.99,['hello','world']]

# Adding items to a list
list_.insert(0,'Vegetable') # -> adding element at a specific index pos
list_.append(2+3j) # -> adding element at the end
list_.extend([2,3,4])

# Removing items from a list
print(list_.pop(5)) # -> removing item from list using index pos
list_.remove(True) # -> Removing item from list using value
print(list_)
# del list_[::] # -> Deleting item from list using index pos

# Operations to be done on list
print(len(list_))
print(list_.count('fruits'))
new_list = [1,10,2,3,7]
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)



