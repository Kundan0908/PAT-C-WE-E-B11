# Map class takes function and iterables as the input parameters,
# It applies function steps to each value of a iterable

lst = [10,2,3,4]
obj = lambda x:x**2
my_map = map(obj,lst)
print(my_map)
print(tuple(my_map))

lst_ = [False,2,3,4,5]
def filter_even(x):
    if x % 2 == 0:
        return True

result = filter(None,lst_)
print(list(result))














# Map functions -> It applies a given function to each item of an iterable(list,tuple, etc) and returns an iterators that
# yield the result.
# map(function,iterable)
# It returns a map object

# numbers = [1, 2, 3, 4]
# squares = map(lambda x: x**2, numbers)
# print(list(squares))  # Output: [1, 4, 9, 16


# The filter() function in Python is a built-in function
# that filters elements from an iterable based on a given function.
#  It takes two arguments:
# function: A function that tests each element of the iterable. It should return True if the element should be included in the result, and False otherwise.
# iterable: The iterable to be filtered (e.g., list, tuple, set).

# def is_even(num):
#     return num % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers)) # Output: [2, 4, 6]
