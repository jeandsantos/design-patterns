from enum import StrEnum, auto
from typing import Any


class Property(StrEnum):
    AGE = auto()
    CAN_VOTE = auto()


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

    @property
    def can_vote(self):
        return self._age >= 18

    @age.setter
    def age(self, value: int):
        if self._age == value:
            return

        previous_can_vote_value = self.can_vote

        self._age = value
        self.property_changed(Property.AGE, value)

        if previous_can_vote_value != self.can_vote:
            self.property_changed(Property.CAN_VOTE, self.can_vote)


def person_changed(name: Property, value: Any):
    if name == Property.CAN_VOTE:
        print(f"Voting status changed to {value}")


def main():
    person = Person(15)
    person.property_changed.append(person_changed)

    for age in range(16, 21):
        print(f"Person age: {age}")
        person.age = age


if __name__ == "__main__":
    main()
    # output:
    # Person age: 16
    # Person age: 17
    # Person age: 18
    # Voting status changed to True
    # Person age: 19
    # Person age: 20
