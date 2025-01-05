from enum import Enum, auto


class ValueType(Enum):
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()


class BinaryExpressionType(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()


class Token:
    def __init__(self, type: ValueType, text: str):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(expression: str):
    result = []

    idx = 0
    while idx < len(expression):
        if expression[idx] == "+":
            result.append(Token(ValueType.PLUS, "+"))
        elif expression[idx] == "-":
            result.append(Token(ValueType.MINUS, "-"))
        elif expression[idx] == "(":
            result.append(Token(ValueType.LEFT_PARENTHESIS, "("))
        elif expression[idx] == ")":
            result.append(Token(ValueType.RIGHT_PARENTHESIS, ")"))
        else:
            digits = [expression[idx]]
            for i in range(idx + 1, len(expression)):
                if expression[i].isdigit():
                    digits.append(expression[i])
                    idx += 1
                else:
                    result.append(Token(ValueType.INTEGER, "".join(digits)))
                    break

        idx += 1

    return result


class Integer:
    def __init__(self, value: int):
        self.value = value


class BinaryExpression:
    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == BinaryExpressionType.ADDITION:
            return self.left.value + self.right.value
        if self.type == BinaryExpressionType.SUBTRACTION:
            return self.left.value - self.right.value

        raise ValueError(f"Unknown binary expression type: {self.type}")


def calc(expression: str) -> None:
    tokens = lex(expression)
    print(" ".join(str(token) for token in tokens))

    parsed = parse(tokens)
    print(f"{expression} = {parsed.value}")


def parse(tokens: list[Token]):
    result = BinaryExpression()

    have_lhs = False

    idx = 0

    while idx < len(tokens):
        token = tokens[idx]

        if token.type == ValueType.INTEGER:
            integer = Integer(int(token.text))

            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == ValueType.PLUS:
            result.type = BinaryExpressionType.ADDITION
        elif token.type == ValueType.MINUS:
            result.type = BinaryExpressionType.SUBTRACTION
        elif token.type == ValueType.LEFT_PARENTHESIS:
            j = idx
            while j < len(tokens):
                if tokens[j].type == ValueType.RIGHT_PARENTHESIS:
                    break
                j += 1
            element = parse(tokens[idx + 1 : j])
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            idx = j

        idx += 1

    return result


if __name__ == "__main__":
    calc("(13+4)-(12+1)")

    # output:
    # `(` `13` `+` `4` `)` `-` `(` `12` `+` `1` `)`
    # (13+4)-(12+1) = 4
