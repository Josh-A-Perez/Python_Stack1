"""
Creating BankAccount class
Add a deposit method to the BankAccount class
Add a withdraw method to the BankAccount class
Add a display_account_info method to the BankAccount class
"""

class BankAccount:
    def __init__(self,interest_rate = 0, balance = 0):
        self.int_rate = interest_rate
        self.balance = balance

    def deposit(self,amount):
            self.balance += amount
            print(self.balance)
            return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("INVALID TRANSACTION")
        elif self.balance > 0:
            self.balance -= amount
            print(self.balance)
        return self

    def display_account_info(self, amount):
        print(self.balance)
        return self

    def yield_interest(self, amount):
        if self.balance > 0:
            self.int_rate = amount * self.balance
            print(self.int_rate + self.balance)
        return self

Josh = BankAccount(0,300)

Josh.deposit(400)
Josh.withdraw(30)
Josh.yield_interest(.05)

Rick = BankAccount(0,1000)

Rick.deposit(200)
Rick.withdraw(20)
Rick.yield_interest(.02)