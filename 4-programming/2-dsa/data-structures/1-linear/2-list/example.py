# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes
# Different Data Types: Yes

# Create a list with mixed data types
my_list = [1, 'hello', 3.14, True]

# Access elements by index
print(my_list[0])  # Output: 1

# Modify an element
my_list[1] = 'world'
print(my_list)  # Output: [1, 'world', 3.14, True]

# Add elements
my_list.append(42)
print(my_list)  # Output: [1, 'world', 3.14, True, 42]

# Remove elements
my_list.remove(3.14)
print(my_list)  # Output: [1, 'world', True, 42]

# Iterate over the list
for element in my_list:
    print(element)  # Output: 1 world True 42
