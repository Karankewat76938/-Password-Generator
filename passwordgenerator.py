import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # Special characters
    
    if not characters:
        return "Please select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Main Program ---
print("🔐 Password Generator 🔐")

try:
    length = int(input("Enter password length (e.g., 8-20): "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\n✅ Generated Password: {password}")
except ValueError:
    print("Please enter a valid number for password length.")
