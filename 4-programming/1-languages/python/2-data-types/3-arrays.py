# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes
# Different Data Types: No

import array as arr

# creating
numbers = arr.array('i', [1, 2, 3, 4, 5]) # 'i' stands for integer

# properties
length = len(numbers) # 5

# access
first_number = numbers[0] # 1
last_number = numbers[-1] # 5

# modifying elements
numbers[0] = 0
numbers[-1] = 6

# adding elements
numbers.append(6)
numbers.extend([7, 8, 9])

# removing elements
numbers.remove(5) # removes first occurrence of 5
numbers.pop() # removes last element
numbers.pop(1) # removes element at index 1
del numbers[2] # removes element at index 2
numbers.clear() # removes all elements

# slicing
numbers[1:3] # from 1 to 3
numbers[:3] # from start to 3
numbers[3:] # from 4 to end
numbers[:] # all elements
numbers[::2] # every 2nd element
numbers[::-1] # reverse list

# copying
numbers_copy = numbers[:]
numbers_copy = arr.array(numbers.typecode, numbers)

# sorting
numbers = arr.array('i', [3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted_numbers = arr.array(numbers.typecode, sorted(numbers))
print(sorted_numbers)  # array('i', [1, 1, 2, 3, 4, 5, 5, 6, 9])

chars = ['d', 'a', 'c', 'b', 'e']
chars.sort()

# searching
index_of_5 = numbers.index(5)  # 4

# checking
is_in_array = 5 in numbers  # True
is_not_in_array = 10 not in numbers  # True

# reversing
numbers.reverse()
print(numbers)  # array('i', [5, 6, 2, 9, 5, 1, 4, 1, 3])

# iterating
for number in numbers:
    print(number)

# nested lists
nested_numbers = arr.array('i', [arr.array('i', [1, 2, 3]), arr.array('i', [4, 5, 6])])

# note: the array module doesn't support nested arrays directly, so nested_numbers would be a regular list of arrays
nested_numbers = [arr.array('i', [1, 2, 3]), arr.array('i', [4, 5, 6])]
for sub_array in nested_numbers:
    for number in sub_array:
        print(number)
