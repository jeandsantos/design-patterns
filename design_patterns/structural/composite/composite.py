class GraphicObject:
    def __init__(self, colour: str | None = None):
        self.colour = colour
        self.children: list[GraphicObject] = []
        self._name: str = "Group"

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append("*" * depth)
        if self.colour:
            items.append(self.colour)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


def main():
    drawing = GraphicObject()
    drawing._name = "Drawing"
    drawing.children.append(Circle("Red"))
    drawing.children.append(Square("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)
    print(drawing)


if __name__ == "__main__":
    main()

    # output:
    # Drawing
    # *RedCircle
    # *YellowSquare
    # *Group
    # **BlueCircle
    # **BlueSquare
