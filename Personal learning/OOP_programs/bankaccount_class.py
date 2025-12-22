class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_numer = account_number
        self.balance = balance 
#adding the methods for depositing
    def deposit(self, amount):
        self.balance += amount 
        print(f" Deposited ${amount}. Current balance: ${self.balance}.")

#adding the method for withdrawal
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuficient funds")
            return
        self.balance  -= amount 
        print(f"Withdrew ${amount}. Current balance: ${self.balance}.")
    
#adding method to check the balance
    def check_balance(self):
        print(f"The current balance: ${self.balance}.")
#test the class
account1 = BankAccount(15450, 0)
account1.deposit(50)
account1.withdraw(100)
account1.check_balance()
