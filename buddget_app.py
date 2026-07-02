class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description = ''):
        entry = {'amount': amount, 'description': description}
        self.ledger.append(entry)

    def withdraw(self, amount, description = ''):
        withdraw_amount = 0 - amount
        entry = {'amount': withdraw_amount, 'description': description}
        self.ledger.append(entry)
        if self.check_funds(amount):
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for i in range(len(self.ledger)):
            total += self.ledger[i]['amount']
        return total

    
    def transfer(self, amount, category):
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        if self.check_funds(amount):
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self): 
        output = self.name.center(30, "*") + "\n"
        for entry in self.ledger:
            desc = entry['description'][:23]
            amount = entry['amount']
            output += f"{desc:<23}{amount:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    chart = f'Percentage spent by category\n'
    spending_per_category = []
    total_spent = 0
    for category in categories:
        category_spending = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                category_spending += abs(entry['amount'])
        spending_per_category.append(float(f"{category_spending:.2f}"))
        total_spent += category_spending
        total_spent = float(f"{total_spent:.2f}")
    print(f"{category_spending:.2f}")
    print(spending_per_category)
    print(total_spent)

    percentages = []
    for spending in spending_per_category:
        if total_spent > 0:
            pct = (spending / total_spent) * 100
            rounded_pct = (int(pct) // 10) * 10
            percentages.append(rounded_pct)
        else:
            percentages.append(0)

    for row_val in range(100, -1, -10):
        row_str = f"{row_val:>3}|"
        pct_str = ' o '
        for pct in percentages:
            if pct >= row_val:
                row_str += pct_str
            else:
                row_str += '   '
        chart += row_str + " \n"

    # Generate the divider dashes line
    dash_count = 4 + (3 * len(categories)) + 1
    chart += "    " + ("-" * (dash_count - 4)) + "\n"

    # Find the maximum name length to establish our vertical boundary
    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        # Initial 4-space indentation alignment to clear the Y-axis column
        name_row = "    "
        
        for cat in categories:
            if i < len(cat.name):
                name_row += f" {cat.name[i]} "
            else:
                name_row += "   " # Spaces if the name already finished printing
                
        # Append the row with its trailing space constraint
        chart += name_row + " "
        
        # Avoid putting a trailing newline on the very last line of text
        if i < max_len - 1:
            chart += "\n"
            
    print(chart)
    return chart


food = Category('Food')
food.deposit(1000, 'initial deposit')
# food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
# food.get_balance()
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(50, 'suit')
# print(food)

create_spend_chart([food, clothing])
