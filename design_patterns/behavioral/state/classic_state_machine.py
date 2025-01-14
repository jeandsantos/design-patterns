from __future__ import annotations

from abc import ABC


class State(ABC):
    def on(self):
        print("Light is already on")

    def off(self):
        print("Light is already off")


class OnState(State):
    def __init__(self):
        print("Light turned on")

    def off(self, switch: Switch):
        print("Light is turned off")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light turned off")

    def on(self, switch: Switch):
        print("Light is turned on")
        switch.state = OnState()


class Switch:
    def __init__(self):
        self.state: State = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


def main():
    switch = Switch()

    switch.on()
    switch.off()
    switch.on()


if __name__ == "__main__":
    main()

    # output:
    # Light turned off
    # Light is turned on
    # Light turned on
    # Light is turned off
    # Light turned off
    # Light is turned on
    # Light turned on
