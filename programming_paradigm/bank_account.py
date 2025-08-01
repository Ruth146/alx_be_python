class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Add amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds are available."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance with two decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
