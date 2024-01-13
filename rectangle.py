class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @classmethod
    def get_info(cls):
        return "This class calculates perimeter and area of the rectangles"

    def __str__(self):
        return f"Rectangle with width {self._width} cm and height {self._height} cm"

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_area(self):
        return self._width * self._height

