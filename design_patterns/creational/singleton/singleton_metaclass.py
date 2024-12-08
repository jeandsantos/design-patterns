from __future__ import annotations

import typing


class Singleton(type):
    _instances: typing.ClassVar[dict[type, object]] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, connection_string: str | None = None):
        print("Loading database")
        if connection_string is not None:
            self.connection_string = connection_string

    def __str__(self):
        return f"Database({self.connection_string})"

    def __eq__(self, other: Database):
        return self.connection_string == other.connection_string


def main():
    db1 = Database(connection_string="localhost:5000")
    print(db1)
    db2 = Database()
    print(db2)

    print(db1 == db2)
    print(db1 is db2)


if __name__ == "__main__":
    main()
    # output:
    # Loading database
    # Database(localhost:5000)
    # Database(localhost:5000)
    # True
    # True
