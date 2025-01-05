class Creature:
    _strength_idx: int = 0
    _agility_idx: int = 1
    _intelligence_idx: int = 2

    def __init__(self, strength: int = 10, agility: int = 10, intelligence: int = 10):
        # use list-backed properties
        self.statistics: list[int] = [strength, agility, intelligence]

    @property
    def strength(self) -> int:
        return self.statistics[Creature._strength_idx]

    @strength.setter
    def strength(self, value: int):
        self.statistics[Creature._strength_idx] = value

    @property
    def agility(self) -> int:
        return self.statistics[Creature._agility_idx]

    @agility.setter
    def agility(self, value: int):
        self.statistics[Creature._agility_idx] = value

    @property
    def intelligence(self) -> int:
        return self.statistics[Creature._intelligence_idx]

    @intelligence.setter
    def intelligence(self, value: int):
        self.statistics[Creature._intelligence_idx] = value

    @property
    def total(self) -> int:
        return sum(self.statistics)

    @property
    def max(self) -> int:
        return max(self.statistics)

    @property
    def average(self) -> float:
        return float(sum(self.statistics) / len(self.statistics))


def main():
    creature = Creature(10, 20, 30)
    print(f"creature.strength: {creature.strength}")
    print(f"creature.agility: {creature.agility}")
    print(f"creature.intelligence: {creature.intelligence}")
    print(f"creature.total: {creature.total}")
    print(f"creature.max: {creature.max}")
    print(f"creature.average: {creature.average}")


if __name__ == "__main__":
    main()
    # output:
    # creature.strength: 10
    # creature.agility: 20
    # creature.intelligence: 30
    # creature.total: 60
    # creature.max: 30
    # creature.average: 20.0
