# Print messages
print('Hello World!')
print('Python\n makes programming fun!')

print('Plain English', end=" ")
print('Easy to follow', end=" ")
print('Fully illustrated', end=" ")

print('\n')
print('Monther\'s recipe')

# concatenate messages
print('Hello','World',sep='*')
print('Hello' + ' ' + 'World')

ID = 'J100'
Name = 'John Smith'
Age = 35
Salary = 60000.00

# converted the numeric to string using str function
print('Using Conversion for numbers -> The data row is ' + ID + ' Name is ' + Name + ' Age is ' + str(Age) + ' Salary is ' + str(Salary))

# Lets try with the old style
print('In Old Style 1 -> The data row is {0} Name is {1} Age is {2} Salary is {3:.4f}'.format(ID,Name,Age,Salary))
print('In Old Style 2 -> The data row is {id} Name is {name} Age is {age} Salary is {salary:.2f}'.format(id=ID,name=Name,age=Age,salary=Salary))

# lets try with the new style
print(f'In New Style -> The data row is {ID} Name is {Name} Age is {Age} Salary is {Salary:.2f}')

