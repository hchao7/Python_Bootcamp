class BankAccount:
  def __init__(self, owner):
    self.owner = owner
    self.balance = 0.0

  def deposit(self, deposit):
    self.balance = self.balance + deposit
    return self.balance
  
  def withdraw(self, withdraw):
    self.balance = self.balance - withdraw
    return self.balance

acct = BankAccount("Darcy")
print(acct.owner) #Darcy
print(acct.balance) #0.0
print(acct.deposit(10))  #10.0
print(acct.withdraw(3))  #7.0
print(acct.balance)  #7.0