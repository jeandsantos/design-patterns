from __future__ import annotations

import math
from pathlib import Path
from typing import ClassVar

FILEPATH_CAPITALS = Path(__file__).parent.joinpath("capitals.txt")


def capitals_file() -> Path:
    text = """Tokyo
    32
    New York
    17
    Sao Paulo
    17
    Seoul
    17
    Manila
    14
    """

    with open(FILEPATH_CAPITALS, "w") as file:
        file.write(text)

    return FILEPATH_CAPITALS


class Singleton(type):
    _instances: ClassVar[dict] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population: dict[str, float] = {}
        file = open(FILEPATH_CAPITALS)
        lines = file.readlines()
        for i in range(0, len(lines) - 1, 2):
            self.population[lines[i].strip()] = float(lines[i + 1].strip())

        file.close()

    def __eq__(self, other: Database):
        equality_checks = []

        if len(self.population) != len(other.population):
            return False

        for city, population in self.population.items():
            check = population == other.population[city]
            equality_checks.append(check)

        return all(equality_checks)


class SingletonRecordFinder:
    def total_population(self, cities: list[str]):
        population_total = 0
        for city in cities:
            population_total += Database().population[city]
        return population_total


class DummyDatabase:
    population: ClassVar[dict] = {
        "city_1": 1_000,
        "city_2": 2_000,
        "city_3": 3_000,
    }

    def get_population(self, city: str) -> float | int:
        return self.population[city]


class ConfigurableRecordFinder:
    def __init__(self, db: Database):
        self.db = db

    def total_population(self, cities: list[str]):
        population_total = 0
        for city in cities:
            population_total += self.db.population[city]
        return population_total


class TestSingleton:
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()

        assert db1 == db2
        assert db1 is db2

    def test_singleton_total_population(self):
        record_finder = SingletonRecordFinder()
        cities = ["Tokyo", "Manila"]

        total_population = record_finder.total_population(cities)

        assert math.isclose(total_population, 32 + 14)

    def test_singleton_total_population_with_configurable_record_finder(self):
        dummy_database = DummyDatabase()
        record_finder = ConfigurableRecordFinder(dummy_database)
        cities = ["city_2", "city_3"]

        total_population = record_finder.total_population(cities)

        assert math.isclose(total_population, 2_000 + 3_000)


def main():
    capitals_file()

    TestSingleton().test_is_singleton()
    TestSingleton().test_singleton_total_population()
    TestSingleton().test_singleton_total_population_with_configurable_record_finder()


if __name__ == "__main__":
    main()
