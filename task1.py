from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо рядок у дату
        target_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Отримуємо сьогоднішню дату
        today = datetime.today().date()

        # Розраховуємо різницю в днях
        delta = today - target_date

        # Повертаємо кількість днів
        return delta.days

    except ValueError:
        # Якщо формат неправильний
        print("Помилка: використовуйте формат YYYY-MM-DD")
        return None


# Перевірка
print(get_days_from_today("2025-01-01"))
