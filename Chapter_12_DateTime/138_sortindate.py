import datetime 

# Create a list of datetime objects
dates = [
    datetime.datetime(2024, 6, 15, 14, 30),
    datetime.datetime(2023, 5, 10, 9, 0),
    datetime.datetime(2024, 1, 1, 0, 0),
    datetime.datetime(2023, 12, 25, 18, 45)
]


# Sort the list of datetime objects
sorted_dates = sorted(dates)
# Print the sorted list of datetime objects
print("Sorted dates:")
for date in sorted_dates:
    print(date,type(date))
    


