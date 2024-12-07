from enum import StrEnum
from math import cos, sin


class CoordinateSystem(StrEnum):
    CARTESIAN = "cartesian"
    POLAR = "polar"


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    @staticmethod
    def new_cartesian_point(x: float, y: float):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float):
        return Point(rho * cos(theta), rho * sin(theta))


def main():
    cartesian_point = Point.new_cartesian_point(3, 4)
    polar_point = Point.new_polar_point(5, 3)
    print(cartesian_point)
    print(polar_point)


if __name__ == "__main__":
    main()
