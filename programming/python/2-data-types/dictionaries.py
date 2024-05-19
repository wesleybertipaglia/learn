# Dictionaries are used to store data values in key:value pairs.
# is the same as an HashMap or a HashTable
# is ordered, changeable, unique keys

# syntax: dictionary = {key: value}
car = {
    "brand": "ford",
    "model": "mustang",
    "color": "red",
    "year": 1964
}

# accessing - O(1)
car["model"] # accessing a value
car.get("model") # accessing a value
car.keys() # list of keys
car.values() # list of values
car.items() # list of items

# Searching - O(n)
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")

# adding items - O(1)
car["color"] = "black"

# changing items - O(1)
car.update({"year": 2020})

# removing items - O(1)
car.pop("model") # removes a specified item
car.popitem() # removes the last item
car.clear() # empities the dictionary

# copy a dictionary
another_car = car.copy()

# loops
for key, value in car.items(): # or car
  print(key, value)

for key in car.keys():
  print(key)

for value in car.values():
  print(value)

# nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}