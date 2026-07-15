#Create a class BankAccount with attributes owner and balance.
#Add methods deposit(amount) and withdraw(amount).
#Prevent withdrawing more than the available balance.
#Add a method display_balance().

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

account = BankAccount("Alice", 1000)
account.display_balance()  # Output: Alice's balance: 1000
account.deposit(500)       # Output: Deposited 500. New balance: 1500
account.withdraw(200)      # Output: Withdrew 200. New balance:
account.withdraw(2000)     # Output: Insufficient funds.
account.display_balance()  # Output: Alice's balance: 1300

