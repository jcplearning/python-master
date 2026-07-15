#Create a class Student with attributes name and grades (a list).
#Add a method average_grade() that returns the average.

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

student = Student("John", [85, 90, 78])
print("Average grade:", student.average_grade())  # Output: Average grade: 84.33333333333333

