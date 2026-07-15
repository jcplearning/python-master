import datetime

# Create a date object
current_dtime = datetime.datetime.now()
print("Current date and time:", current_dtime)

print("Formatted date and time:", current_dtime.strftime("%m/%d/%Y %H:%M:%S"))
print("Formatted date and time:", current_dtime.strftime("%B %d, %Y %I:%M:%S %p"))

print("Day of the week:",current_dtime.strftime("%A"))
print("Day of the week:",current_dtime.strftime("%a"))
