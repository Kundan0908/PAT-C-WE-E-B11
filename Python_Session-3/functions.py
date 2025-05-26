# Functions are a piece of code, that is created for performing a particular task that can be reused again and again.
# Functions are created with keyword 'def'.
# Functions can be passed a parameter/ argument, without argument.

a = 10
b = 20
# print(a+b)
c = 30
# print(a+b+c)

def greet(name): # --> Something inside the () is known as argument/parameter
    print(f"Hello {name}, Welcome to this course of functions: - ")
#
# user_name = input("Enter your name")
# greet(user_name)

def addition_of_numbers(input): #-> *args is used when we have multiple inputs as parameter -> ()
    print(input)

string = 'hello'
addition_of_numbers(string)








