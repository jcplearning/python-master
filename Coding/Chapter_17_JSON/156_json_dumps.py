import json

# JSON.DUMPS converts a python object into a JSON string. It takes a python object as an argument and returns a JSON string.

mydict = {"name": 'Alice', "age": 30}
# If the value has singl e quotes, it will be converted to double quotes in the JSON string.
json_string = json.dumps(mydict)
print(json_string)


mydict = {"name": 'Alice', "age": None}
# If the value is None, it will be converted to null in the JSON string.
json_string = json.dumps(mydict)
print(json_string)


mydict = {"name": 'Alice', "age": 30, "is_student": False}
# If the value is False, it will be converted to false in the JSON string.
json_string = json.dumps(mydict)
print(json_string)

mydict = {"name": 'Alice', "age": 30, "is_student": True}
# If the value is True, it will be converted to true in the JSON string.
json_string = json.dumps(mydict)
print(json_string)



