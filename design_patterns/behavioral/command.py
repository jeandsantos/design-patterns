"""Bank account with command pattern."""

from abc import ABC, abstractmethod

OVERDRAFT_LIMIT: int = -500


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


class WithdrawCommand(Command):
    def __init__(self, account: BankAccount, amount: int):
        self.account = account
        self.amount = amount
        self.success: bool | None = None

    def invoke(self):
        self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        self.account.deposit(self.amount)


class DepositCommand(Command):
    def __init__(self, account: BankAccount, amount: int):
        self.account = account
        self.amount = amount
        self.success: bool | None = None

    def invoke(self):
        self.account.deposit(self.amount)
        self.success = True

    def undo(self):
        if not self.success:
            return
        self.account.withdraw(self.amount)


def main():
    bank_account = BankAccount(0)
    print(bank_account, "\n")

    deposit_command = DepositCommand(bank_account, 1000)
    deposit_command.invoke()
    print(bank_account)
    deposit_command.undo()
    print(bank_account, "\n")

    unauthorized_withdrawal_command = WithdrawCommand(bank_account, 1000)
    unauthorized_withdrawal_command.invoke()
    print(bank_account)
    unauthorized_withdrawal_command.undo()
    print(bank_account)


if __name__ == "__main__":
    main()
    # Output:
    # Balance: 0
    #
    # Deposited 1000. Current balance: 1000
    # Balance: 1000
    # Withdrew 1000. Current balance: 0
    # Balance: 0
    #
    # Insufficient funds
    # Balance: 0
    # Balance: 0
