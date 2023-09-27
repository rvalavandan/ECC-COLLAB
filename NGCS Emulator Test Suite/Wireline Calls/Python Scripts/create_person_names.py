


import random

first_names = [
    "Aaron", "Abigail", "Adam", "Aisha", "Alan", "Alejandro", "Alice", "Amina",
    "Andrew", "Angela", "Anthony", "Aria", "Ariana", "Ashley", "Avery", "Benjamin",
    "Bianca", "Bradley", "Brandon", "Brianna", "Caleb", "Camila", "Carlos", "Caroline",
    "Catherine", "Charlie", "Chloe", "Chris", "Christian", "Christina", "Christopher",
    "Claire", "Daniel", "David", "Diana", "Diego", "Dylan", "Elena", "Elijah",
    "Elizabeth", "Ella", "Emily", "Emma", "Eric", "Ethan", "Eva", "Evan", "Evelyn",
    "Faith", "Fernando", "Gabriel", "Grace", "Hailey", "Hannah", "Harper", "Henry",
    "Isabella", "Isabelle", "Jack", "Jackson", "Jacob", "Jasmine", "Jason", "Jennifer",
    "Jeremy", "Jessica", "John", "Jonathan", "Jordan", "Joseph", "Joshua", "Julia",
    "Kaitlyn", "Katie", "Kayla", "Kevin", "Kiara", "Kimberly", "Kyle", "Laura",
    "Lauren", "Layla", "Leah", "Leo", "Liam", "Lily", "Logan", "Lucas", "Luke",
    "Madison", "Malia", "Maria", "Mark", "Matthew", "Maya", "Megan", "Melanie",
    "Michael", "Miguel", "Mohammed", "Nathan", "Nicholas", "Nicole", "Noah", "Olivia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Garcia",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Hall", "Allen", "Torres", "Nguyen", "Wright", "Flores", "King", "Scott",
    "Rivera", "Green", "Hill", "Adams", "Baker", "Nelson", "Carter", "Mitchell",
    "Roberts", "Cruz", "Morales", "Ortiz", "Gomez", "Murray", "Freeman", "Wells",
    "Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter", "Hicks", "Crawford",
    "Henry", "Boyd", "Mason", "Morris", "Jimenez", "Salazar", "Peck", "Bryant",
    "Armstrong", "Vasquez", "Gonzales", "Fisher", "Vargas", "Harrison", "Mack",
    "Fields", "Gibson", "McDonald", "Brooks", "Ryan", "Ford", "Russell", "Fernandez",
    "Morgan", "Burke", "Richards", "Willis", "Ray", "Watkins", "Olson", "Carroll",
    "Duncan", "Snyder", "Hart", "Cunningham", "Bradley", "Lane", "Andrews", "Ruiz",
    "Harper", "Fox", "Riley", "Armstrong", "Carpenter", "Weaver", "Greene", "Lawrence",
    "Elliott", "Chavez", "Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson"
]


def generate_business_name():
    return f"{random.choice(first_names)} {random.choice(last_names)} "

names = set()
desired_count = 1753

while len(names) < desired_count:
    names.add(generate_business_name())

for name in names:
    print(name.upper().strip())
