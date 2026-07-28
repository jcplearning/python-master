import pandas as pd
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client["salesdb"]
collection = db["user"]

# Read records from MongoDB
records = list(collection.find())
df = pd.DataFrame(records)
df.to_csv('outbound/fake_data.csv', index=False)

