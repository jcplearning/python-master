import csv

list_of_strings_for_csv = [
    "1,John Doe,25,100000.00",
    "2,Jane Smith,30,120000.00",
    "3,Bob Johnson,22,90000.00",
    "4,Alice Williams,28,110000.00"
]

csv_reader = csv.reader(list_of_strings_for_csv, delimiter=',')

total_salary = 0
for row in csv_reader:
    print(row)
    total_salary += float(row[3])

print(f"Total Salary: {total_salary:.2f}")






