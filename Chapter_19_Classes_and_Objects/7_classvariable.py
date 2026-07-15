#Create a class Employee with a class variable company_name.
#Add a @classmethod to change the company name for all employees.

class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        
employee1 = Employee("Alice")
employee2 = Employee("Bob")
print(employee1.company_name)  # Output: TechCorp
print(employee2.company_name)  # Output: TechCorp
Employee.change_company_name("Innovatech")
print(employee1.company_name)  # Output: Innovatech
print(employee2.company_name)  # Output: Innovatech


    