lst = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, lst)) 
print(evens)

strings = ["hello", "world", "python", "lambda"]
long_strings = list(filter(lambda s: len(s) > 5, strings))
print(long_strings)

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90}
]

high_scorers = list(filter(lambda student: student["score"] > 80, students))
print(high_scorers)

students_age = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 21}
]

adults = list(zip(students_age, map(lambda student: 'Major' if student["age"] >= 21 else 'Minor', students_age)))
print(adults)

#Given a list of (name, age), group them into "minor" and "adult" using filter() + lambda.

people = [("Alice", 20), ("Bob", 22), ("Charlie", 19), ("David", 21)]
adults = list(filter(lambda person: person[1] >= 21, people))
minors = list(filter(lambda person: person[1] < 21, people))
print("Adults:", adults)
print("Minors:", minors)

#Given a list of dictionaries representing students, return the top 3 students by score
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eve", "score": 88}
]

top_students = sorted(students, key=lambda student: student["score"], reverse=True)[:3]
print(top_students)

# Given ["apple", "banana", "cherry", "avocado", "blueberry"], group by the first letter using a dict comprehension + lambda key.

fruits = ["apple", "banana", "cherry", "avocado", "blueberry"]
grouped_fruits = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in grouped_fruits:
        grouped_fruits[first_letter] = []
    grouped_fruits[first_letter].append(fruit)
print(grouped_fruits)
