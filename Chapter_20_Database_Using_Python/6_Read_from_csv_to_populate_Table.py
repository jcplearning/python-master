import psycopg2

# Read data from csv file and convert it into list of tuples
with open("C:\\Jagan\\1. DAI Project\\01. TM1 Development\\InProgress Enhancements\\AI Operations Testing\\Sample datasources\\archive_Sales\\cities.csv") as fp:
    data = fp.read().splitlines()

# list of strings
print(type(data))

# convert list of string into list of tuples
mylist = []
for row in data[1:]:
    record = row.split(',')
    mylist.append((int(record[0]), record[1], record[2], int(record[3])))

# Connect to the PostgreSQL database and insert data into the table
try:
    Connection = psycopg2.connect(dbname="postgres",
    user="postgres.wqifpwiazpxcicwymwds",
    password="WorldFIFA2026",
    host="aws-1-us-east-2.pooler.supabase.com",
    port="5432"
    )

    Cursor = Connection.cursor()
    Cursor.execute("Drop table if exists public.city")
    Cursor.execute("create table public.city ( CityID bigint, CityName text, Zip text, CountryID bigint)")
    query = "Insert into public.city values (%s,%s,%s,%s)"
    Cursor.executemany(query, mylist)
    Connection.commit()

    Cursor.execute("Select * from public.city")
    data = Cursor.fetchall()
    for row in data:
        print(row[0],row[1],row[2],row[3])

    Cursor.close()

except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")
finally:
     Connection.close()
     print("Database connection closed.")
