import uuid

def generate_uuids():
    return str(uuid.uuid4())


for _ in range(52702):
    print(generate_uuids())
