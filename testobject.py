class BankAccount:
    def __init__(self,name,account_Number,ID_Number,age,deposit_amount,withdraw_amount ):
        self.name = name
        self.account_Number = account_Number
        self.ID_Number = ID_Number
        self.age = age
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount
    def deposit(self):
        self.balance = self.balance + self.deposit_amount
        return self.balance
    def withdraw(self,):
        self.balance =  self.balance - self.withdraw_amount
        return self.balance
    def bank_fees(self):
        self.balance = (self.balance * 0.05)
        return self.balance

