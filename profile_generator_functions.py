# https://faker.readthedocs.io/en/master/providers.html
import faker

fake_generator = faker.Faker()


def generate_random_name(is_female):
    if is_female:
        return fake_generator.name_female()

    return fake_generator.name_male()


def generate_random_address():
    while(True):
        try:
            address = fake_generator.address()
            country = fake_generator.current_country()
            city = address.split("\n")[1].split(",")[0]
            state = address.split("\n")[1].split(",")[1].strip().split(" ")[0]
            return address, country, state, city
        except Exception as e:
            pass

def generate_random_job():
    return fake_generator.job()