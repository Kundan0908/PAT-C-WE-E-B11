# Method Types
# Instance Methods -> Takes self keyword as argument, this belongs to instance of class (obj)
# Class Methods -> Takes cls keyword as argument, It is declared by using tag @class method.
# Static Method -> It is an independent method which do not take any self or cls argument. It is declared by using tag @static method.

from datetime import datetime
class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age

    def display_details(self):  #-> Instance method
        return f"Hi! My name is {self.name} and i'm {self.age} years old"

    @classmethod #-> Class method
    def Age_at_year (cls,name,year):
        return cls(name,datetime.today().year-year)

    @staticmethod #-> Does not use and tagging arguments
    def isAdult(age):
        return age >= 18

person_details_1 = Person('XYZ',25)
print(person_details_1.display_details())
# print(person_details_1.isAdult(25))

person_details_2 = Person.Age_at_year('ABC',2021)
print(person_details_2.display_details())
# print(person_details_2)
# new_age = person_details_2.age
# print(person_details_2.isAdult(new_age))





















#
# class MyClass:
#     strength = 0
#     def __init__(self, batch):
#         self.batch = batch
#
#     def display_details(self):
#         print(self.batch)
#
#     @classmethod
#     def my_class_method(cls,new_strength):
#         cls.strength = new_strength
#         return cls.strength
#
#     def display_details(self):
#         print("Hello")
#
#     @staticmethod
#     def role(role):
#         return("the role is",role)
#
#
# obj = MyClass("B11")
# new_obj = MyClass('B12')
# print(obj.strength)
# obj.my_class_method(10)
# print(new_obj.strength)
# print(obj.role('mentor'))