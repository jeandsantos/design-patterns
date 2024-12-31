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
    def __init__(self):
        self.success: bool = False

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


class TransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: int):
        super().__init__(
            [
                BankAccountCommand(from_account, Actions.WITHDRAW, amount),
                BankAccountCommand(to_account, Actions.DEPOSIT, amount),
            ],
        )

    def invoke(self):
        is_previous_operation_successful = True
        for command in self:
            if is_previous_operation_successful:
                command.invoke()
                is_previous_operation_successful = command.success
            else:
                command.success = False

        self.success = is_previous_operation_successful


def main():
    for transfer_amount in [80, 1000]:
        print(f"Transfer amount: {transfer_amount}\n")

        bank_account_1 = BankAccount(100)
        bank_account_2 = BankAccount(0)
        print("bank_account_1", bank_account_1)
        print("bank_account_2", bank_account_2)
        print()

        print("Invoke")
        transfer_command = TransferCommand(bank_account_1, bank_account_2, transfer_amount)
        transfer_command.invoke()
        print("bank_account_1", bank_account_1)
        print("bank_account_2", bank_account_2)
        print("Command success: ", transfer_command.success)
        print()

        print("Undo")
        transfer_command.undo()
        print("bank_account_1", bank_account_1)
        print("bank_account_2", bank_account_2)
        print("Command success: ", transfer_command.success)
        print("-" * 50)


if __name__ == "__main__":
    main()
