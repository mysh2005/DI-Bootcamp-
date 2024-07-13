from faker import Faker

fake = Faker()

users = []

def add_user():
    user = {
        "name": fake.name(),
        "address": fake.address().replace('\n', ' '), 
        "language_code": fake.language_code()
    }
    users.append(user)

add_user()

for user in users:
    print(user)
