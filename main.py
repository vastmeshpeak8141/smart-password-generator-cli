import random
import string

def generate_password(pwd_len=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pwd_len))
    return password

if __name__ == "__main__":
    print(generate_password())
