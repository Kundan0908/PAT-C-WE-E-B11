# loop -> loop is a concept that is used for iterating/moving to next element/items in any data type
from Tools.scripts.findnocoding import needs_declaration



# two types of loops
#     1. for loop
#     2. While loop

# approach 1
# for i in name:
#     print(i) ->'k'

# approach 2
# in any loop, two things are needs -> iterable, iterator
# range method always needs an integer input
# name = 'kundan'
# for i in range(len(name)):# start,stop,step --> range(6)-->[0,6,1]
#     print(name)#->0,1,2,3,4 -> 'k' -> name[4]
#     break

# for printing integer output we use range function/method
# for i in range(10):
#     print(i)

# for i in range(0,10,1):
#     print(i)
#     if i == 4:
#         break #-> breaks entire loop
#     print("Hello")
#     print("World")
#
# name = 'Me'
# for i in range(0,4,1):
#     print(i)
#     if i == 2
#         continue

# nested loops -> loop inside loop
# for i in range(5): #-> range(5) i -> 0 in ->(0,5,1)
#     print(i) #-> 0,1
#     for j in range(3): # -> range(3) j ->0  in ->(0,3,1) ->
#         print(j) # -> 0
#     break


# while loop
end_range = 10
start_range = 0
while start_range <= end_range: #-> 0 <= 10 -> True
    print(start_range)
    start_range += 1
