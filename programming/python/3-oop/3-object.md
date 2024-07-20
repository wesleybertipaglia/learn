# Objects

In Python, an object is an instance of a class. Objects can hold both data (attributes) and functions (methods) that operate on the data.

## Creating Objects

Objects are created by calling a class as if it were a function.

### Example:
```python
class MyClass:
    def __init__(self, value):
        self.value = value

my_obj = MyClass(10)
print(my_obj.value) # Output: 10
```

## Atributes

Attributes are variables defined within a class. They hold data for the object.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)

my_dog.name # accessing attribute
my_dog.age = 4 # modifying attribute
```

## Methods

Methods are functions defined within a class. They are used to define the behavior of an object.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self): # method
        print(f"{self.name} is barking.")

my_dog = Dog("Buddy", 3)

my_dog.bark() # calling method
```
