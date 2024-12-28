class FormattedText:
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start: int, end: int):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = ""
        for i in range(len(self.plain_text)):
            if self.caps[i]:
                result += self.plain_text[i].upper()
            else:
                result += self.plain_text[i]
        return result


class BetterFormattedText:
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start: int, end: int, capitalize: bool = False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position: int) -> bool:
            return self.start <= position < self.end

    def get_range(self, start: int, end: int) -> TextRange:
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = ""
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for _range in self.formatting:
                if _range.covers(i) and _range.capitalize:
                    c = c.upper()
            result += c
        return result


def main():
    text = "My name is john doe"

    formatted_text = FormattedText(text)
    formatted_text.capitalize(11, 12)
    formatted_text.capitalize(16, 17)
    print(formatted_text)

    better_formatted_text = BetterFormattedText(text)
    better_formatted_text.get_range(11, 12).capitalize = True
    better_formatted_text.get_range(16, 17).capitalize = True
    print(better_formatted_text)

    assert str(formatted_text) == str(better_formatted_text)


if __name__ == "__main__":
    main()
    # output:
    # My name is John Doe
    # My name is John Doe
