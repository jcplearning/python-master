import psycopg2

# Connect to the PostgreSQL database
try:
    Connection = psycopg2.connect(dbname="postgres",
    user="postgres.wqifpwiazpxcicwymwds",
    password="WorldFIFA2026",
    host="aws-1-us-east-2.pooler.supabase.com",
    port="5432"
    )

    Cursor = Connection.cursor()
    query = "Delete from public.Category where CategoryID = %s"
    Cursor.execute(query,(10,))
    Connection.commit()

    Cursor.execute("Select * from public.Category")
    data = Cursor.fetchall()
    for row in data:
        print(row[0],row[1])

    Cursor.close()

except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")
finally:
     Connection.close()
     print("Database connection closed.")