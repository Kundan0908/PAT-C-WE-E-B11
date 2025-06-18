class Operator:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        return(self.x + other.x)

old_obj = Operator(10)
print(old_obj)
new_obj = Operator(20)
print(new_obj)
print(old_obj.__add__(new_obj))
