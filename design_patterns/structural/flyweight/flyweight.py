"""Flyweight pattern."""

import random
import typing


def random_first_name() -> str:
    return random.choice(["Diana", "Charlie", "Bob", "Alice"])


def random_last_name() -> str:
    return random.choice(["Smith", "Doe", "Khan", "Wilson"])


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class UserOptimized:
    strings: typing.ClassVar[list[str]] = []

    def __init__(self, full_name: str):
        def get_or_add(s: str) -> int:
            if s in self.strings:
                return self.strings.index(s)
            self.strings.append(s)
            return len(self.strings) - 1

        self.names = [get_or_add(name) for name in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[n] for n in self.names])


def main():
    random.seed(0)

    n_users = 12
    users = []
    first_names = [random_first_name() for _ in range(n_users)]
    last_names = [random_last_name() for _ in range(n_users)]

    for first_name, last_name in zip(first_names, last_names):
        user = UserOptimized(f"{first_name} {last_name}")
        print(user, "\t", user.names)
        users.append(user)


if __name__ == "__main__":
    main()
    # output:
    # Alice Doe        [0, 1]
    # Alice Smith      [0, 2]
    # Diana Khan       [3, 4]
    # Bob Doe          [5, 1]
    # Alice Khan       [0, 4]
    # Alice Smith      [0, 2]
    # Bob Smith        [5, 2]
    # Alice Khan       [0, 4]
    # Bob Wilson       [5, 6]
    # Charlie Smith    [7, 2]
    # Charlie Khan     [7, 4]
    # Bob Wilson       [5, 6]
