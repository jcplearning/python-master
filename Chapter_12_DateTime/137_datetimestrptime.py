import datetime

datestring = "2024-06-15 14:30:00"
# Convert the string to a datetime object

dt_object = datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
print("Datetime object:", dt_object)
# Extracting components
print("Year:", dt_object.year)
print("Month:", dt_object.month)
print("Day:", dt_object.day)
print("Hour:", dt_object.hour)
print("Minute:", dt_object.minute)
print("Second:", dt_object.second)

