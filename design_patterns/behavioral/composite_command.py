"""Bank account with command pattern."""

from abc import ABC, abstractmethod
from enum import Enum, auto

OVERDRAFT_LIMIT: int = -500


class Actions(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount: int) -> bool:
        if self.balance - amount < OVERDRAFT_LIMIT:
            print("Insufficient funds")
            return False
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")
        return True

    def __str__(self):
        return f"Balance: {self.balance}"


class Command(ABC):
    @abstractmethod
    def invoke(self): ...
    @abstractmethod
    def undo(self): ...


class BankAccountCommand(Command):
    def __init__(self, account: BankAccount, action: Actions, amount: int):
        self.account = account
        self.action = action
        self.amount = amount
        self.success: bool | None = None

    def invoke(self):
        if self.action == Actions.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == Actions.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
        else:
            raise ValueError(f"Unknown action: {self.action}")

    def undo(self):
        if not self.success:
            return

        if self.action == Actions.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == Actions.WITHDRAW:
            self.account.deposit(self.amount)
        else:
            raise ValueError(f"Unknown action: {self.action}")


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: list[Command] = []):
        super().__init__()
        self.extend(items)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in reversed(self):
            command.undo()


def main():
    bank_account = BankAccount()
    print(bank_account, "\n")

    deposit_command_1 = BankAccountCommand(bank_account, Actions.DEPOSIT, 1000)
    deposit_command_2 = BankAccountCommand(bank_account, Actions.DEPOSIT, 500)

    print("Invoke")
    composite_command = CompositeBankAccountCommand([deposit_command_1, deposit_command_2])
    composite_command.invoke()
    print(bank_account, "\n")

    print("Undo")
    composite_command.undo()
    print(bank_account)


if __name__ == "__main__":
    main()
