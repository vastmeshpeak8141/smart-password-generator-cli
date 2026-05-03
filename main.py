import random
import string

def generate_password(pwd_len=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pwd_len))
    return password

def generate_batch(count=5, pwd_len=12):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(pwd_len))
    return passwords

if __name__ == "__main__":
    for i, pwd in enumerate(generate_batch(), 1):
        print(f"{i}. {pwd}")
