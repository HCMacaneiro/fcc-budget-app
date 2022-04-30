class Category:
    total = 0
    def __init__(self, name, ledger=None):
        self.name = name
        if ledger is None:
            ledger = []
            self.ledger = ledger

    def deposit(self, amount, description = ""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})
        self.total += amount

    def withdraw(self, withdraw_amount, withdraw_description = ""):
        if self.check_funds(withdraw_amount) == True:
            self.withdraw_amount = -withdraw_amount
            self.withdraw_description = withdraw_description
            self.ledger.append({"amount": self.withdraw_amount, "description": withdraw_description})
            self.total -= withdraw_amount
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, transfer_amount, other_category):
        self.transfer_amount = transfer_amount
        self.withdraw(self.transfer_amount, f"Transfer to {other_category.name}")
        other_category.deposit(self.transfer_amount, f"Transfer from {self.name}")

    def check_funds(self, check_amount):
        self.check_amount = check_amount
        if self.check_amount > self.total:
            return False
        else:
            return True

    def __repr__(self):
        return f"{self.ledger}"


def create_spend_chart(categories):
    pass

