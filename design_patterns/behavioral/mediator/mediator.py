from __future__ import annotations

CHAT_TEMPLATE = "{sender}: {message}"


class Person:
    def __init__(self, name: str):
        self.name = name
        self.chat_log: list[str] = []
        self.room: ChatRoom | None = None

    def receive(self, sender: str, message: str):
        text = CHAT_TEMPLATE.format(sender=sender, message=message)
        print(f"[{self.name}'s chat session] {text}")
        self.chat_log.append(text)

    def send(self, message: str):
        self.room.broadcast(self.name, message)

    def send_private_message(self, receiver: Person, message: str):
        self.room.message(self.name, receiver.name, message)


class ChatRoom:
    def __init__(self):
        self.people: list[Person] = []

    def join(self, person: Person):
        join_message = f"{person.name} joins the chat"
        self.broadcast("room", join_message)

        person.room = self
        self.people.append(person)

    def broadcast(self, source: str, message: str):
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def message(self, source: str, destination: str, message: str):
        for person in self.people:
            if person.name == destination:
                person.receive(source, message)


def main():
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.send("Hi everyone!")
    jane.send("Hello John!")

    susy = Person("Susy")
    room.join(susy)
    susy.send("Hello everyone!")

    jane.send_private_message(susy, "Hi Susy")
    susy.send_private_message(jane, "Hi Jane")


if __name__ == "__main__":
    main()
    # output:
    # [John's chat session] room: Jane joins the chat
    # [Jane's chat session] John: Hi everyone!
    # [John's chat session] Jane: Hello John!
    # [John's chat session] room: Susy joins the chat
    # [Jane's chat session] room: Susy joins the chat
    # [John's chat session] Susy: Hello everyone!
    # [Jane's chat session] Susy: Hello everyone!
    # [Jane's chat session] Susy: Hi Jane
    # [Susy's chat session] Jane: Hi Susy
