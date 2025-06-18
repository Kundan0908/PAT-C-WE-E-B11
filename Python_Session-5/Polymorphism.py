# Polymorphism -> Poly-> Means more than and Phism -> Form

class Bird:
    def Can_fly(self):
        return "All birds can fly"

class Ostrich(Bird):
    def Can_fly(self):
        return "Ostrich is a type of bird that cannot fly"

bird_obj = Ostrich()
print(bird_obj.Can_fly())




