"""Protection proxy."""

MINIMUM_DRIVING_AGE: int = 18


class DriverAgeError(ValueError): ...


class Driver:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"{self.driver.name} drives the car")


class CarProxy:
    """Protection proxy for Car."""

    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= MINIMUM_DRIVING_AGE:
            self._car.drive()
        else:
            raise DriverAgeError(f"{self.driver.name} is too young to drive")


def main():
    for age in [12, 35]:
        print(f"Driver age: {age}")
        driver = Driver("John Doe", age)
        try:
            car = CarProxy(driver)
            car.drive()
        except DriverAgeError as exception:
            print(f"Exception raised: {exception}")


if __name__ == "__main__":
    main()
    # output:
    # Driver age: 12
    # Exception raised: John Doe is too young to drive
    # Driver age: 35
    # John Doe drives the car
