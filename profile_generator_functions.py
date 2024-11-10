# https://faker.readthedocs.io/en/master/providers.html
import faker
import random
import numpy as np
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

def generate_random_age(use_normal_dist = False):
    if not use_normal_dist:
        return random.randint(18, 75)

    # Parameters for the normal distribution
    mean_age = 30  # Peak at 30
    std_dev_age = 10  # Standard deviation of 10
    min_age = 15
    max_age = 75

    # Function to generate a random age within the specified range
    def generate_random_age_normal_dist():
        age = None
        while age is None or age < min_age or age > max_age:
            age = int(np.round(np.random.normal(mean_age, std_dev_age)))
        return age

    # Generate a random age
    return generate_random_age_normal_dist()
()