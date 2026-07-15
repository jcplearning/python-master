import psycopg2

# Connect to the PostgreSQL database
try:
    Connection = psycopg2.connect(dbname="postgres",
    user="postgres.wqifpwiazpxcicwymwds",
    password="WorldFIFA2026",
    host="aws-1-us-east-2.pooler.supabase.com",
    port="5432"
    )

    # Create a cursor and execute SQL commands to create a table and insert data
    Cursor = Connection.cursor()

    # Drop the table if it already exists and create a new one
    Cursor.execute("Drop table if exists public.Category")

    # Create the Category table and insert data into it
    Cursor.execute("create table public.Category ( CategoryID int, CategoryName text)")
    Cursor.execute("Insert into public.Category values (1,\'Confections\')")
    query = "Insert into public.Category values (%s,%s)"
    Cursor.execute(query,(2,'Shell fish'))
    Cursor.execute(query,(3,'Cereals'))
    Cursor.execute(query,(4,'Dairy'))

    # Insert multiple records using executemany
    Cursor.executemany(query,[(5,'Beverages'),(6,'Seafood'),(7,'Meat'),(8,'Grain'),(9,'Poultry'),(10,'Snails')])

    # Insert more records
    mylist = [(11,'Vegetables'),(12,'Fruits')]
    Cursor.executemany(query,mylist)
    
    #Commit the transaction and fetch the data to verify the insertions
    Connection.commit()

    # Fetch and print the data from the Category table
    Cursor.execute("Select * from public.Category")
    data = Cursor.fetchall()
    for row in data:
        print(row[0],row[1])

    # Close the cursor and connection
    Cursor.close()

# Close the connection
except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")
finally:
     Connection.close()
     print("Database connection closed.")

