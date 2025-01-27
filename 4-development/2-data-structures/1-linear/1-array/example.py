# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes
# Different Data Types: No (all elements must be of the same type)

import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements by index
print(arr[0])  # Output: 1

# Modify an element
arr[1] = 10
print(arr)  # Output: array('i', [1, 10, 3, 4, 5])

# Add elements
arr.append(6)
print(arr)  # Output: array('i', [1, 10, 3, 4, 5, 6])

# Remove elements
arr.remove(10)
print(arr)  # Output: array('i', [1, 3, 4, 5, 6])

# Iterate over the array
for element in arr:
    print(element)  # Output: 1 3 4 5 6
