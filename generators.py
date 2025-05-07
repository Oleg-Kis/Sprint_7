from faker import Faker

fake = Faker()

def generate_order_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=5),
        "phone": fake.phone(),
        "rentTime": fake.random_int(min=1, max=5),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.word(),
        "color": [
        ]
    }

def generate_create_courier_body():
    return {
        "login": fake.word(),
        "password": fake.word(),
        "firstName": fake.word()
    }
