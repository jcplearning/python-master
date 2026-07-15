import json
from textwrap import indent
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'hobbies': ['reading', 'gaming'],
    'phone': None
}
# JSON.DUMP writes a python object into a JSON file. It takes a python object and a file object as arguments and writes the JSON string into the file.
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

lst = [1, 2, 3, "four", True, None, {"name": "Alice", "age": 30}, (10, 20)]
with open('list.json', 'w') as f:
    json.dump(lst, f, indent=2)



students = [
    {"name": "Alice", "age": 30, "grade": "A"},
    {"name": "Bob", "age": 25, "grade": "B"},
    {"name": "Charlie", "age": 35, "grade": "C"}
]

with open('students.json','w') as f:
    json.dump(students,f,indent=2,sort_keys=True,ensure_ascii=False)
    
    