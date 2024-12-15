"""Class decorator."""

from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius: float | int):
        self.radius = radius

    def resize(self, factor: float | int):
        self.radius *= factor

    def __str__(self):
        return f"Circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, side: float | int):
        self.side = side

    def resize(self, factor: float | int):
        self.side *= factor

    def __str__(self):
        return f"Square with side {self.side}"


class ColouredShape(Shape):
    def __init__(self, shape: Shape, colour: str):
        self.shape = shape
        self.colour = colour

    def __str__(self):
        return f"{self.shape} has the colour {self.colour}"


class TransparentShape(Shape):
    def __init__(self, shape: Shape, transparency: float):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency*100.:.2f}% transparency"


def main():
    circle = Circle(5)
    print(circle)

    red_circle = ColouredShape(circle, "red")
    print(red_circle)

    transparent_red_circle = TransparentShape(red_circle, 0.5)
    print(transparent_red_circle)

    mixed_colour_square = ColouredShape(ColouredShape(Square(5), "red"), "blue")
    print(mixed_colour_square)


if __name__ == "__main__":
    main()
    # output:
    # Circle with radius 5
    # Circle with radius 5 has the colour red
    # Circle with radius 5 has the colour red has 50.00% transparency
    # Square with side 5 has the colour red has the colour blue
