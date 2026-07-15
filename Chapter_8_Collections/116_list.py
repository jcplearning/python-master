# list examples 

mylist = [10,20,25,34,56,78,45,90,100]
print(mylist)

print(f'The slice is {mylist[2:5]}')

print(f'The count of elements in this list is {len(mylist)}')

print(f'The sum of elements in this list is {sum(mylist)}')

mylist.append(120)
mylist.insert(7,40)
mylist[2:5] = [30,34,56]
print(mylist)

mylist.remove(40)
print(mylist)

mynewlist = mylist.copy()
print(mynewlist)

mynewlist1 = [10.0, 20.1,30.4, 40.5]

mylist.extend(mynewlist1)
print(mylist)

print(sorted(mylist))


