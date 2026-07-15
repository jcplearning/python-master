import datetime

# Get the current date and time
current_datetime = datetime.date.today()
print("Current date:", current_datetime)

# get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# get only the time
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

datestring = datetime.datetime.now().date()
print("Current date:", datestring)


print("Current year:", datetime.datetime.now().year)
print("Current month:", datetime.datetime.now().month)
print("Current day:", datetime.datetime.now().day)

print("Current hour:", datetime.datetime.now().hour)
print("Current minute:", datetime.datetime.now().minute)
print("Current second:", datetime.datetime.now().second)

print("Current microsecond:", datetime.datetime.now().microsecond)
print("Current microsecond:", datetime.datetime.now().weekday())

