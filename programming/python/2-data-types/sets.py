# sets
# unordered (don't have index), unchangeable, unique items

# syntax: set = {item1, item2, item3}
fruits = {"apple", "banana", "cherry", "apple"}
tropical = {"pineapple", "mango", "papaya"}
len(fruits)

# adding items (no duplicates) - O(1)
fruits.add("orange")
fruits.update(tropical) # add elements from an interable (str, arr, set)

# removing items - O(1)
fruits.remove("banana") # can raise an error
fruits.discard("banana") # not raise an error
fruits.pop() # remove a random element

# accessing items - O(1)
for fruit in fruits:
  print(fruit)

# check if an item exists - O(1)
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits set")

# operations
union_set = fruits.union(tropical)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = fruits.intersection(tropical)
print(intersection_set)  # Output: {3}

difference_set = fruits.difference(tropical)
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = fruits.symmetric_difference(tropical)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# comparison
fruits.issubset(tropical) # return true or false
tropical.issuperset(fruits) # return true or false
fruits.isdisjoint(tropical) # return true or false

# clear and delete a set
fruits.clear() # empty the set
del fruits # delete the set

# loops
for fruit in tropical:
  print(fruit)

# set comprehension
squared = {x**2 for x in range(10)}
print(squared)  # Output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# frozen set
# immutable version of a set
frozen = frozenset(["apple", "banana", "cherry"])
print(frozen)