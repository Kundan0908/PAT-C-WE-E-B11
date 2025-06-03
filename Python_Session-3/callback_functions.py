# A callback function in Python is a function that is passed as an argument to another function.

def func1():
    print("I am from func1")

def func2():
    print("I am from func2")

def main_func(func):  # -> a,b,c
    print("I am from main func")
    func()

main_func(func2)




















# # def function1():
# #     print("This is me from function 1")
# #     print(function2())
# #
# # def function2():
# #     return "This is me from function 2"
#
#
# def my_operator_func(a,b,func):
#     print(func(a,b))
#
# def sum(x,y): # callback functions
#     return x+y
#
# def subtract(x,y): # callback functions
#     return x - y
#
# my_operator_func(a=10,b=20,func=subtract)