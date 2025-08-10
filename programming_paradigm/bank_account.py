# bank_account.py

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated balance

    def deposit(self, amount: float):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        """Withdraw money if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

