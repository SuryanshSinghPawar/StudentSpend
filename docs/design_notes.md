# Design Notes

## Functional modules
1. Expense Management
2. Monthly Budget Management
3. Analytics and Reporting
4. Persistent JSON Storage

## Non-functional requirements
- Performance: normal CLI operations should complete immediately for typical student-sized datasets.
- Security: data is stored locally; user input is validated before processing.
- Usability: numbered menu and clear messages.
- Reliability: JSON persistence keeps data between program runs and file-read errors are handled.
- Maintainability: logic is separated into modules.
- Error handling: invalid amounts, categories and dates are rejected.

## Design decisions
JSON was selected because it is simple, readable, requires no external dependency and is suitable for a beginner Python project.
