"""Shapes and renderers."""

from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius: float | int):
        raise NotImplementedError

    def render_square(self, side: float | int):
        raise NotImplementedError


class VectorRenderer(Renderer):
    def render_circle(self, radius: float | int):
        print(f"Drawing a circle of radius {radius}")

    def render_square(self, side: float | int):
        print(f"Drawing a square with side {side}")


class RasterRenderer(Renderer):
    def render_circle(self, radius: float | int):
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_square(self, side: float | int):
        print(f"Drawing pixels for a square of side {side}")


class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float | int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer: Renderer, radius: float | int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_square(self.radius)

    def resize(self, factor):
        self.radius *= factor


def main():
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    square = Square(raster, 2)
    square.draw()
    square.resize(4)
    square.draw()


if __name__ == "__main__":
    main()

    # output:
    # Drawing a circle of radius 5
    # Drawing a circle of radius 10
    # Drawing pixels for a square of side 2
    # Drawing pixels for a square of side 8
