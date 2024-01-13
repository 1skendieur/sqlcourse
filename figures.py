import math 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

    def calc_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return "Rectangle"


class Square:
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side

    def calc_perimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return "Square"
    
    


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        import math
        return math.pi * (self.radius ** 2)

    def calc_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return "Circle"
