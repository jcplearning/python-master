import csv

list_of_strings_for_csv = [
['1', 'John Doe', '25', '100000.00'],
['2', 'Jane Smith', '30', '120000.00'],
['3', 'Bob Johnson', '22', '90000.00'],
['4', 'Alice Williams', '28', '110000.00']
]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Age', 'Salary'])
    writer.writerows(list_of_strings_for_csv)
print("Data written to output.csv")

with open('output1.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    for row in list_of_strings_for_csv:
        writer.writerow(row)
print("Data written to output1.csv")
