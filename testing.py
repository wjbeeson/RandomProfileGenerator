from profile import Profile

def print_profile(profile: Profile):
    print(f"Name: {profile.full_name} | Age: {profile.age} | City: {profile.city} | Job: {profile.job} | IsFemale: {profile.is_female}")


print("Random Everything: ")
for i in range(10):
    print_profile(Profile())
print()

print("Random Females: ")
for i in range(10):
    print_profile(Profile(is_female=True))

print()
