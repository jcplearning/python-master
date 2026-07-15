#Add __str__ to Person for readable printing.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

person1 = Person("Alice", 25)
print(person1)  # Output: Person(name='Alice', age=25)

