from dataclasses import dataclass
from typing import Protocol


class DocumentState(Protocol):
    def edit(self): ...

    def review(self): ...

    def finalize(self): ...


class DocumentContext(Protocol):
    content: list[str]

    def set_state(self, state: DocumentState) -> None: ...

    def edit(self) -> None: ...

    def review(self) -> None: ...

    def finalize(self) -> None: ...

    def show_content(self) -> None: ...


@dataclass
class Draft:
    document: DocumentContext

    def edit(self) -> None:
        print("Editing document")
        self.document.content.append("New content")

    def review(self) -> None:
        print("Document is now under review")
        self.document.set_state(Reviewed(self.document))

    def finalize(self) -> None:
        print("You need to review the document before finalizing it")


@dataclass
class Reviewed:
    document: DocumentContext

    def edit(self) -> None:
        print("The document is under review, you can't edit it now.")

    def review(self) -> None:
        print("The document is already under review")

    def finalize(self) -> None:
        print("Finalizing document")
        self.document.set_state(Finalized(self.document))


@dataclass
class Finalized:
    document: DocumentContext

    def edit(self) -> None:
        print("The document is finalized. Editing is not allowed.")

    def review(self) -> None:
        print("The document is finalized. Reviewing is not allowed.")

    def finalize(self) -> None:
        print("The document is already finalized")


class Document:
    def __init__(self):
        self.state: DocumentState = Draft(self)
        self.content: list[str] = []

    def set_state(self, state: DocumentState) -> None:
        self.state = state

    def edit(self) -> None:
        self.state.edit()

    def review(self) -> None:
        self.state.review()

    def finalize(self) -> None:
        self.state.finalize()
