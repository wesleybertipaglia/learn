# lists
# ordered, changeable, allow duplicates

fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

# accessing items
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
fruits[0] # first element
fruits[-1] # last element
fruits[-2] # second last element
fruits[2:] # ["cherry", "orange", "kiwi", "melon"]
fruits[:1] # ["apple"]
fruits[2:4] # ["cherry", "orange"]

# reordering
fruits.sort() # sort alphanumerically
fruits.sort(reverse = True) # sort descending
fruits.reverse() # reverse

# change items
fruits[1] = "blackcurrant"
fruits[1:3] = ["blackcurrant", "watermelon"]

# adding items
fruits.insert(2, "watermelon") # insert in determined index
fruits.append("orange") # append to the end
fruits.extend(tropical) # append a list to another

# removing items
fruits.remove("kiwi")
fruits.pop() # remove the last item
fruits.pop(1) # remove item from a specified index
del fruits[0] # remove item from a specified index

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