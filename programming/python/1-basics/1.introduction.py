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

# arithmetic operators
sum = 1 + 2
sub = 5 - 3
mul = 8 * 5
div = 10 / 2
flo = 11 // 2 # absolute division (discard the decimal part) = 5
mod = 33 % 2 # module (remainder of the division) = 1
exp = 2 ** 3 # exponentiation = 8

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

# for loop (in)
fruits = ['apple', 'banana', 'kwi', 'coconut']

for fruit in fruits:
    if fruit == "banana":
        break # break the entry loop
    if fruit == "coconut":
        continue # skip the current interation
    print(fruit)

# for loop (in range)
for x in range(10):
    print(x)

# try, except, finally
try:
    if x < 0:
        raise Exception("Sorry, no numbers bellow zero.")
    print(x)
except:
    print("Something went wrong.")

finally:
    print('The \'try except\' is finished.')