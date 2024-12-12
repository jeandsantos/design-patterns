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
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    count: int = 0

    def __init__(self, line: Line):
        super().__init__()
        self.count += 1
        print(
            f"{self.count}: Generating points for line "
            f"({line.start.x}, {line.start.y}) - "
            f"({line.end.x}, {line.end.y})"
        )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left > bottom - top:
            self.extend(
                [
                    Point(left + t, top),
                    Point(left + t, bottom),
                ]
                for t in range(right - left)
            )
        else:
            self.extend(
                [
                    Point(left, top + t),
                    Point(right, top + t),
                ]
                for t in range(bottom - top)
            )


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
