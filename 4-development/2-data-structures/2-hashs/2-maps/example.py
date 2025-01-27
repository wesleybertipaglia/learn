# Ordered: Yes (since Python 3.7, insertion order is preserved)
# Mutable: Yes
# Duplicates: No (keys must be unique)
# Indexing: Yes (by keys)
# Different Data Types: Yes (both keys and values can be different types, but keys must be hashable)

# Create a hash map (dictionary)
my_dict = {}

# Add key-value pairs
my_dict['name'] = 'Alice'
my_dict['age'] = 25
my_dict['height'] = 5.7
my_dict[1] = 'one'

# Access values by key
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 25

# Modify a value
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'height': 5.7, 1: 'one'}

# Remove a key-value pair
del my_dict['height']
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 1: 'one'}

# Check for the presence of a key
print('name' in my_dict)  # Output: True
print('height' in my_dict)  # Output: False

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f'{key}: {value}')
    # Output:
    # name: Alice
    # age: 26
    # 1: one

# Get the size of the dictionary
print(len(my_dict))  # Output: 3

# Create a dictionary with initial values
person = {'name': 'Bob', 'age': 30, 'job': 'Developer'}

# Get all keys
print(person.keys())  # Output: dict_keys(['name', 'age', 'job'])

# Get all values
print(person.values())  # Output: dict_values(['Bob', 30, 'Developer'])

# Get all key-value pairs
print(person.items())  # Output: dict_items([('name', 'Bob'), ('age', 30), ('job', 'Developer')])

# Get a value with a default if the key doesn't exist
print(person.get('salary', 'Not specified'))  # Output: Not specified

# Update the dictionary with another dictionary
person.update({'age': 31, 'city': 'New York'})
print(person)  # Output: {'name': 'Bob', 'age': 31, 'job': 'Developer', 'city': 'New York'}
