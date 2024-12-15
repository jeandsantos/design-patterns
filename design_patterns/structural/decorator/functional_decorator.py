"""Functional decorator."""

import time
from collections.abc import Callable


def time_it(func: Callable) -> Callable:
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result

    return wrapper


@time_it
def some_operation():
    print("Starting operation")
    time.sleep(0.5)
    print("Finished operation")

    return 42


if __name__ == "__main__":
    some_operation()
    # output:
    # Starting operation
    # Finished operation
    # some_operation took 0.50527 seconds
