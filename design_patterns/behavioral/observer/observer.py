class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str):
    print(f"Calling doctor for {name} at {address}")


def main():
    person = Person("Bob", "123 London Road")
    person.falls_ill.append(call_doctor)

    person.catch_a_cold()

    person.falls_ill.remove(call_doctor)

    person.catch_a_cold()


if __name__ == "__main__":
    main()
    # output:
    # Calling doctor for Bob at 123 London Road
