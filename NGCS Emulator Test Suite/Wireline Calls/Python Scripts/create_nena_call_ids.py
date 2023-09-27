import random

import random
import string


def generate_string(length=15):
    # Start the string with a random lowercase letter
    result = random.choice(string.ascii_lowercase)

    # Append random characters until we reach the desired length
    for _ in range(length - 1):
        result += random.choice(string.ascii_lowercase + string.digits)

    return result


for _ in range(58279):
    print(generate_string())
