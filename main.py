from modules.expense_manager import ExpenseManager
from modules.budget_manager import BudgetManager
from modules.analytics import Analytics
from modules.storage import Storage
from utils.validators import valid_amount, valid_category, valid_date
from utils.helpers import pause, print_header


def add_expense(manager):
    print_header("ADD EXPENSE")
    title = input("Expense title: ").strip()
    amount_text = input("Amount (₹): ").strip()
    category = input("Category (Food/Travel/Education/Entertainment/Shopping/Other): ").strip()
    date = input("Date (YYYY-MM-DD, blank=today): ").strip()

    if not title or not valid_amount(amount_text) or not valid_category(category) or not valid_date(date):
        print("Invalid input. Please check the values and try again.")
        return

    manager.add_expense(title, float(amount_text), category.title(), date)
    print("Expense added successfully.")


def list_expenses(manager):
    print_header("ALL EXPENSES")
    expenses = manager.list_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"{'ID':<5}{'Title':<22}{'Amount':>12}  {'Category':<16}{'Date'}")
    print("-" * 70)
    for e in expenses:
        print(f"{e['id']:<5}{e['title'][:20]:<22}{e['amount']:>10.2f}  {e['category']:<16}{e['date']}")


def set_budget(budget_manager):
    print_header("SET MONTHLY BUDGET")
    month = input("Month (YYYY-MM): ").strip()
    amount = input("Budget amount (₹): ").strip()
    if len(month) != 7 or not valid_amount(amount):
        print("Invalid month or amount.")
        return
    budget_manager.set_budget(month, float(amount))
    print("Budget saved.")


def show_summary(manager, budget_manager):
    print_header("MONTHLY SUMMARY")
    month = input("Month (YYYY-MM): ").strip()
    analytics = Analytics(manager)
    summary = analytics.monthly_summary(month)
    budget = budget_manager.get_budget(month)
    print(f"Month: {month}")
    print(f"Total spent: ₹{summary['total']:.2f}")
    print(f"Number of expenses: {summary['count']}")
    print(f"Highest category: {summary['highest_category'] or 'N/A'}")
    if budget is not None:
        remaining = budget - summary["total"]
        print(f"Budget: ₹{budget:.2f}")
        print(f"Remaining: ₹{remaining:.2f}")
        if remaining < 0:
            print("WARNING: Budget exceeded.")
        elif budget and summary["total"] / budget >= 0.8:
            print("WARNING: More than 80% of the budget has been used.")
    else:
        print("No budget set for this month.")


def main():
    storage = Storage()
    manager = ExpenseManager(storage)
    budget_manager = BudgetManager(storage)

    while True:
        print_header("STUDENTSPEND - EXPENSE & BUDGET TRACKER")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Set monthly budget")
        print("4. View monthly summary")
        print("5. Category report")
        print("6. Delete expense")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(manager)
        elif choice == "2":
            list_expenses(manager)
        elif choice == "3":
            set_budget(budget_manager)
        elif choice == "4":
            show_summary(manager, budget_manager)
        elif choice == "5":
            month = input("Month (YYYY-MM): ").strip()
            report = Analytics(manager).category_report(month)
            print_header(f"CATEGORY REPORT - {month}")
            if not report:
                print("No expenses for this month.")
            else:
                for category, amount in report.items():
                    print(f"{category:<18} ₹{amount:.2f}")
        elif choice == "6":
            expense_id = input("Expense ID to delete: ").strip()
            if manager.delete_expense(expense_id):
                print("Expense deleted.")
            else:
                print("Expense ID not found.")
        elif choice == "7":
            print("Thanks for using StudentSpend!")
            break
        else:
            print("Invalid option.")
        pause()


if __name__ == "__main__":
    main()
