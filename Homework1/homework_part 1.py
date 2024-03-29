from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=today.year).date()
        if birthday_this_year < today:
            continue  

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            weekday = birthday_this_year.weekday()

            if weekday == 5 or weekday == 6:
                celebrate_day = "Monday"
            else:
                celebrate_day = birthday_this_year.strftime('%A')
            
            birthdays_per_week[celebrate_day].append(name)

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        if day in birthdays_per_week:
            names = ', '.join(birthdays_per_week[day])
            print(f"{day}: {names}")

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 2, 24)}, 
    {"name": "Jill Valentine", "birthday": datetime(1974, 2, 20)},  
    {"name": "Kim Kardashian", "birthday": datetime(1980, 2, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 3, 3)} 
]

get_birthdays_per_week(users)




