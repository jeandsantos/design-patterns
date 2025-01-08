class Memento:
    def __init__(self, balance: int):
        self.balance = balance

    def __str__(self):
        return f"Snapshot of bank account with balance: {self.balance}"


class BankAccout:
    def __init__(self, balance: int = 0):
        self.balance = balance
        print(f"Created bank account with balance: {self.balance}")

    def deposit(self, amount: int) -> Memento:
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")
        return Memento(self.balance)

    def withdraw(self, amount: int) -> Memento:
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")
        return Memento(self.balance)

    def restore(self, memento: Memento) -> None:
        print(f"Restoring balance to {memento.balance}")
        self.balance = memento.balance

    def __str__(self):
        return f"Balance: {self.balance}"


def main():
    bank_account = BankAccout(1000)

    memento_1 = bank_account.deposit(500)
    memento_2 = bank_account.withdraw(200)

    bank_account.restore(memento_1)
    bank_account.restore(memento_2)

    print(bank_account)


if __name__ == "__main__":
    main()
    # output:
    # Created bank account with balance: 1000
    # Deposited 500. Current balance: 1500
    # Withdrew 200. Current balance: 1300
    # Restoring balance to 1500
    # Restoring balance to 1300
    # Balance: 1300
