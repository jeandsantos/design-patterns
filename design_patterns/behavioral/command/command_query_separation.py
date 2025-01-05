"""Event broker with command query separation."""

from abc import ABC, abstractmethod
from enum import Enum, auto


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class QueriableProperty(Enum):
    ATTACK = auto()
    DEFENSE = auto()


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class Query:
    def __init__(self, creature_name: str, property: QueriableProperty, default_value):
        self.value = default_value
        self.creature_name = creature_name
        self.property = property


class Creature:
    def __init__(self, game: Game, name: str, attack: int, defense: int):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        query = Query(self.name, QueriableProperty.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defense(self):
        query = Query(self.name, QueriableProperty.DEFENSE, self.initial_defense)
        self.game.perform_query(self, query)
        return query.value

    def __str__(self):
        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense})"


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender: Creature, query: Query): ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.game.queries.remove(self.handle)
        print(f"{self.creature.name}'s attack and defense returned to normal")


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if sender.name == self.creature.name and query.property == QueriableProperty.ATTACK:
            print(f"Doubling {self.creature.name}'s attack")
            query.value *= 2


def main():
    game = Game()

    wizard = Creature(game, "Wizard", 10, 5)
    print(wizard)

    with DoubleAttackModifier(game, wizard):
        print(wizard)

    print(wizard)


if __name__ == "__main__":
    main()
