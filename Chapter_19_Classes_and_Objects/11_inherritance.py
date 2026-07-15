#Create a class Vehicle with attributes brand and speed.
#Create subclasses Car and Bike.
#Add a method in Vehicle called move().
#Override move() in subclasses with more specific behavior.
#Use super() in subclass constructors.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"The {self.brand} is moving at {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def move(self):
        print(f"The car {self.brand} is driving at {self.speed} km/h with {self.num_doors} doors.") 

class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def move(self):
        print(f"The {self.bike_type} bike {self.brand} is cycling at {self.speed} km/h.")

car = Car("Toyota", 120, 4)
bike = Bike("Trek", 30, "mountain")
car.move()  # Output: The car Toyota is driving at 120 km/h with 4 doors.
bike.move()  # Output: The mountain bike Trek is cycling at 30 km/h.
