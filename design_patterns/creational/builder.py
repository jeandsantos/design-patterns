from __future__ import annotations


class HTMLElement:
    indent_size: int = 2

    def __init__(self, name: str = "", text: str = ""):
        self.text: str = text
        self.name: str = name
        self.elements: list = []

    def __str(self, indent: int) -> str:
        lines: list[str] = []
        i: str = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent + 1))  # noqa: PERF401

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)


class HTMLBuilder:
    def __init__(self, root_name: str):
        self.root_name: str = root_name
        self.__root: HTMLElement = HTMLElement(name=root_name)

    def add_child(self, child_name: str, child_text: str):
        self.__root.elements.append(
            HTMLElement(
                name=child_name,
                text=child_text,
            )
        )

    def add_child_fluent(self, child_name: str, child_text: str) -> HTMLBuilder:
        self.__root.elements.append(
            HTMLElement(
                name=child_name,
                text=child_text,
            )
        )
        return self

    def __str__(self):
        return str(self.__root)


def main():
    builder = HTMLBuilder(root_name="ul")
    builder.add_child_fluent(child_name="li", child_text="hello").add_child_fluent(child_name="li", child_text="world")

    html = str(builder)
    print(html)


if __name__ == "__main__":
    main()
    # output:
    # <ul>
    #   <li>
    #     hello
    #   </li>
    #   <li>
    #     world
    # </li>
