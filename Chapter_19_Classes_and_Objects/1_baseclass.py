#Create a class Person with attributes name and age.
#Create two Person objects and print their attributes.
#Add a method introduce() that prints: "Hi, my name is Alice and I am 25 years old."

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
        
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25
print(person2.name)  # Output: Bob
print(person2.age)   # Output: 30
person1.introduce()  # Output: Hi, my name is Alice and I am 25 years old.
person2.introduce()  # Output: Hi, my name is Bob and I am
