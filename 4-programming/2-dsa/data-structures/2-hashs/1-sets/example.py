# Ordered: No
# Mutable: Yes
# Duplicates: No
# Indexing: No (but can check membership)
# Different Data Types: Yes (but elements must be hashable)

# Create a hash set
my_set = set()

# Add elements to the set
my_set.add(1)
my_set.add('hello')
my_set.add(3.14)
my_set.add(True)
my_set.add(1)  # Duplicates are ignored

# Print the set
print(my_set)  # Output: {1, 3.14, 'hello'}

# Check membership
print(3.14 in my_set)  # Output: True

# Remove an element
my_set.remove('hello')
print(my_set)  # Output: {1, 3.14}

# Iterate over the set
for element in my_set:
    print(element)  # Output: 1 3.14

# Get the size of the set
print(len(my_set))  # Output: 2

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
