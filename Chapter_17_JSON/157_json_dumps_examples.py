import json

lst = [1, 2, 3, "four", True, None, {"name": "Alice", "age": 30}, (10, 20)]
print(type(json.dumps(lst)))
print(json.dumps(lst,indent=2)) 

