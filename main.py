import random
import string
import argparse

def generate_password(pwd_len=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for _ in range(pwd_len))
    return password

def generate_batch(count=5, pwd_len=12, **kwargs):
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(pwd_len, **kwargs))
    return passwords

def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("-l", "--pwd_len", type=int, default=12, help="Password length")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")
    args = parser.parse_args()

    passwords = generate_batch(
        count=args.count,
        pwd_len=args.pwd_len,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_special=not args.no_special,
    )
    for pwd in passwords:
        print(pwd)

if __name__ == "__main__":
    main()
