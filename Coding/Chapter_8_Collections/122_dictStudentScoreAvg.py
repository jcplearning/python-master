# average of staudent scores 

students_scores = {
    "Alice": [85, 90, 78],
    "Bob": [72, 88, 91],
    "Charlie": [95, 100, 92]
}

students_avg_scores = {} 

for student, scores in students_scores.items():
    avg_score = sum(scores) / len(scores)
    students_avg_scores[student] = avg_score 

for student, avg_score in students_avg_scores.items():
    print(f"{student}: {avg_score:.2f}")
    