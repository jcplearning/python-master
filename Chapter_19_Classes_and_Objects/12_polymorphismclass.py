#Create classes Circle and Square, each with a method area().
#Write a function that accepts any object with an area() method and prints the area.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_area(shape):
    print(f"The area is: {shape.area()}")

circle = Circle(5)
square = Square(4)

print_area(circle)  # Output: The area is: 78.53981633974483
print_area(square)  # Output: The area is: 16
