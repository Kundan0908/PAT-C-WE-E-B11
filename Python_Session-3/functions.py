# Functions -> It is piece of code that is created for performing a specific task.
# Functions are reusable piece of code.
# Functions are created with keyword 'def'
# In python, everything is a object
# for a function to execute we need to call it with its object name
# Types of functions:
    # keyword arguments -> It contains keywords passed as a parameter/argument.
    # positional arguments -> It contains values passed to arguments in an order
    # Default arguments -> It contains a default value assigned to a argument/parameter
    # Variable-length arguments -> It contains arguments of n length

# keyword arguments
def keyword_argument_func(name,role):
    print(f"My name is {name} and I am a {role}")

keyword_argument_func(name='Kundan',role='Mentor')

# positional arguments
def positional_arguments_func(role,name):
    print(f"My name is {name} and I am a {role}")

positional_arguments_func('Mentor','Kundan')

# Default arguments
def default_arguments_func(name,role='Mentor'):
    print(f"My name is {name} and I am a {role}")

default_arguments_func('Kundan')

# # Variable-length arguments
def Variable_length_arguments_func(*args):
    print(args)

Variable_length_arguments_func('Kundan','Mentor')

def My_dict_func(**kwargs):
    print(kwargs)

My_dict_func(name='kundan',role='mentor',experience = 7)

# Return Values
def Return_sum_func(a,b):
    return a+b

print(Return_sum_func(10,20))











