# tuples examples
mytuple = ( 10,20,25,34,56,78,45,90,100)
print(mytuple)

print(f'The count of elements in this tuple is {len(mytuple)}') 

print(f'The sum of elements in this tuple is {sum(mytuple)}') 

print(f'The sum of elements in this tuple is {max(mytuple)}') 

print(f'The sum of elements in this tuple is {min(mytuple)}') 

print(f'The sum of elements in this tuple is {mytuple.count(25)}') 

print(f'The count of elements in this tuple that are 25 is {mytuple.index(25)}')

index = 0
while index < len(mytuple):
    print(mytuple[index])
    index += 1
    
