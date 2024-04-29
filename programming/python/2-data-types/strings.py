# strings

hello = "Hello" # same as 'hello'

multiline = """Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua."""

# length
len(multiline)

# format
age = 36  
txt = f"My name is John, and I am {age}"

# case
hello.upper()
hello.lower()
hello.capitalize()
hello.casefold()

# white spaces
hello.center(4)
" Hello, World! ".strip() # remove whitespaces

hello.replace("H", "J") # replace
hello.split(",") # split
"-".join(hello) # join

# concatenation
a = "Hello"  
b = "World"  
c = a + b
c = a + " " + b

# checking
txt = "The best things in life are free!"  
print("free" in txt) # true
print("expensive" not in txt) # true
print(txt.startswith("The")) # true
print(txt.endswith("The")) # false

# index
print(hello[1]) # accessing an index
print(hello[2:5]) # slicing [start, end - 1]
print(hello[2:]) # 2 pos to end
print(hello[:5]) # start to 4 pos
print(hello[-1]) # last pos
print(hello[-2]) # seccond last pos
hello.find("world") # return the first index
hello.index("world") # return the first index
hello.count("o") # return the num of "o" in the string

# for in
for x in "banana":
    print(x)

# escape
quotes = "\""
single_quotes = "\'"
backslash = "\\"
new_line = "\n"
carriage_return = "\r"
tab = "\t"
backspace = "\b"
form_feed = "\f"
octal_value = "\ooo"
hex_value = "\xhh"
