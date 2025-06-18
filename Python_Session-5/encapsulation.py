class ABC:
    def __init__(self,a,b):
        self._a = a
        self.b = b

    def print_details(self):
        print(self._a,self.b)

class DEF(ABC):
    def __init__(self,a,b):
        ABC.__init__(self,a,b)

    def print_details(self):
        print(self._a,self.b)

obj = DEF(10,20)
# obj = ABC(10,20)
print(obj.print_details())