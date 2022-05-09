class Category:
    total = 0
    def __init__(self, name, ledger=None):
        self.name = name
        if ledger is None:
            ledger = []
            self.ledger = ledger

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})
        self.total += amount

    def withdraw(self, withdraw_amount, withdraw_description=""):
        if self.check_funds(withdraw_amount) == True:
            self.withdraw_amount = -withdraw_amount
            self.withdraw_description = withdraw_description
            self.ledger.append({"amount": self.withdraw_amount, "description": withdraw_description})
            self.total -= withdraw_amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, transfer_amount, other_category):
        if self.check_funds(transfer_amount) == True:
            self.transfer_amount = transfer_amount
            self.withdraw(self.transfer_amount, f"Transfer to {other_category.name}")
            other_category.deposit(self.transfer_amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, check_amount):
        self.check_amount = check_amount
        if self.check_amount > self.total:
            return False
        else:
            return True

    def __str__(self):
        output = ""
        num_char_name = len(self.name)
        first_half_title = "*"*int(((30 - len(self.name)) / 2))
        second_half_title = "*"*int((30 - len(first_half_title) - len(self.name)))
        title = first_half_title + self.name + second_half_title + "\n"
        output += title
        for transactions in self.ledger:
            amount = ""
            description = ""
            for key in transactions:
                if key == "amount":
                    amount = transactions[key]
                    price = amount
                    amount = "{:.2f}".format(price)
                    if len(amount) > 7:
                        amount = amount[:7]
                elif key == "description":
                    if len(transactions[key]) > 23:
                        description = transactions[key][:23]
                    else: 
                        description = transactions[key]
                whitespace = (" ")*(30 - len(description) - len(amount))
                items_ledger = description + whitespace + amount + "\n"
            output += items_ledger
        output += f"Total: {self.get_balance()}"
        return f"{output}"


def create_spend_chart(categories):
    names = []
    words = []
    spent_percentage = []
    for category in categories:
        names.append(category.name)
        for j in range(len(category.ledger)):
            items = category.ledger[j]
            amount = items["amount"]
            qtn = 0
            if amount < 0:
                qtn += amount
        words.append(float(qtn))
    total_words = sum(words)
    spent_percentage = []
    for i in words:
        qtn = int(i / total_words * 10)
        spent_percentage.append(qtn)

    chart = "Percentage spent by category\n"

    bars = []
    max_bar_length = 11
    for i in spent_percentage:
        bar = ""
        o = ""
        bar_space = ""
        for j in range(max_bar_length - i - 1):
            bar_space += " "
        for k in range(i + 1):
            o += "o"
        bar += bar_space + o
        bars.append(bar)

    qtn = []
    x = 100
    for i in range(max_bar_length):
        qtn2 = ""
        for j in bars:
            qtn2 += j[i] + "  "
        qtn.append(qtn2)

        if x == 100:
            chart += str(x) + "| " + qtn[i] + "\n"
        elif x > 0 and x < 100:
            chart += " " + str(x) + "| " + qtn[i] + "\n"
        elif x == 0:
            chart += "  " + str(x) + "| " + qtn[i] + "\n"
        x -= 10

    dashes = "-"
    for i in range(len(categories)):
        dashes += "---"
    chart += "    " + dashes + "\n"

    max_name_length = 0
    for i in names:
        if len(i) > max_name_length:
            max_name_length = len(i)
    for i in range(len(names)):
        if len(names[i]) < max_name_length:
            for j in range(max_name_length - len(names[i])):
                names[i] += " "
            names[i] = names[i]
    qtn = []
    for i in range(max_name_length):
        qtn2 = ""
        for j in names:
            qtn2 += j[i] + "  "
        qtn.append(qtn2)
        chart += "     " + qtn[i]
        if i != max(0, max_name_length - 1):
            chart += "\n"

    return chart

