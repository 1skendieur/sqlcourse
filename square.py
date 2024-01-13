from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square with side {self._width} cm"

    def get_area(self):
        return f"The area of the square is {self._width * self._height} cm"

