class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def weight(self, density):
        return self.area * density


if __name__ == '__main__':
    rect = Rectangle(width=5, height=3)
    print("before assignment")
    print(f"{rect.width=}")
    print(f"{rect.area=}")

    rect.width = 10
    print("\nafter assignment ")
    print(f"{rect.width=}")
    print(f"{rect.area=}")

    print("\ninvalid initialization as well as settings raise an error:\n")
    r = Rectangle(width=2, height=-5)
