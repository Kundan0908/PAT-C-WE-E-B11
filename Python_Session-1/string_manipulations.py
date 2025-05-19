# String manipulations -> whatever written in a single or a double quote is knows as string.
#                         Manipulation is how to play with string.

name = "kundan_" # -> pos 0:k, pos 1:u,pos 2:n ---
print(len(name)) # len() will count the length of strings
print(name.count('u'))
print(name.capitalize())
# string slicing -> it is denoted by [start:stop:step], for positive number, slicing first index pos is 0
print(name[:5])
print(name[0:5:2]) # -> 0 -> k
                   # -> 0+5 -> n
                   # -> 2+2 -> a
                   # -> 4+2 ->

# print(name[::-1]) # for reverse order, slicing first index pos is -1
