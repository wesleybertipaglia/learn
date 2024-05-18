# array: ordered, mutable, allow duplicates
# syntax: array(typecode, [elements])
# data types: only one type of data
# stored: in a memory block
# size: fixed

from array import array
x = array('i', [1, 2, 3, 4, 5])

# accessing
x[0] # accessing a value
x[1:3] # accessing a range of values
x[-1] # negative indexing
x[1] = 8 # changing a value

# adding items
x.append(6) # add an item
x.extend([7, 8, 9]) # add multiple items
x.insert(2, 10) # add an item at a specified position

# removing items
x.pop() # removes a specified item
x.remove(10) # removes the first occurrence of the specified value
del x[0] # removes the specified index
x.clear() # empties the array

# properties
x.typecode # data type
x.itemsize # size in bytes of each element
x.buffer_info() # memory address and size
x.count(2) # number of occurrences
x.index(3) # index of the first occurrence

# methods
len(x) # length
x.reverse() # reverse the array
x.tobytes() # convert to bytes
x.tolist() # convert to list
y = x.copy() # copy an array

# loops
for i in x:
  print(i)