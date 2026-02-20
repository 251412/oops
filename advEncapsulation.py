class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   
        self.__balance = balance               

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
acc = BankAccount("lalli", 5000)

acc.deposit(2000)
acc.withdraw(1000)

print("Current Balance:", acc.get_balance())