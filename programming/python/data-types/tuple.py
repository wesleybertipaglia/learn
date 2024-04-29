# tuples
# ordered, unchangeable, allow duplicates

thistuple = ("apple", "banana", "cherry")
len(thistuple)

# accessing
thistuple[0] # first item
thistuple[-1] # last item
thistuple[2:5] # items from 2 to 4
thistuple[:4] # from start to 3
thistuple[1:] # from 1 to end

# adding items
repeated_tuple = thistuple * 3

# concatenating
thistuple += ("mango", "kiwi")

# unpacking items
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits # * returns the rest of the tuple

# for in
for x in fruits:
  print(x)

# range
for i in range(len(fruits)):
  print(fruits[i])

# while
while i < len(fruits):  
  print(fruits[i])  
  i = i + 1