# 1. Given a list of temperatures, return a list of days where the temperature was above average.

weather = [ ('4/21/2025',54), ('4/22/2025', 60), 
('4/23/2025', 65), ('4/24/2025', 70), ('4/25/2025', 68) 
]

# Get the average temperature

total_temp = 0
for date, temp in weather:
    total_temp += temp
average_temp = total_temp/ len(weather) 

print(f"Average temperature: {average_temp}")

for date, temp in weather:
    if temp > average_temp:
        print(f"{date} had a temperature of {temp}, which is above average.")


# 2. Given a list of prices, compute the running total.

lst = [10, 20, 30, 40, 50]

running_total = 0
for price in lst:
    running_total += price
    print(f"Running total: {running_total}")

# 3. Given a list of names, return the one that appears most frequently.

names = ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Alice']
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

most_frequent_name = max(name_counts, key=name_counts.get)
print(f"The most frequent name is {most_frequent_name} with {name_counts[most_frequent_name]} occurrences.")

