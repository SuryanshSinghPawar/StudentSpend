import tempfile
import unittest
from pathlib import Path

from modules.storage import Storage
from modules.expense_manager import ExpenseManager
from modules.budget_manager import BudgetManager
from modules.analytics import Analytics


class TestStudentSpend(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage = Storage()
        self.storage.data_dir = Path(self.temp_dir.name)
        self.storage.expense_file = self.storage.data_dir / "expenses.json"
        self.storage.budget_file = self.storage.data_dir / "budgets.json"
        self.storage._ensure_file(self.storage.expense_file, [])
        self.storage._ensure_file(self.storage.budget_file, {})
        self.expenses = ExpenseManager(self.storage)
        self.budgets = BudgetManager(self.storage)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_list(self):
        self.expenses.add_expense("Lunch", 120, "Food", "2026-09-29")
        self.assertEqual(len(self.expenses.list_expenses()), 1)

    def test_budget(self):
        self.budgets.set_budget("2026-09", 5000)
        self.assertEqual(self.budgets.get_budget("2026-09"), 5000.0)

    def test_analytics(self):
        self.expenses.add_expense("Lunch", 120, "Food", "2026-09-29")
        self.expenses.add_expense("Bus", 80, "Travel", "2026-09-29")
        summary = Analytics(self.expenses).monthly_summary("2026-09")
        self.assertEqual(summary["total"], 200)
        self.assertEqual(summary["count"], 2)


if __name__ == "__main__":
    unittest.main()
