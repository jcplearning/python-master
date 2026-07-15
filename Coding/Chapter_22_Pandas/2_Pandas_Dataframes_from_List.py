import pandas as pd

# Example for dataframe from list of tuples 

mylist = [ (100, 'John Smith', 10000.00), (101, 'Ricky Robinson', 90000.00), (102, 'Mary Anderson', 98000.00) ]

df = pd.DataFrame(mylist, columns=['ID','Name','Annual Salary'])

print(type(df))
print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns')
print(df.columns)
print(df.values)

## Example for dataframe from list of dictionaries

mydict = [ { 'ID':100, 'Name': 'David Morgan', 'Annual Salary': 100000 },
           { 'ID':101, 'Name': 'Jane Finch', 'Annual Salary': 90000 },
           { 'ID':102, 'Name': 'Amelia Kerr', 'Annual Salary': 99000 }]

df = pd.DataFrame(mydict)

print(type(df))
print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns')
print(df.columns)
print(df.values)
print(df)
print(df.describe())