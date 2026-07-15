import pandas as pd

df = pd.read_json('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\data.json')
print(df)


df = pd.DataFrame(
    [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 22}
] )

print(df.to_json(orient='split')) 
print(df.to_json(orient='index'))

