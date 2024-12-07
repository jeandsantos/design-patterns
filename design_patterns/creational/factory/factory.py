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


class PointFactory:
    @staticmethod
    def new_cartesian_point(x: float, y: float) -> Point:
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float) -> Point:
        return Point(rho * cos(theta), rho * sin(theta))


point_factory = PointFactory()


def main():
    cartesian_point = point_factory.new_cartesian_point(3, 4)
    polar_point = point_factory.new_polar_point(5, 3)
    print(cartesian_point)
    print(polar_point)


if __name__ == "__main__":
    main()
