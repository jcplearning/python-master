import csv

mylist = [ "100, 'John Smith', 35",
           "101, 'Jason Dawson', 33",
            "102, 'Will Benjamin', 32"]

csvdata = csv.DictReader(mylist,fieldnames=["ID","Name","Age"],delimiter=',')

for data in csvdata:
    print(data["ID"], data["Name"],data["Age"])