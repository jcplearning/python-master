#Create a class Employee with a protected attribute _salary.
#Add a method to increase salary by a percentage.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected attribute

    def increase_salary(self, percentage):
        self._salary += self._salary * (percentage / 100)
        print(f"{self.name}'s new salary: {self._salary}")
        
employee = Employee("Alice", 50000)
employee.increase_salary(10)  # Output: Alice's new salary: 55000.0

