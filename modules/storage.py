import json
from pathlib import Path


class Storage:
    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.expense_file = self.data_dir / "expenses.json"
        self.budget_file = self.data_dir / "budgets.json"
        self._ensure_file(self.expense_file, [])
        self._ensure_file(self.budget_file, {})

    def _ensure_file(self, path, default):
        if not path.exists():
            path.write_text(json.dumps(default, indent=2), encoding="utf-8")

    def load_expenses(self):
        try:
            return json.loads(self.expense_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def save_expenses(self, expenses):
        self.expense_file.write_text(json.dumps(expenses, indent=2), encoding="utf-8")

    def load_budgets(self):
        try:
            return json.loads(self.budget_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}

    def save_budgets(self, budgets):
        self.budget_file.write_text(json.dumps(budgets, indent=2), encoding="utf-8")
