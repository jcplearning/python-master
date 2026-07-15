import pandas as pd 

# sorting dataframes for employee data using key
df11 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'],  
                            'Age': [30, 35, 37, 33, 34, 30]})

df12 = pd.DataFrame({'Name': ['RACHEL', 'MONICA', 'PHOEBE',
                          'ROSS', 'CHANDLER', 'JOEY'],
                    'Salary': [100000, 93000, 88000, 120000, 94000, 95000]})

# Merge the two dataframes on the 'Name' column
result7 = pd.merge(df11, df12, on='Name')
# Sort the merged dataframe by 'Age' in ascending order
result7_sorted = result7.sort_values(by='Age', ascending=True)
print(result7_sorted)

# Sort the merged dataframe by 'Salary' in descending order
result7_sorted_desc = result7.sort_values(by='Salary', ascending=False)
print(result7_sorted_desc)

