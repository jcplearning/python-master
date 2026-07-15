# dict example
import operator

mydict = {"name": "Alice", "age": 30, "city": "New York"}

print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict["name"])
print(mydict.get("age"))

for dict_key, dict_value in mydict.items():
    print(f'Key: {dict_key}, Value: {dict_value}')

# sort dict by keys 
listkey = ["d", "b", "c", "a"]
mydict = dict.fromkeys(listkey,100)
print(mydict)


mydict = {"d": 100, "b": 105, "c": 101, "a": 102}

sorted_dict = dict(sorted(mydict.items(), key=lambda item: item[1]))
print(sorted_dict)

# sort dict without using lambda function 
sorted_dict2 = dict(sorted(mydict.items(), key=operator.itemgetter(1)))
print(sorted_dict2)

reverse_sorted_dict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
print(reverse_sorted_dict)




