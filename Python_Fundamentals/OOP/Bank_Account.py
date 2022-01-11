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

Steph = BankAccount(.03,1000)

Steph.deposit(100).deposit(120).deposit(200).withdraw(60).yield_interest().display_account_info()

###################################################################################################
Klay = BankAccount(.02,1000)

Klay.deposit(350).deposit(200).withdraw(20).withdraw(80).withdraw(100).withdraw(40).yield_interest().display_account_info()