import pandas as pd

# joining dataframes for employee data using key
df7 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'],
                            'Age': [30, 35, 37, 33, 34, 30]})

df8 = pd.DataFrame({'Name': ['MONICA', 'JOHN', 'JAMES',
                          'JAMES', 'JOHN', 'JOEY'],
                    'Salary': [100000, 93000, 88000, 120000, 94000, 95000]})

# Join the two dataframes on the 'Name' column
result4 = df7.set_index('Name').join(df8.set_index('Name'), how='inner')
print(result4)

result5 = df7.join(df8.set_index('Name'), how='outer')
print(result5)

# Merging dataframes for employee data using key with suffixes
df9 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'],  
                            'Age': [30, 35, 37, 33, 34, 30]})   

df10 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'], 
                    'Salary': [100000, 93000, 88000, 120000, 94000, 95000]})

# Merge the two dataframes on the 'Name' column with suffixes
result6 = pd.merge(df9, df10, on='Name') 
print(result6)
