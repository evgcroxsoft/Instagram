import random

from randominfo import get_phone_number, random_password


class RandomCredentials:
    def email(self):
        fake_names = [
            "zhenya",
            "olya",
            "katya",
            "masha",
            "platon",
            "fedor",
            "alex",
            "john",
        ]
        fake_email = [
            "@gmail.com",
            "@yandex.ru",
            "@meta.ua",
            "@yahoo.com",
            "@example.com",
        ]
        name = random.randint(0, len(fake_names) - 1)
        domen = random.randint(0, len(fake_email) - 1)
        return fake_names[name] + fake_email[domen]

    def password(self):
        return random_password(length=8, special_chars=True, digits=True)

    def phone(self):
        return get_phone_number(country_code=True)


fake = RandomCredentials()
fake_email = fake.email()
fake_phone = fake.phone()
fake_password = fake.password()
