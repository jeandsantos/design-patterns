from typing import ClassVar


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    cache: ClassVar[dict] = {}

    def __init__(self, line: Line):
        self.hash = hash(line)
        if self.hash in self.cache:
            return

        super().__init__()

        print(f"Generating points for line " f"({line.start.x}, {line.start.y}) - " f"({line.end.x}, {line.end.y})")

        # if self.hash in self.cache:
        #     self.extend(self.cache[self.hash])

        # print(f"({line.start.x}, {line.start.y}) - " f"({line.end.x}, {line.end.y})")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))  # noqa: PERF401
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))  # noqa: PERF401

        self.cache[self.hash] = points

    def __iter__(self):
        return iter(self.cache[self.hash])


def draw_point(point: Point):
    print(".", end="")


def draw(rectangles: list[Rectangle]):
    print("Draw rectangles")
    for rectangle in rectangles:
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for point in adapter:
                draw_point(point)


if __name__ == "__main__":
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]

    draw(rs)
