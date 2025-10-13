from datetime import datetime

def get_days_from_today(date):
    # Перетворюємо рядок у дату
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    # Отримуємо сьогоднішню дату
    today = datetime.today().date()
    # Рахуємо різницю в днях
    delta = today - target_date
    return delta.days
except ValueError:
        return "Помилка: використовуйте формат YYYY-MM-DD"

# Приклад перевірки
print(get_days_from_today("2025-01-01"))







