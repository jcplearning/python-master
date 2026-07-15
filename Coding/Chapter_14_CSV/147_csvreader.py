import csv
mylist = ['Cereal','Pretzels','PopTarts','Oatmeal'] 

parties = csv.reader(mylist,delimiter=',')

for party in parties:
    print(party)
    