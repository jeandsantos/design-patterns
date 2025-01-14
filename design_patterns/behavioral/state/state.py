from enum import StrEnum, auto


class State(StrEnum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(StrEnum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    GET_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


def main():
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING),
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.GET_CONNECTED, State.CONNECTED),
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.OFF_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state.name.lower()}")

        for i in range(len(rules[state])):
            trigger = rules[state][i][0]
            print(f"\t{i}: {trigger}")
        idx = int(input("Select a trigger: "))

        state = rules[state][idx][1]

    print(f"We are done using the phone. The state is {state}")


if __name__ == "__main__":
    main()
    # e.g.:
    # The phone is currently off_hook
    #         0: call_dialed
    # Select a trigger: 0
    # The phone is currently connecting
    #         0: hung_up
    #         1: get_connected
    # Select a trigger: 1
    # The phone is currently connected
    #         0: left_message
    #         1: hung_up
    #         2: placed_on_hold
    # Select a trigger: 1
    # We are done using the phone. The state is on_hook
