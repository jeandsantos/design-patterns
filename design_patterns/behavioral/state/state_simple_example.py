from typing import Protocol


class LightState(Protocol):
    def switch(self, bulb) -> None: ...


class OffState(LightState):
    def switch(self, bulb):
        bulb.state = OnState()
        print("Light is off")


class OnState(LightState):
    def switch(self, bulb):
        bulb.state = OffState()
        print("Light is on")


class Bulb:
    def __init__(self):
        self.state = OnState()

    def switch(self) -> None:
        self.state.switch(self)


def main() -> None:
    bulb = Bulb()
    bulb.switch()
    bulb.switch()


if __name__ == "__main__":
    main()
    # output:
    # Light is on
    # Light is off
