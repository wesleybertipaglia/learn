# Basics of Python

# variables and data types
x = 10 # Integers
y = 3.14 # Floats
name = "Alice" # Strings
numbers = [1, 2, 3, 4, 5] # Lists
coordinates = (10, 20) # Tuples
person = {"name": "Bob", "age": 30} # Dictionaries
my_set = {"apple", "banana", "cherry"} # Sets
my_bool = True

# comment 

# output
print("Hello, world!")

# input 
username = input("Enter username:")

# function
def hello_world(): 
	print("Hello, World")
	
def hello_name(name): # parameters
	print("Hello, ", name)
	
sum = lambda a,b: a + b # lambda (one line function)

hello_name("wesley") # calling a function

# operators
sum = 1 + 2
sub = 5 - 3
mul = 8 * 5
div = 10 / 2
flo = 11 // 2
mod = 33 % 2
exp = 2 ** 3

# conditionals
value = 20

if value < 10:
    print("the value is less to 10")
elif value == 10:
    print("the value is equal to 10")
else:
    print("the value is bigger tha 10")

# while loop
i = 0

while i < 10:
    if i == 5:
        break # stop the loop
    if i == 2:
        i += 1
        continue # stop the current iteration
    print(i)
    i += 1

# for in
fruits = ['apple', 'banana', 'kwi', 'coconut']

for fruit in fruits:
    print(fruit)

# for in range
for x in range(10):
    print(x)

# try except finally
try:
    if x < 0:
        raise Exception("Sorry, no numbers bellow zero.")
    print(x)
except:
    print("Something went wrong.")

finally:
    print('The \'try except\' is finished.')