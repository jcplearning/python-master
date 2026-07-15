import csv

list_of_strings_for_csv = [
{'ID': 1, 'Name': 'John Doe', 'Age': 25, 'Salary': 100000.0},
{'ID': 2, 'Name': 'Jane Smith', 'Age': 30, 'Salary': 120000.0},
{'ID': 3, 'Name': 'Bob Johnson', 'Age': 22, 'Salary': 90000.0}, 
{'ID': 4, 'Name': 'Alice Williams', 'Age': 28, 'Salary': 110000.0}
]

with open('output_dict.csv', mode='w', newline='') as file:
    fieldnames = ['ID', 'Name', 'Age', 'Salary']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_of_strings_for_csv)
print("Data written to output_dict.csv")

