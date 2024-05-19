import json

obj = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

json_obj = '{ "name":"John", "age":30, "city":"New York"}'

# Encode a Python object into a JSON formatted string with specified separators and no indentation
json.dumps(obj, indent=None, separators=(',', ':'), sort_keys=False)

# Encode a Python object into a JSON formatted string, pretty-printed with indentation
json.dumps(obj, indent=4)

# Decode a JSON formatted string into a Python object
json.loads(json_obj)

# Write a Python object to a JSON formatted file with specified separators and no indentation
with open('file.json', 'w') as file:
    json.dump(obj, file, indent=None, separators=(',', ':'), sort_keys=False)

# Write a Python object to a JSON formatted file, pretty-printed with indentation
with open('file.json', 'w') as file:
    json.dump(obj, file, indent=4)

# Read a Python object from a JSON formatted file
with open('file.json', 'r') as file:
    json.load(file)
