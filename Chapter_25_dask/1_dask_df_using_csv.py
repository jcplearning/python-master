from dask import dataframe as dd

# Read CSV file into a Dask DataFrame
df = dd.read_csv('C:\\Jagan\\temp\\Product.csv')

# Display the first few rows of the DataFrame
print(df.head())

print(df.compute().shape)  # Compute the shape of the DataFrame

print(df.query('product_id > 100').compute())  # Query the DataFrame and compute the result

print(df.sort_values('product_id', ascending=False).compute())  # Sort the DataFrame by 'product_id' and compute the result



