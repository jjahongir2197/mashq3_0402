class Budget:
    def __init__(self):
        self.income = []
        self.expense = []

    def add_income(self, amount):
        self.income.append(amount)

    def add_expense(self, amount):
        self.expense.append(amount)

    def balance(self):
        return sum(self.income) - sum(self.expense)

    def report(self):
        print("Daromad:", sum(self.income))
        print("Xarajat:", sum(self.expense))
        print("Qoldiq:", self.balance())


b = Budget()
b.add_income(5000000)
b.add_expense(1200000)
b.add_expense(800000)
b.report()
