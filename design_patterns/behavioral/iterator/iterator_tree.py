from __future__ import annotations

from collections.abc import Generator
from typing import Any


class Node:
    def __init__(self, value: Any, left: Node | None = None, right: Node | None = None):
        self.value = value
        self.left = left
        self.right = right

        self.parent: Node | None = None

        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class InOrderIterator:
    def __init__(self, root: Node):
        self.root = self.current = root
        self.yielded_start_value = False

        while self.current.left is not None:
            self.current = self.current.left

    def __next__(self):
        if self.yielded_start_value is False:
            self.yielded_start_value = True
            return self.current

        if self.current.right is not None:
            self.current = self.current.right

            while self.current.left is not None:
                self.current = self.current.left

            return self.current

        parent = self.current.parent

        while parent is not None and self.current == parent.right:
            self.current = parent
            parent = self.current.parent

        self.current = parent

        if self.current is None:
            raise StopIteration

        return self.current


def traverse_in_order(root: Node) -> Generator[Node, None, None]:
    def traverse(current: Node) -> Generator[Node, None, None]:
        if current.left is not None:
            for left in traverse(current.left):  # noqa: UP028
                yield left
        yield current
        if current.right is not None:
            for right in traverse(current.right):  # noqa: UP028
                yield right

    for node in traverse(root):  # noqa: UP028
        yield node


if __name__ == "__main__":
    #      1
    #    /   \
    #   2     3

    # Traversal methods
    # in-order: 2, 1, 3
    # pre-order: 1, 2, 3
    # post-order: 2, 3, 1

    root = Node(1, left=Node(2), right=Node(3))

    print("Iterating with for loop")
    for node in root:
        print(node)

    print("Iterating with iter()")
    iterator = iter(root)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass

    print("Iterating with list comprehension")
    print([node.value for node in root])

    print("Iterating with traverse_in_order()")
    for node in traverse_in_order(root):
        print(node)

    # output:
    # Iterating with for loop
    # 2
    # 1
    # 3
    # Iterating with iter()
    # 2
    # 1
    # 3
    # Iterating with list comprehension
    # [2, 1, 3]
    # Iterating with traverse_in_order()
    # 2
    # 1
    # 3
