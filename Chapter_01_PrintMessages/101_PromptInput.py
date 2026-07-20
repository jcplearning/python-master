# Prompting input from the console


while True:
    name = input('Enter the name of the person:')
    if name == '':
        print('Name cannot be blank')
        continue
    else:
        break

while True:
    age = input('Enter the age of the person:')
    if age == '':
        print('Name cannot be blank')
        continue
    elif int(age) <= 0 or int(age) > 100:
        print('invalid age')
        continue
    else:
        break
print(f'Welcome {name}')


