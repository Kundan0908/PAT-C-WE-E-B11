# decorators are used to call another function from a calling function. It is used to modify the behaviour of existing fucntion

def func1(func):
    print("I am from function 1")
    def func2():
        print("I am from function2")
        func()
    return func2
@func1
def func3():
    print("I am from func 3")

func3()

# def func1(func):
#     print("I am from func1")
#     def wrapper_func(x,y):
#         print("I am from wrapper_func")
#         return func(x,y)
#     return wrapper_func
#
# @func1
# def my_new_func(a,b):
#     return a+b
#
# obj = func1(my_new_func)
#
# print(my_new_func(10,20))
