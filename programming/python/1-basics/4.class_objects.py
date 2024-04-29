# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello, my name is ", self.name)

# inheritance
class Student:
    def __init__(self, name, age, course, university):
        super().__init__(name, age)
        self.course = course
        self.university = university

# polymorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:  
    def __init__(self, brand, model):  
        self.brand = brand  
        self.model = model  

    def move(self):
        print("Sail!")
	  
  
class Plane:  
    def __init__(self, brand, model):  
        self.brand = brand  
        self.model = model

    def move(self):
        print("Fly!")

# objects
p1 = Person("John", 36)  
p1.hello()
p1.age = 20 # modify props
del p1.age # delete props
del p1 # delete object

