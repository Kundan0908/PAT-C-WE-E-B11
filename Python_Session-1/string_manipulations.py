# String manipulations -> whatever written in a single or a double quote is knows as string.
#                         Manipulation is how to play with string.

# name = "kundan_" # -> pos 0:k, pos 1:u,pos 2:n ---
# print(len(name)) # len() will count the length of strings
# print(name.count('u'))
# print(name.capitalize())
# # string slicing -> it is denoted by [start:stop:step], for positive number, slicing first index pos is 0
# print(name[:5])
# print(name[0:5:2]) # -> 0 -> k
#                    # -> 0+5 -> n
#                    # -> 2+2 -> a
#                    # -> 4+2 ->
#
# print(name[::-1]) # -> -1=-1, -1+-1=-2, -2+-1 =-3
# print(name[-1:-8:-1]) # -> -1=-1, -1+-1=-2, -2+-1 =-3, -3+-1=-4,-4+-1=-5-----,-7+-1=-8

shape = 'Triangle' # ->'n','a'
# In positive string slicing, by default value is set which, start=0, stop= till last index pos,step = 1
# In negative string slicing, there is no by default value.. we need to always specify, step value with negative integer

# print(shape[-4])