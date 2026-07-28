import pandas as pd
import random
import matplotlib.pyplot as plt

Sales = []

for i in range(202501, 202513):
    Sales.append((i,random.randint(1000, 5000)))

sales_df = pd.DataFrame(Sales, columns=['Month', 'Sales'])

print(sales_df)

sales_df.plot(x='Month', y='Sales', kind='bar', title='Monthly Sales Data', legend=False)

#sales_df.plot(x='Month', y='Sales', kind='line', title='Monthly Sales Data', legend=False)

#sales_df.plot(x='Month', y='Sales', kind='pie', title='Monthly Sales Data', legend=False, autopct='%1.1f%%', startangle=90, figsize=(8, 8))

plt.show()



