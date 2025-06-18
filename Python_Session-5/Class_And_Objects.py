# Class-> It is a blueprint for creating objects. It is a collection of objects. A class defines a set of attributes and methods that
# create objects can have.

# Created using class keyword
# attributes are variables that belong to a class
# attributes can be accessed using . operator

class Python:
    batch='B11'
    def __init__(self,name,role):
        self.name = name
        self.role = role

# Objects are implementation of a class and it holds its own data. It is a instance of a class.
# An object consists of state, behaviour,identity

obj = Python("Kundan","Mentor")
print(f"Hello!! My name is {obj.name} and I am a {obj.role} of batch {obj.batch}")

