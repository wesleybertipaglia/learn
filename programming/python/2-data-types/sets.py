# sets
# unordered, unchangeable, unique items, don't have index

fruits = {"apple", "banana", "cherry", "apple"}
tropical = {"pineapple", "mango", "papaya"}
len(fruits)

# for in
for x in fruits:  
    print(x)

# adding items
fruits.add("orange")
fruits.update(tropical) # add elements from an interable (str, arr, set)

# removing items
fruits.remove("banana") # can raise an error
fruits.discard("banana") # not raise an error
fruits.pop() # remove a random element

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