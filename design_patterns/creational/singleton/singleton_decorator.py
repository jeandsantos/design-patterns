def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Database:
    def __init__(self, connection_string: str | None = None):
        print("Loading database")
        if connection_string is not None:
            self.connection_string = connection_string

    def __str__(self):
        return f"Database({self.connection_string})"

    def __eq__(self, other):
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
