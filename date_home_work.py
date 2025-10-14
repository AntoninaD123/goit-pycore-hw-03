
#task 1//homework
from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime("1992-10-09", "%Y-%m-%d")
    today = datetime.today()
    difference = today-given_date
    print(difference.days)
get_days_from_today("1992-10-09")



#task 2//homework

import random
def get_numbers_ticket(min, max, quantity):
    if quantity < 1 or quantity > 49:
        return[]
    numbers = random.sample(range(1, 50), quantity)
    numbers.sort()
    return numbers
ticket = get_numbers_ticket(1, 49, 6)
print(ticket)



#task 3//homework

import re

def normalize_phone(phone_number):
    phone = re.sub(r"[^\d+]", "", phone_number)

    if phone.startswith("+380"):
        return phone

    elif phone.startswith("380"):
        return "+" + phone

    else:
        return "+38" + phone


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS distribution:", sanitized_numbers)


#task 4//homework
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "Tonia D", "birthday": "1992.10.09"},
    {"name": "Tania D", "birthday": "1998.01.28"},
    {"name": "Nastia P", "birthday": "2004.11.01"},
    {"name": "Polina P", "birthday": "2015.06.26"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of congratulations for this week:", upcoming_birthdays)


