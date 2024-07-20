# Classes

A class in Python is a blueprint for creating objects. Classes encapsulate data for the object and methods to manipulate that data.

## Components of a Class

1. Class Definition

A class is defined using the `class` keyword followed by the class name and a colon.

### Example:
```python
class Dog:
    pass
```

2. Constructor Method

The `__init__` method is a special method that initializes an object. It is called when an object is created.

### Example:
```python
class Dog:
    def __init__(self):
        pass
```

3. Properties (or attributes)

Properties are variables defined within a class. They hold data for the object.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

4. Methods

Methods are functions defined within a class. They are used to define the behavior of an object.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self): # method
        print(f"{self.name} is barking.")
```
