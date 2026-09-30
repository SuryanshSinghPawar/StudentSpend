class BudgetManager:
    def __init__(self, storage):
        self.storage = storage

    def set_budget(self, month, amount):
        budgets = self.storage.load_budgets()
        budgets[month] = round(float(amount), 2)
        self.storage.save_budgets(budgets)

    def get_budget(self, month):
        return self.storage.load_budgets().get(month)
