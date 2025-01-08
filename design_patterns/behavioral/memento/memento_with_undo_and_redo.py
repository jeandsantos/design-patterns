class Memento:
    def __init__(self, balance: int):
        self.balance = balance

    def __str__(self):
        return f"Snapshot of bank account with balance: {self.balance}"


class BankAccout:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.changes: list[Memento] = [Memento(self.balance)]
        self.current_index: int = 0
        print(f"Created bank account with balance: {self.balance}")

    def deposit(self, amount: int) -> Memento:
        self.balance += amount
        memento = Memento(self.balance)
        self.changes.append(memento)
        self.current_index += 1
        print(f"Deposited {amount}. Current balance: {self.balance}")
        return memento

    def withdraw(self, amount: int) -> Memento:
        self.balance -= amount
        memento = Memento(self.balance)
        self.changes.append(memento)
        self.current_index += 1
        print(f"Withdrew {amount}. Current balance: {self.balance}")
        return memento

    def restore(self, memento: Memento) -> None:
        if memento is not None:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current_index = len(self.changes) - 1
            print(f"Restoring balance to {memento.balance}")

    def undo(self) -> Memento | None:
        if self.current_index > 0:
            self.current_index -= 1
            memento = self.changes[self.current_index]
            self.balance = memento.balance
            print(f"Undoing {memento}. Current balance: {self.balance}")
            return memento

        return None

    def redo(self) -> Memento | None:
        if self.current_index + 1 < len(self.changes):
            self.current_index += 1
            memento = self.changes[self.current_index]
            self.balance = memento.balance
            print(f"Redoing {memento}. Current balance: {self.balance}")
            return memento

        return None

    def __str__(self):
        return f"Balance: {self.balance}"


def main():
    bank_account = BankAccout(1000)

    bank_account.deposit(100)
    bank_account.deposit(200)

    bank_account.undo()
    bank_account.undo()

    bank_account.redo()
    bank_account.redo()


if __name__ == "__main__":
    main()
    # output:
    # Created bank account with balance: 1000
    # Deposited 100. Current balance: 1100
    # Deposited 200. Current balance: 1300
    # Undoing Snapshot of bank account with balance: 1100. Current balance: 1100
    # Undoing Snapshot of bank account with balance: 1000. Current balance: 1000
    # Redoing Snapshot of bank account with balance: 1100. Current balance: 1100
    # Redoing Snapshot of bank account with balance: 1300. Current balance: 1300
