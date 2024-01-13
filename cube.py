from square import Square

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def __str__(self):
        return f"Cube with side {self._width} cm"

    def get_surface_area(self):
        return 6 * (self._width ** 2)

    def get_volume(self):
        return self._width ** 3
