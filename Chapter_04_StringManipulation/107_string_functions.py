# Section 1
# Case convertion

message = 'Hello World!'
print(f'The original message is {message}')

print(f'The upper case message is {message.upper()}')
print(f'The lower case message is {message.lower()}')
print(f'The title message is {message.title()}')
print(f'The capitalize message is {message.capitalize()}')
print(f'The casefold message is {message.casefold()}')

# Section 2
# slicing using position
name = 'Top Gun Maverick'
print(f'The original message is {name}')
print(f'The first 3 character is {name[:3]}')
print(f'The first 7 character is {name[0:7]}')
print(f'The last 4 character is {name[-4:]}')

# Section 3
# searching
name = 'Anaconda'
print(f'The letter n present in the position {name.find('n')}')
print(f'The letter k present in the position {name.find('k')}')

print(f'The letter n present in the position {name.index('o')}')
#print(f'The letter k present in the position {name.index('k')}') # this will error out

print(f'The count of letter o present for  {name.count('o')}')

print(f'The count of letter o present for  {name.count('o')}')
print(f'The count of letter o present for  {name.count('o')}')
print(f'the word conda is in {'conda' in name}')

print(f'the word Ana starts with {name.startswith('An')}')
print(f'the word da starts with {name.endswith('da')}')


# Section 4
# modifying
store = 'Shoprite '
print(f'stripped string is {store.strip()}')
print(f'replaced string is {store.replace('rite','bite')}')

# Section 5
# spliting & joining
mystring = 'Everybody loves Raymond'
print('splitted strings are {}'.format(mystring.split()))

mystring = 'How,i,met,your,mother'
print('splitted strings are {}'.format(mystring.split(',')))

mystring = 'Seinfeld\nEverybody loves Raymond\nBigbang Theory\n'
print('splitted strings are {}'.format(mystring.splitlines()))

series1 ='Seinfeld'
series2 ='King of Queens'
print('combined strings are {}'.format(','.join(series1)))






















