class Mammal:
    def walk(self):
        print("walk")
        
class Dog(Mammal):
    pass # pass this line so that we don't have an empty class


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()