import datetime

current_date = datetime.date.today()
print("Current date:", current_date)

# Create a timedelta object representing a duration of 10 days
time_delta = datetime.date.today() + datetime.timedelta(days=10)
print("Time delta of 10 days:", time_delta)

# Create a timedelta object representing a duration of 1 year
time_delta = datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30)
print("Time delta:", time_delta)


start_date = datetime.date(1978,1,11)
end_date = datetime.date.today()
date_difference = end_date - start_date
print("Difference between", end_date, "and", start_date, "is", date_difference.days,  "days")
