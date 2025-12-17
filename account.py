class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def view_balance(self):
        return self.balance
