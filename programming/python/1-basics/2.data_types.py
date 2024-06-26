# Data types

# strings
x = "Hello World"
x = 'Hello World' # same as above

# booleans
x = True
x = False

# numbers
x = 20 # int
x = 20.5 # float
x = 1j # complex

# array: ordered, mutable, allow duplicates
from array import array
x = array('i', [1, 2, 3, 4, 5])

# list: ordered, mutable, allow duplicates
x = ["apple", "banana", "cherry"]

# tuple: ordered, immutable, allow duplicates
x = ("apple", "banana", "cherry")

# dictionary: ordered, mutable, uunique keys
x = {"name" : "John", "age" : 36}

# set: unordered, mutable, unique values
x = {"apple", "banana", "cherry"}

# bytes
x = b"Hello" # bytes
x = bytearray(5) # bytearray

# special types
x = range(6) # range
x = frozenset({"apple", "banana", "cherry"}) # frozensetw
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

# setting a specific data type
x = str("Hello World")
x = int(20)

# getting the data type
x = 5
print(type(x)) # <class 'int'>

# casting
x = int(1) # 1
x = int(2.8) # 2
x = int("3") # 3
x = float(1) # 1.0
x = set(("apple", "banana", "cherry")) # {'apple', 'banana', 'cherry'}