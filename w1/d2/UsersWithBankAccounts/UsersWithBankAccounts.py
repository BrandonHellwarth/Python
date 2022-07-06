class BankAccount:
    def __init__(self, interest_rate = 0, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        self.arr = []
    def deposit(self, amount):
        self.balance += amount
        self.arr.append(f"deposit: ${amount}")
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            self.arr.append("Insufficient funds: -$5")
        else:
            self.balance -= amount
            self.arr.append(f"withdraw: ${amount}")
            return self
    def display_account_info(self):
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance >= 0:
            b = self.balance * self.interest_rate#stores amount added so it can be printed later
            self.balance = self.balance + self.balance * self.interest_rate
            self.arr.append(f"Yielded interest added: {b}")
        return self
    def statement(self):
        print(self.arr)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
            self.account.deposit(amount)
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print(self.account.balance)
user = User("Brandon", "gmail.com")
user.make_deposit(50)
user.make_withdraw(25)
user.display_user_balance()
