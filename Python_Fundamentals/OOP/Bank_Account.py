"""
Creating BankAccount class
Add a deposit method to the BankAccount class
Add a withdraw method to the BankAccount class
Add a display_account_info method to the BankAccount class
"""

class BankAccount:
    def __init__(self,interest_rate = 0, balance = 0):
        self.interest_rate = interest_rate
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

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_Amount = self.interest_rate * self.balance
            self.balance += interest_Amount
        return self   

Josh = BankAccount(.03,1000)

Josh.deposit(100)
Josh.deposit(120)
Josh.deposit(200)
Josh.withdraw(60)
Josh.yield_interest().display_account_info()

Rick = BankAccount(.02,1000)

Rick.deposit(350)
Rick.deposit(200)
Rick.withdraw(20)
Rick.withdraw(80)
Rick.withdraw(100)
Rick.withdraw(40)

Rick.yield_interest().display_account_info()