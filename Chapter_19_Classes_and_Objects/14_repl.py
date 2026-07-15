#Add __repr__ to Person for debugging.
import unittest

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
person1 = Person("Alice", 25)
print(repr(person1))  # Output: Person(name='Alice', age=25)

