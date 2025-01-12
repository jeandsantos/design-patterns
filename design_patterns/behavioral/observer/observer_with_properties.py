from typing import Any


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age: int):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        person.property_changed.append(self.notify)

    def notify(self, property_name: str, value: Any):
        if property_name == "age":
            if value < 18:
                print("You are too young to drive")
            else:
                print("You are old enough to drive now")
                self.person.property_changed.remove(self.notify)


def main():
    person = Person(15)
    traffic_authority = TrafficAuthority(person)  # noqa: F841

    for age in range(16, 21):
        print(f"Person age: {age}")
        person.age = age


if __name__ == "__main__":
    main()
    # output:
    # Person age: 16
    # You are too young to drive
    # Person age: 17
    # You are too young to drive
    # Person age: 18
    # You are old enough to drive now
    # Person age: 19
    # Person age: 20
