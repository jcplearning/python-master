import json

with open('wiki.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data)) 
    print(data["address"]["city"])
    print(data["first_name"])
    print(data["children"])

