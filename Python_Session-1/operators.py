# Arithmetic operators -> +,-,*,/,//-> floor division, %
a = 20
b = 10
# print(a + b) # -> 30
# print(a - b) # -> -10
# print(a * b) # -> 200
# print(a / b) # -> 2.0
# print(a // b) # -> 2
# print(a % b) #  -> 0

# comparison operators -> ==, =, >, <, !=, >=,<=
c = 30
# print(c)
# print(a == c) # python check for '==' value assigned ->(20 equals to 30)
# print(a > b)
# print(a != b) # python check for '!=' value assigned ->(20 not equals to 30)

# membership operators -> in, not in
lst = [10,20]
# print(10 in lst) # python check for value 10 inside variable lst having values stored [10,20]
# print(20 not in lst) # python check for value 20 not inside variable lst having values stored [10,20]

# identity operators -> is, is not
d = 40
e = 50

print(id(d),id(e))
print(d is e) # python checks for address of the variable is same
print(d is not e) # python checks for address of the variable not same