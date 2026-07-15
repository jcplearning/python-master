import random
#generate a CSV file of 1,000 fake users for testing.
import csv
def generate_fake_users(num_users=1000):
    fake_users = []
    for i in range(num_users):
        user_id = i + 1
        name = f"User{user_id}"
        email = f"user{user_id}@example.com"
        fake_users.append([user_id, name, email])
    return fake_users

def save_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UserID', 'Name', 'Email'])
        writer.writerows(data)
if __name__ == "__main__":
    fake_users = generate_fake_users()
    save_to_csv('fake_users.csv', fake_users)
    print("Fake users saved to fake_users.csv")

    