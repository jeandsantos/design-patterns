from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


def main():
    code = "1234"

    state = State.LOCKED
    entry = ""

    while True:
        if state == State.LOCKED:
            entry += input(entry)

            if entry == code:
                state = State.UNLOCKED

            if not code.startswith(entry):
                state = State.FAILED

        elif state == State.FAILED:
            print("Access denied")
            entry = ""
            state = State.LOCKED

        elif state == State.UNLOCKED:
            print("Access granted")
            break


if __name__ == "__main__":
    main()
    # output:
    # hello
    # Access denied
    # 1
    # 12
    # 123
    # 1234
    # Access granted
