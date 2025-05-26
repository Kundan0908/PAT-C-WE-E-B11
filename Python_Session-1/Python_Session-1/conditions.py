# conditions -> if, if-else, if-elif-else
a = 10
b = 20
if b > a :  # python check for condition b > a i.e.. 20 > 10, if it is true, the interpreter will go inside if blocl
    print('b is greater than a')
else: # python checks for if block comparison result, if it is 'false' then else block will get executed
    print('a is greater than b')

c = 30
if a > b :  # python check for condition b > a i.e.. 10 > 20, if it is true, the interpreter will go inside if blocl
    print('a is greater than b')
elif b > c: # python checks for if block comparison result, if it is 'false' then if will check for condition in elif block
    print('b is greater than c')
else: # python check for both if, elif condition if the result of both are false, then else block will get executed
    print('c is the greatest number')