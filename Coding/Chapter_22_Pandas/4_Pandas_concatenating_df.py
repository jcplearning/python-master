import pandas as pd

# concatenating dataframes for employee data
df1 = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                          '  ROSS    ', 'CHANDLER', ' JOEY    '], 
                          'Age': [30, 35, 37, 33, 34, 30]})

df2 = pd.DataFrame({'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                    'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY', 'IT', 'ARTIST']})

# Concatenate the two dataframes along the columns (axis=1)
result = pd.concat([df1, df2], axis=1)

print(result)

# concatenating dataframes for employee data with axis 0
df3 = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                          '  ROSS    ', 'CHANDLER', ' JOEY    '], 
                          'Age': [30, 35, 37, 33, 34, 30]}) 

df4 = pd.DataFrame({'Name': ['  JAMES   ', '  JOHN    ', '  JAMES   ',
                          '  JAMES   ', '  JOHN    ', '  JAMES   '],
                    'Age': [30, 35, 37, 33, 34, 30]})

# Concatenate the two dataframes along the rows (axis=0)
# do not display index values in the concatenated dataframe
result2 = pd.concat([df3, df4], axis=0, ignore_index=True)
print(result2)


# Merging dataframes for employee data using key 

df5 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'],
                            'Age': [30, 35, 37, 33, 34, 30]})

df6 = pd.DataFrame({'Name': ['MONICA', 'JOHN', 'JAMES',
                          'JAMES', 'JOHN', 'JOEY'],
                    'Salary': [100000, 93000, 88000, 120000, 94000, 95000]})

# Merge the two dataframes on the 'Name' column
result3 = pd.merge(df5, df6, on='Name', how='inner')
print(result3)


