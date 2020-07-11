class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            # transfer out
            withdraw_description = "Transfer to " + category.category
            self.withdraw(amount, withdraw_description)
            # transfer into
            deposit_description = "Transfer from " + self.category
            category.deposit(amount, deposit_description)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount <= balance:
            return True
        else:
            return False

    def __str__(self):
        output = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output


def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total -= item["amount"]
        spent.append(round(total, 2))
        category_names.append(category.category)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"

    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    longest_name_length = 0

    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)

    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return graph
