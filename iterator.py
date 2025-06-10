# an iterator is an object that enables traversal through the elements of a collection(like lists, tuples, dictionaries, sets, and strings) one at a time
# How it works:
# The iter() function is used to obtain an iterator object from an iterable.
# The next() function is used to retrieve the subsequent element from the iterator.
# When the iterator reaches the end of the sequence, the next() function raises StopIteration.

lst_ = [1,2,3,4,5,6,7,8] #-->
for i in lst_:
    print(i)

obj = iter(lst_)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


