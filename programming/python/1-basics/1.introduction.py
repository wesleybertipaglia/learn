# Basics of Python
import array

# variables and data types
x = 10 # Integers
y = 3.14 # Floats
major_age = True # Booleans
name = "Alice" # Strings
numbers = [1, 2, 3, 4, 5] # Lists
ages = array(18, 34, 25, 19) # Arrays
coordinates = (10, 20) # Tuples
person = {"name": "Bob", "age": 30} # Dictionaries
fruits = {"apple", "banana", "cherry"} # Sets

# comments

# input and output
username = input("Enter username:")
print("Hello, world!")

# function
def hello_world(): 
	print("Hello, World")
	
def hello_name(name): # parameters
	print("Hello, ", name)

hello_name("wesley") # calling a function

# lambda (one line function)
sum = lambda a,b: a + b
print(sum(1, 2)) # 3