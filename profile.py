import random
import profile_generator_functions as gf


class Profile:

    def __init__(self, is_female: bool = None, age_use_normal_dist:bool = True):
        #  Randomly generate name
        if is_female is None:
            is_female = random.choice([True, False])

        self.is_female = is_female
        self.full_name = gf.generate_random_name(self.is_female)
        self.first_name = self.full_name.split(" ")[0]
        self.last_name = self.full_name.split(" ")[1]

        #  Randomly assign address
        self.address, self.country, self.state, self.city = gf.generate_random_address()

        #  Randomly assign job
        self.job = gf.generate_random_job()

        self.age = gf.generate_random_age(age_use_normal_dist)