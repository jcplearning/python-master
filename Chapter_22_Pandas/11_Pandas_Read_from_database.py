import pandas as pd
from sqlalchemy import create_engine

username = "postgres"
password = "PalaniAmrudham-123"
host = "localhost"
port = "5432"
database = "postgres"

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

df = pd.read_sql('Select * from  public."Department"', engine)

print(df.head())
print(df.shape)

