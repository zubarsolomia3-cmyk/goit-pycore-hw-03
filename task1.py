from datetime import datetime

def get_days_from_today(date):
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - target_date
    return delta.days
except ValueError:
        return "Помилка: використовуйте формат YYYY-MM-DD"

print(get_days_from_today("2025-01-01"))








