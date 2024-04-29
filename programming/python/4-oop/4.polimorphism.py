# Polimorphism
# Inheriting classes that implement the same method or property differently

class Animal:
    def __init__(self, type, breed):
        self.type = type
        self.breed = breed

    def speak(self):
        print('I\'m a animal!')

class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Dog', breed)

    def speak(self):
        print('Au, au, au!')

class Cat(Animal):
    def __init__(self, breed):
        super().__init__('Cat', breed)

    def speak(self):
        print('Miau, miau, miau!')

class Duck(Animal):
    def __init__(self, breed):
        super().__init__('Dock', breed)

    def speak(self):
        print('Quack, quack, quack!')

# instances
dog = Dog('Labrador')
cat = Cat('Persian')
duck = Duck('Mallard')
