import math

# Base class
class Shape:
    def area(self):
        """Method to calculate area. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")
