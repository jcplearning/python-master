import random
#Password manager — generate strong passwords with configurable length and character set.
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = "abcdefghijklmnopqrstuvwxyz"
    if use_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_digits:
        characters += "0123456789"
    if use_special_chars:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 16
password = generate_password(length=password_length, use_uppercase=True, use_digits=True, use_special_chars=True)
print(f"Generated Password: {password}")


