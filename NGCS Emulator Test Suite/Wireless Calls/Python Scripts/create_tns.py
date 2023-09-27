import random


def generate_phone_number(area_code):
    return str(area_code) + ''.join([str(random.randint(0, 9)) for _ in range(7)])


def generate_random_phone_numbers(n):
    numbers = []
    for _ in range(int(n * 0.30)):
        numbers.append(generate_phone_number(403))
    for _ in range(int(n * 0.15)):
        numbers.append(generate_phone_number(587))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(825))
    for _ in range(int(n * 0.10)):
        numbers.append(generate_phone_number(604))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(250))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(672))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(778))
    for _ in range(int(n * 0.15)):
        numbers.append(generate_phone_number(416))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(263))
    for _ in range(int(n * 0.05)):
        numbers.append(generate_phone_number(902))

    random.shuffle(numbers)
    return numbers


# Test the function
phone_numbers = generate_random_phone_numbers(58279)
for number in phone_numbers:
    print(number)
