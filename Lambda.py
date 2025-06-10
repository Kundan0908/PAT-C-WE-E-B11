# lambda function -> Lambda is an anonymous function that is created to perform a single operation
# they are created by using keyword lambda
# cannot be used for condition filtering, if, elif, else

# print square of a number
obj = lambda x:x**2  #-> lambda argument:expression
obj(2)  #-- create a variable to store lambda function
        # -- to call/ to run lambda function -> call variable with argument value

def square_of_number(y):
    return(y**2)

var = square_of_number(3)
# you need to create structure of normal function with steps
# to call/to run normal function -> call the function with its name and argument value


# adding of two number
obj_ = lambda x,y:x+y
print(obj_(x=2,y=3))

