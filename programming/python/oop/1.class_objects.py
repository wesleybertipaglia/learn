# Class and objects
# Class: A blueprint for creating objects
# Objects: an instance from a class

# special methods
# __init__: initialize the class
# __del__: run after destruction
# __str__: describe the class in a print statement


class  Person:
    def __init__(self, name, age, contry):
        self.name = name
        self.age = age
        self.contry = contry

    def say_hello(self):
        print(f'Hello, {self.name}!')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

    def __del__(self):
        print('Destructuring class')

wesley = Person('Wesley', 25, 'Brazil')