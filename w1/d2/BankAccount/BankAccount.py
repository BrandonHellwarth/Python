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
bankAccount = BankAccount(.1, 0)
bankAccount1 = BankAccount(.5, 20)
bankAccount.deposit(100).deposit(50).deposit(25).withdraw(100).yield_interest().display_account_info()
bankAccount1.deposit(20).deposit(200).withdraw(20).withdraw(20).withdraw(20).withdraw(40).yield_interest().display_account_info()
bankAccount.statement()