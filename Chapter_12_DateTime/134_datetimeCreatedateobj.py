import datetime

#create a date object
date_object = datetime.date(2026, 12, 25)
time_object = datetime.time(14, 30, 45)
date_time_object = datetime.datetime(2025, 12, 12, 14, 30, 45)

print("Date object:", date_object)
print("Time object:", time_object)
print("Date and Time object:", date_time_object)

print("weekday:", date_time_object.weekday())

#create a date object using the current date
current_year = datetime.date.today().year
current_month= datetime.date.today().month
currentday = 1 
current_date_object = datetime.date(current_year, current_month, currentday)
print("Current date object:", current_date_object)
print("weekday:", current_date_object.weekday())

