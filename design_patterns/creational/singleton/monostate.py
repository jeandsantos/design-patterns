from typing import ClassVar


class CEO:
    __shared_state: ClassVar[dict] = {
        "name": "Steve",
        "age": 55,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Monostate:
    _shared_state: ClassVar[dict] = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}"


def main():
    cfo1 = CFO()
    cfo1.name = "Jane"
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 2

    print(cfo1)
    print(cfo2)


if __name__ == "__main__":
    main()
    # output:
    # Jane manages $1
    # Ruth manages $2
    # Ruth manages $2
