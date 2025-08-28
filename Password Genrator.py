import random
import string

def generate_password(length=12):
    """Generate a strong random password"""
    # Characters: letters + digits + special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one lowercase, one uppercase, one digit, one special char
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the remaining length with random characters
    password += random.choices(characters, k=length-4)
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    
    return "".join(password)

# ---------------- MAIN PROGRAM ----------------
print(" Random Password Generator ")

try:
    length = int(input("Enter desired password length (min 6): "))
    if length < 6:
        print(" Password length too short! Using default length = 12")
        length = 12
except ValueError:
    print(" Invalid input! Using default length = 12")
    length = 12

password = generate_password(length)
print(f"\n Your secure password is: {password}")