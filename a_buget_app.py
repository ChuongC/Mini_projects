class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = self.name.center(30,'*') + '\n'
        lines = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            lines += f'{desc:<23}{amt:>7}\n'
        total = f'Total: {self.get_balance():.2f}' 
        return title + lines + total

    def deposit(self, amount, description= ''):
        #add a transaction
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, another_budget):         
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another_budget.name}")
            another_budget.deposit(amount, f"Transfer from {self.name}")
            return True
        return False 

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    # 1) spending per category (positive numbers)
    spent = []
    for c in categories:
        s = 0
        for item in c.ledger:
            if item["amount"] < 0:
                s += -item["amount"]
        spent.append(s)

    total = sum(spent)
    if total == 0:
        percentages = [0] * len(spent)
    else:
        percentages = [int((s / total) * 100) for s in spent]
        percentages = [p - (p % 10) for p in percentages]  # floor to nearest 10

    # 2) header
    chart = "Percentage spent by category\n"

    # 3) percentage rows (100 down to 0)
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        for p in percentages:
            row += "o  " if p >= level else "   "
        chart += row + "\n"

    # 4) separator line (4 spaces then dashes)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5) names vertically, starting with 5 spaces; no newline at the very end
    names = [c.name for c in categories]
    max_len = max(len(n) for n in names)
    for i in range(max_len):
        row = "     "
        for n in names:
            row += (n[i] if i < len(n) else " ") + "  "
        chart += row if i == max_len - 1 else row + "\n"

    return chart




food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

            #output
#*************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96