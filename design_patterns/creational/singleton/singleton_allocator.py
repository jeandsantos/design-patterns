class Database:
    _instance = None

    def __init__(self):
        print("Loading database")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.connection_string = None

        return cls._instance

    def __str__(self):
        return f"Database({self.connection_string})"


def main():
    db1 = Database()
    print(db1)
    db1.connection_string = "localhost:5000"
    print(db1)

    db2 = Database()
    print(db2)

    print(db1 is db2)


if __name__ == "__main__":
    main()
    # output:
    # Creating new instance
    # Loading database
    # Database(None)
    # Database(localhost:5000)
    # Loading database
    # Database(localhost:5000)
    # True
