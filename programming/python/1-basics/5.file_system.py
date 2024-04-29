# modes: (r) read, (a) append, (w) write, (x) create
# types: (t) text, (b) binary
# methods: open(), remove(), rmdir()

import os

current_dir = "cs/programming-laguages/python/basics" # os.getcwd()
folder_dir = current_dir + '/test/'

# creating
os.mkdir(folder_dir) # create a dir
f = open(folder_dir + 'test.txt', "x") # create a text file
f = open(folder_dir + 'test.bin', "x") # create a binary file
os.path.exists("demofile.txt") # check if it exists

# reading
with open(folder_dir + 'test.txt', 'r') as f: # text
    content = f.read()
    print(content)

with open(folder_dir + 'test.bin', 'rb') as f: # binary
    data = f.read()

# writing
with open(folder_dir + 'test.txt', 'w') as f: # text
    f.write('Hello, world!\n')

with open(folder_dir + 'test.bin', 'wb') as f: # binary
    f.write(b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21')

# appending
with open(folder_dir + 'test.txt', 'a') as f:
    f.write('Appending to the file.\n')

# deleting
os.remove(folder_dir + 'test.txt') # text
os.remove(folder_dir + 'test.bin') # binary
os.rmdir(folder_dir) # delete a dir