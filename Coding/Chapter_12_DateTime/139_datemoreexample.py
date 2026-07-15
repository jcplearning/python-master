#Age calculator — given a birth date, compute exact age in years, months, and days.

import datetime
# Get the current date
current_date = datetime.date.today()
# Define a birth date
birth_date = datetime.date(1980, 5, 28)
# Calculate the age
age_years = current_date.year - birth_date.year
age_months = current_date.month - birth_date.month
age_days = current_date.day - birth_date.day
# Adjust for negative months and days
if age_months < 0:
    age_years -= 1
    age_months += 12
if age_days < 0:
    age_months -= 1
    age_days += (current_date - datetime.date(current_date.year, current_date.month, 1)).days
print(f"Age: {age_years} years, {age_months} months, and {age_days} days")


#Days until event — print how many days are left until New Year.
new_year = datetime.date(current_date.year + 1, 1, 1)
days_until_new_year = (new_year - current_date).days
print(f"Days until New Year: {days_until_new_year} days")

