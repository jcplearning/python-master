from faker import Faker
from datetime import datetime
import pymongo
import pandas as pd

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
        record = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'date_of_birth': datetime.combine(dob, datetime.min.time()),  # Fix: convert date → datetime
            'company': fake.company(),
            'job_title': fake.job(),
            'credit_card_number': fake.credit_card_number(),
            'credit_card_expiry': fake.credit_card_expire(),
            'credit_card_provider': fake.credit_card_provider(),
        }
        data.append(record)
    return data

if __name__ == "__main__":
    num_records = 100

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["salesdb"]
    collection = db["user"]

    fake_data = generate_fake_data(num_records)

    # Print the generated fake data
    for record in fake_data:
        print(record)

    # Insert the generated fake data into the collection
    collection.insert_many(fake_data)
    print(f"\n✅ {num_records} records inserted into MongoDB successfully.")





    

