from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Поточна системна дата
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо день народження з рядка у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження цього року вже минув — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця в днях до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Якщо день народження у межах 7 днів
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Якщо припадає на вихідний — переносимо на понеділок
            if congratulation_date.weekday() >= 5:
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            # Додаємо у список привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад перевірки
users = [
    {"name": "John Doe", "birthday": "1985.10.19"},  # завтра
    {"name": "Jane Smith", "birthday": "1990.10.22"},  # через 4 дні
    {"name": "Anna Taylor", "birthday": "1995.10.30"}  # далі ніж через 7 днів
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
