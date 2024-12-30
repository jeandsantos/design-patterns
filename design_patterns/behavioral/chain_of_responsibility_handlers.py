"""Chain of Responsibility pattern.

All Concrete Handlers either handle a request or pass it to the next handler in the chain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import StrEnum

HANDLER_TEMPLATE = "{handler}: I'll eat the {request}"


class Request(StrEnum):
    BANANA = "Banana"
    NUT = "Nut"
    MEATBALL = "MeatBall"


class Handler(ABC):
    """Handler interface.

    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: ...

    @abstractmethod
    def handle(self, request) -> str | None: ...


class AbstractHandler(Handler):
    """An abstract class for concrete handlers.

    The default chaining behavior can be implemented inside a base handler class.
    """

    _next_handler: Handler | None = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Request) -> str:
        if self._next_handler is not None:
            return self._next_handler.handle(request)

        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request == Request.BANANA:
            return HANDLER_TEMPLATE.format(handler=self.__class__.__name__, request=request)
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request == Request.NUT:
            return HANDLER_TEMPLATE.format(handler=self.__class__.__name__, request=request)
        return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request == Request.MEATBALL:
            return HANDLER_TEMPLATE.format(handler=self.__class__.__name__, request=request)
        return super().handle(request)


def client_code(handler: Handler) -> None:
    """Client code sends a request to a handler.

    The client code is usually suited to work with a single handler.
    In most cases, it is not even aware that the handler is part of a chain.
    """
    for food in [Request.NUT, Request.BANANA, "Beetroot"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"\t{result}", end="")
        else:
            print(f"\t{food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)

    # output:
    # Chain: Monkey > Squirrel > Dog
    #
    # Client: Who wants a Nut?
    #         SquirrelHandler: I'll eat the Nut
    # Client: Who wants a Banana?
    #         MonkeyHandler: I'll eat the Banana
    # Client: Who wants a Beets?
    #         Beets was left untouched.
    #
    # Subchain: Squirrel > Dog
    #
    # Client: Who wants a Nut?
    #         SquirrelHandler: I'll eat the Nut
    # Client: Who wants a Banana?
    #         Banana was left untouched.
    # Client: Who wants a Beetroot?
    #         Beets was left untouched.
