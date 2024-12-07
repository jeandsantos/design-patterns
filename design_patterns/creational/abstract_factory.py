from abc import ABC
from enum import StrEnum
from typing import ClassVar


class DrinkTypes(StrEnum):
    TEA = "Tea"
    COFFEE = "Coffee"


class Drink(ABC):
    def consume(self):
        pass


class Tea(Drink):
    def consume(self):
        print("This tea is delicious")


class Coffee(Drink):
    def consume(self):
        print("This coffee is delicious")


class DrinkFactory(ABC):
    def prepare(self, amount: int | float) -> Drink:
        pass


class TeaFactory(DrinkFactory):
    def prepare(self, amount: int | float) -> Drink:
        print("Put in tea bag, boil water")
        print(f"Prepare {amount} ml of tea")
        return Tea()


class CoffeeFactory(DrinkFactory):
    def prepare(self, amount: int | float) -> Drink:
        print("Grind some beans, boil water")
        print(f"Prepare {amount} ml of coffee")
        return Coffee()


class DrinkMachine:
    factories: ClassVar[list[str, DrinkFactory]] = []
    initialized: bool = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True

            for drink in DrinkTypes:
                factory_name = drink.value + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self, drink: DrinkTypes, amount: int | float) -> Drink:
        for factory_name, factory_instance in self.factories:
            if factory_name == drink.value + "Factory":
                return factory_instance.prepare(amount)
        raise ValueError(f"Unknown drink: {drink}")


drink_machine = DrinkMachine()


def main():
    for drink_name in DrinkTypes:
        print(f"\nMaking {drink_name}")
        drink = drink_machine.make_drink(drink_name, 200)
        drink.consume()


if __name__ == "__main__":
    main()
