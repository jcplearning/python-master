# sort the list basic

lst = [5, 2, 9, 1, 5, 6]
sorted_lst = sorted(lst)
print(sorted_lst)

print('\n\n')
students_scores_multipleSubjects_tuple = [
    ("Alice", {'scores': [85,90, 88]}),
    ("Bob", {'scores': [78, 82, 80]}),
    ("Charlie", {'scores': [92, 88, 84]})
]

sorted_students_tuple = sorted(students_scores_multipleSubjects_tuple, key=lambda student: sum(student[1]['scores']), reverse=True)
print(sorted_students_tuple)


students_scores_multipleSubjects = [
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "Literature": 88}},
    {"name": "Bob", "scores": {"Math": 78, "Science": 82, "Literature": 80}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 88, "Literature": 84}}
]

print('\n\n')
# Sort the students based on total score across all subjects in reverse order (highest total score first) using sorted() + lambda. 
students_new = []

for student in students_scores_multipleSubjects:
    student["total_score"] = sum(student["scores"].values())    
    students_new.append(student)
sorted_students = sorted(students_new, key=lambda student: student["total_score"], reverse=True)
print(sorted_students)


