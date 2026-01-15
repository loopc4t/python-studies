class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._owner = None  # Protected (convention: single underscore)
        self.__balance = balance  # Private (name mangling: double score)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


account = BankAccount("123456", 1000)
account.deposit(500)
print(account.get_balance())
