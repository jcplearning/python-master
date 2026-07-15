import json

json_string ='{"name": "Bob", "age": 25}'
# JSON.LOADS converts a JSON string into a python object. It takes a JSON string as an argument and returns a python object.
python_obj = json.loads(json_string)
print(python_obj)

json_string ='{"name": "Bob", "age": 25, "is_student": false, "hobbies": ["reading", "gaming"], "phone": null}' 
python_obj = json.loads(json_string)
print(python_obj)



