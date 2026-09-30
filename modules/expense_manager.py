from datetime import date
from uuid import uuid4


class ExpenseManager:
    def __init__(self, storage):
        self.storage = storage

    def list_expenses(self):
        return self.storage.load_expenses()

    def add_expense(self, title, amount, category, expense_date=""):
        expenses = self.storage.load_expenses()
        if not expense_date:
            expense_date = date.today().isoformat()
        expense = {
            "id": str(uuid4())[:8],
            "title": title,
            "amount": round(float(amount), 2),
            "category": category,
            "date": expense_date,
        }
        expenses.append(expense)
        self.storage.save_expenses(expenses)
        return expense

    def delete_expense(self, expense_id):
        expenses = self.storage.load_expenses()
        filtered = [e for e in expenses if e["id"] != expense_id]
        if len(filtered) == len(expenses):
            return False
        self.storage.save_expenses(filtered)
        return True
