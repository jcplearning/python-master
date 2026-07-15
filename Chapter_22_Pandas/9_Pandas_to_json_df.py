import pandas as pd

df = pd.DataFrame(data=[
    ['15135', 'Alex', '25/4/2014'],
    ['23515', 'Bob', '26/8/2018'],
    ['31313', 'Martha', '18/1/2019'],
    ['55665', 'Alen', '5/5/2020'],
    ['63513', 'Maria', '9/12/2020']],
    columns=['ID', 'NAME', 'DATE OF JOINING'])

df.to_json('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\file.json', orient='split', compression='infer')

df = pd.read_json('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\file.json', orient='split', compression='infer')
print(df)

df.to_json('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\file1.json', orient='records', compression='infer')
