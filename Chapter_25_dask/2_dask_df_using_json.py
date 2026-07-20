from dask import dataframe as dd

# Read CSV file into a Dask DataFrame
df = dd.read_json('C:\\Jagan\\3. DAI-Learning\\PythonSamples\\inbound\\user.json', lines=True)

# Display the first few rows of the DataFrame
print(df.compute())

df.to_csv('C:\\Jagan\\3. DAI-Learning\\PythonSamples\\outbound\\user_output.csv', index=False, single_file=True)  # Save the DataFrame to a CSV file