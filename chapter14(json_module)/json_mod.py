# JSON (JavaScript Object Notation) is a lightweight data format used for data exchange between servers and applications. It is widely used in APIs, web applications, and configurations.


import json
# Converting Python Objects to JSON (Serialization)

data = {"name": "Alice", 
        "age": 25, 
        "city": "New York"}
 
json_string = json.dumps(data)   #dump means dump this as a string
print(json_string) 
print(type(json_string))

# Converting JSON to Python Objects (Deserialization)

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

python_obj = json.loads(json_data)
print(python_obj)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(python_obj))  # <class 'dict'>


# json.dump() – Write JSON data to a file
with open("data.json", "w") as file:
    json.dump(data, file)
    file.close()


# You can format JSON for better readability using indentation.
formatted_json = json.dumps(data, indent=4)
print(formatted_json)

# json.load() – Read JSON data from a file
with open("data.json", "r") as file:
    python_data = json.load(file)
print(python_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}