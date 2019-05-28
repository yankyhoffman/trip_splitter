class Expense:
    def __init__(self, name):
        self.name = name
        self._splitters = {}

    def add_splitter(self, splitter):
        self._splitters[splitter] = 0
        splitter.add_expense(self)

    def pay(self, splitter, amount):
        self._splitters[splitter] += amount
