# StudentSpend - Smart Student Expense & Budget Tracker

## Overview
StudentSpend is a Python command-line application designed to help students record expenses, manage monthly budgets, and view simple spending analytics.

## Features
- Add and view expenses
- Delete expenses
- Categorize expenses
- Set monthly budgets
- View monthly spending summaries
- Generate category-wise reports
- Persistent JSON data storage
- Input validation
- Unit tests

## Technologies
- Python 3
- JSON
- Git/GitHub
- Python unittest

## Project Structure
```text
student_spend/
├── main.py
├── modules/
│   ├── expense_manager.py
│   ├── budget_manager.py
│   ├── analytics.py
│   └── storage.py
├── utils/
│   ├── validators.py
│   └── helpers.py
├── data/
├── tests/
│   └── test_app.py
└── docs/
```

## How to Run
1. Install Python 3.
2. Clone/download the repository.
3. Open a terminal in the `student_spend` folder.
4. Run:
```bash
python main.py
```

## Testing
Run:
```bash
python -m unittest discover tests
```

## Input Rules
- Amount must be a positive number.
- Category must be one of: Food, Travel, Education, Entertainment, Shopping, Other.
- Dates use `YYYY-MM-DD`.
- Data is stored locally in JSON files.

## Academic Note
This project demonstrates programming fundamentals including variables, input/output, conditions, loops, functions, modular code, file handling, validation, data structures, and basic testing.
