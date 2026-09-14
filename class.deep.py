"""
OOP:
1.Encupsulation
2.Inheritance
3.Polymorphism
"""

# Encupsulation -> public __private _protected


class Account():
    description = "This class makes bank accounts"

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def getBalance(self):
        print(f"{self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("Deposit success")
        self.__amount += amount

    def withdraw(self, amount):
        print("Withdraw success")
        self.__amount -= amount

    # getter
    @property
    def holder(self):
        return self.__owner

    # setter
    @holder.setter
    def holder(self, new_owner):
        self.__owner = new_owner


account = Account("Nathan", 25000)
account.getBalance()
account.deposit(10000)
account.getBalance()
account.withdraw(30000)
account.getBalance()

account_owner = account.holder  # state
print("Owner:", account_owner)

account.holder = "Declan"
print("New owner:", account.holder)
