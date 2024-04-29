# Class Methods
# variables and methods: belonging to the class itself

class Car:    
    wheels = 4 # class variable
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def change_number_of_wheels(cls, new_wheels): # class method
        cls.wheels = new_wheels

# instances
my_car = Car("Toyota", "Camry", 2022)
my_car.wheels # class variable
Car.change_number_of_wheels(6) # calling class method
