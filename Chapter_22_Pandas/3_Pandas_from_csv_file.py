import pandas as pd

# Example for dataframe from csv file
df = pd.read_csv('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\OnlineSalesData.csv')
##print(type(df))
#print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns')
##print(df.columns)
#rint(df.values)
#print(df)

#print(df.query('`Product_Category` == "Clothing" and `Total_Revenue` > 100'))

print(df[df['Total_Revenue'] > 1000])

# Indexing and selecting data using loc
print(df.loc[0:3, ['Product_Category', 'Product_Name', 'Total_Revenue']])

# Head and tail of the dataframe
print(df.head(5))
print(df.tail(5))

#at of the dataframe
print(df.at[0, 'Product_Name'])

#Querying the dataframe using query method
print(df.query('`Product_Category` == "Clothing" and `Total_Revenue` > 100'))

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# filter dataframe 
print(dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")])
