# A closure is created when a function (the inner function) is defined within another function (the outer function)
# and the inner function references variables from the outer function.
# Closures are useful when you need a function to retain state across multiple calls, without using global variables.
#
# def outer(a):
#     def inner(b):
#         print(a+b)
#     inner(20)
#
# outer(10)






def fun1():
    def fun2():
        print("I am from fun 2")
    print("I am from fun 1")
    return fun2()

def fun1(z):
    def fun2(y):
        print("I am from fun 2")
        return z + y
    print("I am from fun 1")
    return fun2

x = 10
y = 20
obj1 = fun1(x)
print(obj1)
print(obj1(y))