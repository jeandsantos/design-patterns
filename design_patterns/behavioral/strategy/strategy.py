from abc import ABC, abstractmethod
from enum import StrEnum, auto


class OutputFormat(StrEnum):
    MARKDOWN = auto()
    HTML = auto()


class ListStrategy(ABC):
    @abstractmethod
    def start(self, buffer: list): ...

    @abstractmethod
    def end(self, buffer: list): ...

    @abstractmethod
    def add_list_item(self, buffer: list, item: str): ...


class MarkdownListStrategy(ListStrategy):
    def start(self, buffer: list):
        buffer.append("\n")

    def end(self, buffer: list):
        buffer.append("\n")

    def add_list_item(self, buffer: list, item: str):
        buffer.append(f"* {item}\n")


class HTMLListStrategy(ListStrategy):
    def start(self, buffer: list):
        buffer.append("<ul>\n")

    def end(self, buffer: list):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer: list, item: str):
        buffer.append(f"  <li>{item}</li>\n")


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HTMLListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items: list[str]):
        self.list_strategy.start(self.buffer)

        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)

        self.list_strategy.end(self.buffer)

    def set_output_format(self, output_format: OutputFormat):
        if output_format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif output_format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


def main():
    items = ["Item 1", "Item 2", "Item 3"]
    text_processor = TextProcessor()
    text_processor.set_output_format(OutputFormat.HTML)
    text_processor.append_list(items)
    print(text_processor)

    text_processor.clear()
    text_processor.set_output_format(OutputFormat.MARKDOWN)
    text_processor.append_list(items)
    print(text_processor)


if __name__ == "__main__":
    main()
    # output:
    # <ul>
    #   <li>Item 1</li>
    #   <li>Item 2</li>
    #   <li>Item 3</li>
    # </ul>
    #
    #
    # * Item 1
    # * Item 2
    # * Item 3
    #
