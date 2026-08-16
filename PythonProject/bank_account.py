class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self.balance += amount
        self._history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.balance:
            print("Error: Not enough funds.")
            return
        self.balance -= amount
        self._history.append(f"Withdraw: {amount}")

    def get_balance(self):
        return self.balance

    @property
    def history(self):
        return self._history


if __name__ == "__main__":
    print("Python")
    account = BankAccount("Alice", 100)
    print(f"Current balance: {account.get_balance()}")
    account.withdraw(150)
    print(f"Current balance: {account.get_balance()}")
    account.withdraw(-50)
    print(f"Current balance: {account.get_balance()}")

    print("\nPython")
    account2 = BankAccount("Bob", 50)
    print(f"Current balance: {account2.get_balance()}")
    print("Operation history:")
    account2.deposit(50)
    account2.withdraw(100)
    for operation in account2.history:
        print(f"    {operation}")
