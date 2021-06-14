"""
Creating BankAccount class
"""

class BankAccount(object):
    def __init__(self,balance=0):
        self.balance=balance
    
"""
Method to show balance after depositing cash to bank account
"""

def deposit(self,amount):
    self.balance+= amount
    return self.balance

"""
Method that updates balance after withdrawal,no transation if amount>balance
"""

def withdraw(self, amount):
    if amount > self.balance:
        return ("INVALID TRANSACTION")
        self.balance-= amount
        return self.balance

"""
Creating a subclass
"""

class MinimumBalanceAccount(BankAccount):
    pass


"""
-Test variables
-pondiAccount=BankAccount()
-faithAccount=MinimumBalanceAccount()
-pondiAccount.deposit(5000)
-faithAccount.deposit(40000)
"""