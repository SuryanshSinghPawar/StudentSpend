from collections import defaultdict


class Analytics:
    def __init__(self, expense_manager):
        self.expense_manager = expense_manager

    def monthly_expenses(self, month):
        return [e for e in self.expense_manager.list_expenses() if e["date"].startswith(month)]

    def monthly_summary(self, month):
        expenses = self.monthly_expenses(month)
        total = sum(e["amount"] for e in expenses)
        categories = self.category_report(month)
        highest = max(categories, key=categories.get) if categories else ""
        return {"total": total, "count": len(expenses), "highest_category": highest}

    def category_report(self, month):
        totals = defaultdict(float)
        for expense in self.monthly_expenses(month):
            totals[expense["category"]] += expense["amount"]
        return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))
