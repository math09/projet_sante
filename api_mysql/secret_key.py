import os

random_bytes = os.urandom(32)

SECRET_KEY = random_bytes.hex()

print(SECRET_KEY)