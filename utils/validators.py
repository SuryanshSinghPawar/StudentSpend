from datetime import datetime


CATEGORIES = {"Food", "Travel", "Education", "Entertainment", "Shopping", "Other"}


def valid_amount(value):
    try:
        return float(value) > 0
    except (TypeError, ValueError):
        return False


def valid_category(value):
    return value.title() in CATEGORIES


def valid_date(value):
    if not value:
        return True
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False
