"""Bank account with command pattern."""

from abc import ABC, abstractmethod
from enum import Enum, auto


class Actions(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


class BankAccount:
    OVERDRAFT_LIMIT: int = -500

    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount: int) -> bool:
        if self.balance - amount < BankAccount.OVERDRAFT_LIMIT:
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


def main():
    bank_account = BankAccount()
    print(bank_account)
    print()

    deposit_command = BankAccountCommand(bank_account, Actions.DEPOSIT, 1000)
    deposit_command.invoke()
    print(bank_account)
    deposit_command.undo()
    print(bank_account)

    print()

    illegal_command = BankAccountCommand(bank_account, Actions.WITHDRAW, 1000)
    illegal_command.invoke()
    print(bank_account)
    illegal_command.undo()
    print(bank_account)


if __name__ == "__main__":
    main()
