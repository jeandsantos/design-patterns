"""Chain of Responsibility pattern."""

from __future__ import annotations


class Creature:
    def __init__(self, name: str, attack: int, defense: int):
        print(f"Creating {name}")
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense})"


class BaseModifier:
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier: BaseModifier | None = None

    def add_modifier(self, modifier: BaseModifier):
        if self.next_modifier is not None:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier is not None:
            self.next_modifier.handle()


class DoubleAttackModifier(BaseModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(BaseModifier):
    def handle(self):
        if self.creature.attack > 10:
            print(f"{self.creature.name}'s attack is too high, skipping defense increase")
        else:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1
        super().handle()


class NoBonusesModifier(BaseModifier):
    def handle(self):
        print(f"No bonuses for {self.creature.name}")


def main():
    wizard = Creature("Wizard", 10, 5)
    print(wizard)
    root_modifier = BaseModifier(wizard)
    root_modifier.add_modifier(IncreaseDefenseModifier(wizard))
    root_modifier.add_modifier(DoubleAttackModifier(wizard))
    root_modifier.add_modifier(IncreaseDefenseModifier(wizard))
    root_modifier.handle()
    print(wizard)

    print()

    dragon = Creature("Dragon", 100, 100)
    print(dragon)
    root_modifier = BaseModifier(dragon)
    root_modifier.add_modifier(NoBonusesModifier(dragon))
    root_modifier.add_modifier(IncreaseDefenseModifier(dragon))
    root_modifier.add_modifier(DoubleAttackModifier(dragon))
    root_modifier.handle()
    print(dragon)


if __name__ == "__main__":
    main()
    # output:
    # Creating Wizard
    # Wizard (Attack: 10, Defense: 5)
    # Increasing Wizard's defense
    # Doubling Wizard's attack
    # Wizard's attack is too high, skipping defense increase
    # Wizard (Attack: 20, Defense: 6)
    #
    # Creating Dragon
    # Dragon (Attack: 100, Defense: 100)
    # No bonuses for Dragon
    # Dragon (Attack: 100, Defense: 100)
