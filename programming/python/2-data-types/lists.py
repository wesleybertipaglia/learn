# lists
# ordered, mutable, allow duplicates
# data types: different types of data
# stored: in a memory block
# size: dynamic

# syntax: list = [elements]
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

# accessing items - O(1)
fruits[0] # first element
fruits[-1] # last element
fruits[-2] # second last element
fruits[2:] # from the position 2 to the end
fruits[:1] # from the beginning to the position 1
fruits[2:4] # from the position 2 to the position 4

# searching - O(n)
fruits.index("banana") # search for a value
fruits.count("banana") # count the number of occurrences

# adding items - O(n)
fruits.insert(2, "watermelon") # insert in determined index
fruits.append("orange") # append to the end
fruits.extend(tropical) # append a list to another

# removing items - O(n)
fruits.remove("kiwi")
fruits.pop() # remove the last item
fruits.pop(1) # remove item from a specified index
del fruits[0] # remove item from a specified index

# reordering
fruits.sort() # sort alphanumerically
fruits.sort(reverse = True) # sort descending
fruits.reverse() # reverse

# change items
fruits[1] = "blackcurrant"
fruits[1:3] = ["blackcurrant", "watermelon"]

# join
fruits = fruits + tropical

# coping
mylist = fruits.copy()

# for in
for x in fruits:  
  print(x)

# for in range
for i in range(len(fruits)):  
  print(fruits[i])

# while
i = 0  
while i < len(fruits):  
  print(fruits[i])  
  i = i + 1

# clear and delete a list
fruits.clear() # empities the entry list
del fruits # delete the entry list