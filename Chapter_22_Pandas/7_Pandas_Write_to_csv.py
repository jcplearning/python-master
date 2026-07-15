import pandas as pd

# Example for dataframe from csv file
df = pd.read_csv('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\OnlineSalesData.csv',\
                 header=1, index_col=0, usecols=[0, 1, 2, 3, 4, 5], nrows=10)
print(df)


# Read a csv file from a URL
url = 'https://cdn.wsform.com/wp-content/uploads/2018/09/country.csv'
df_url = pd.read_csv(url, header=1, index_col=1)
print(df_url)

df_url.to_csv('C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\Country_out.csv', 
          index=True, \
          header=True, \
            sep='|', \
            encoding='utf-8', \
           # line_terminator='\n', \
            quoting=1, \
            quotechar='"', \
            escapechar='\\', \
            doublequote=True, \
            date_format='%Y-%m-%d', \
            decimal='.', \
            float_format='%.2f', \
            chunksize=1000) 