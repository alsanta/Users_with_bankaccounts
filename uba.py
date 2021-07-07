class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposit {amount}\n")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You withdraw {amount}\n")
        else:
            print (f"You have {self.balance} and tried withdrawing {amount}\n You have insufficient funds and the transaction will be cancelled\n")
        return self

    def display_account_info(self):
        print(f"Your balance is {self.balance}\n")
        return self

    def yield_interest(self):
        gained = self.balance * self.int_rate
        self.balance += self.balance * self.int_rate
        print(f"Congrats you have gained {gained} in intrest\n")
        return self

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

alex = User('Alex')
alex.make_deposit(500).make_deposit(1500)
alex.display_user_balance()

