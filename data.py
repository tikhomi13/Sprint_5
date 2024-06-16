# Здесь находится метод get_sign_up_data(), генерирующий данные для автотестов. Эл. почту, имена, пароли

import faker


def get_sign_up_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()

    return name, email, password
