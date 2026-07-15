#============================
# sum of arbitrary arguments (tuples)
#============================

def sum_of_tuples(*args): 
    return sum(args)

# calling the function
tup1 = ( 100.45, 200.30, 150.25 )

print(f'The sum of the tuple is {sum_of_tuples(*tup1)}')

#============================
# sum of arbitrary arguments (lists)
#============================
def sum_of_lists(*args): 
    return sum(args)

list1 = [ 100.45, 200.30, 150.25 ]

print(f'The sum of the list is {sum_of_lists(*list1)}')

#============================
# sum of arbitrary arguments (sets)
#============================
def sum_of_sets(*args): 
    return sum(args)

# calling the function
set1 = { 100.45, 200.30, 150.25 }

print(f'The sum of the set is {sum_of_sets(*set1)}')

#============================
# sum of arbitrary arguments (dictionaries)
#============================

def sum_of_dicts(**args):
    return sum(args.values())

shares = {'oracle': 100.45, 'microsoft': 200.30, 'apple': 150.25 , 'google': 250.50 , 'amazon': 300.75 , 'facebook': 180.20 }

print(f'The sum of the dictionary values is {sum_of_dicts(**shares)}')
