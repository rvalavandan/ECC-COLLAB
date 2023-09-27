import random
import string


def generate_string():
    random_num = str(random.randint(1000, 9999))
    random_alpha_num = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    random_alpha = ''.join(random.choices(string.ascii_lowercase,k=3))
    random_single_digit = str(random.randint(0, 9))

    return f"{random_alpha}-{random_num}-cc000000{random_num}-{random_alpha_num}_{random_single_digit}"


# Generate 100 such strings
strings = [generate_string() for _ in range(3208)]
for s in strings:
    print(s)