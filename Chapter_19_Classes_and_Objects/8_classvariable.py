#Create a class Dog with a class variable species = "Canis familiaris".
#Create multiple dog objects and show they share the class variable.
#Add a class variable count that tracks how many Dog objects were created.
#Use a @classmethod to display how many dogs exist.

class Dog:
    species = "Canis familiaris"
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total dogs created: {cls.count}")

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Bella")
Dog.display_count()  # Output: Total dogs created: 3
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(dog3.species)  # Output: Canis familiaris
