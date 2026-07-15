import pandas as pd
import openpyxl

df = pd.read_excel('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\students.xlsx')
#print(df)

sheet1 = pd.read_excel('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\students.xlsx', 
                        sheet_name = 0, 
                        index_col = 0)

sheet2 = pd.read_excel('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\students.xlsx', 
                        sheet_name = 1, 
                        index_col = 0)

newData = pd.concat([sheet1, sheet2])
print(newData)

sorted_column = newData.sort_values(['English'], ascending = False)
print(sorted_column)

sorted_column.to_excel('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\sorted_students.xlsx', index = False)

#Grouping the data based on Roll No. and calculating the sum of marks for each student
print(newData.groupby('Roll No.').sum())

# Pivot Table Example
sales = pd.DataFrame({
    "category": ["A", "A", "B", "B"],
    "region": ["East", "West", "East", "West"],
    "sales": [100, 150, 200, 250]
})

pivot = sales.pivot_table(values="sales", index="category", columns="region", aggfunc="mean", fill_value=0)
print(pivot)


