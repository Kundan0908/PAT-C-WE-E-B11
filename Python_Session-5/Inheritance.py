# Single Inheritance
class Guvi:
    def __init__(self,course):
        self.course = course

    def display_details(self):
        print("Welcome!!, to course",self.course)

class Batch(Guvi):
    def __init__(self,batch,course):
        self.batch = batch
        Guvi.__init__(self,course)
    def Batch_details(self):
        print("This is batch",self.batch)


obj = Batch('B11',"PAT")
obj.display_details()
obj.Batch_details()


# Multiple Inheritance
class Guvi:
    def display_details(self):
        print("Welcome!!,Guvi Learners")

class Course(Guvi):
    def __init__(self,course):
        self.course = course

    def Batch_details(self):
        print("You have registered for: ",self.course)

class Batch(Course):
    def __init__(self,batch,course):
        self.batch = batch
        Course.__init__(self,course)

    def Course_details(self):
        print("And you are enrolled in batch: ",self.batch)

obj = Batch('B11',"PAT")
obj.display_details()
obj.Batch_details()
obj.Course_details()



# Multilevel Inheritance
class Guvi:
    def __init__(self, course):
        self.course = course

class Batch:
    def __init__(self, batch):
        self.batch = batch

class Role(Guvi,Batch):
    def __init__(self,role,course,batch):
        self.role = role
        Batch.__init__(self,batch)
        Guvi.__init__(self,course)

    def display_details(self):
        print(self.course,self.batch,self.role)

new_obj = Role("Mentor","B11","PAT")
new_obj.display_details()
