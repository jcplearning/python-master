# Comprehensions exercise ( list of squares)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# like map lambda 
squares = [ num * num  for num in numbers]
print(f'The squares of the number is {squares}')

# like filter lambda 
evens = [ num for num in numbers if num % 2 == 0 ]
print(f'The even numbers in the list are {evens}')

words = ['hello', 'world', 'python', 'comprehension', 'exercise']
# like filter lambda 
bigwords = [ word for word in words if len(word) > 5 ]
print(f'The words with more than 5 characters are {bigwords}')

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

dict1 = dict(zip(keys, values)) 
print(f'The dictionary created from the keys and values is {dict1}')

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 95)]

students_dict = {student for student in students if student[1] >= 80}
print(f'The students with scores greater than or equal to 80 are {students_dict}')

students_dict = {student: 'Pass' if mark >= 80 else 'Fail' for student, mark in students}
print(f'The students with scores greater than or equal to 80 are {students_dict}')

