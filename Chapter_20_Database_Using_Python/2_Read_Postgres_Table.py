import psycopg2

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host="aws-1-us-east-2.pooler.supabase.com",
        port="5432",
        database="postgres",
        user="postgres.wqifpwiazpxcicwymwds",
        password="WorldFIFA2026"
    )
    print("Connection to the database was successful!")

    # Creating curson and executing a query to read data from a table
    cursor = connection.cursor()
    cursor.execute("select * from public.\"Product\"")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1])  # Assuming the first column is 'id' and the second column is 'name'
    cursor.close()

except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")


