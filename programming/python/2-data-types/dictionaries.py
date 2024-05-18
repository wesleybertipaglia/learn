# Dictionaries are used to store data values in key:value pairs.
# is the same as an HashMap or a HashTable
# is ordered, changeable, unique keys

car = {
    "brand": "ford",
    "model": "mustang",
    "color": "red",
    "year": 1964
}

# accessing
car["model"] # accessing a value
car.get("model") # accessing a value
car.keys() # list of keys
car.values() # list of values
car.items() # list of items

# changing and adding items
car["color"] = "black"
car.update({"year": 2020})

# removing items
car.pop("model") # removes a specified item
car.popitem() # removes the last item
car.clear() # empities the dictionary

# copy a dictionary
another_car = car.copy()

# loops
for key in car: # same as car.keys
  print(key)

for value in car.values():  
  print(value)