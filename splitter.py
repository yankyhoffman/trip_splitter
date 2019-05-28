class Splitter:
    def __init__(self, name):
        self.name = name
        self._expenses = []

    def add_expense(self, expense):
        self._expenses.append(expense)
        expense.add_splitter(self)
