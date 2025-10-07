import re
import secrets
import string

def generate_password(
        length: int=16, 
        nums: int=1, 
        special_chars: int=1, 
        uppercase: int=1, 
        lowercase: int=1
) -> str:
    """Takes parameters provided and generates a password matching those parameters. Uses true random secrets module for security.
    Args:
        length (int): How long the password should be
        nums (int): How many numbers in the password
        special_chars (int): How many special characters including underscore in the password
        uppercase (int): How many uppercase characters in the password
        lowercase (int): How many lowercase characters in the password
        
        Returns:
            str: The resulting password based on constraints
    """
    total_constraints = nums + special_chars + uppercase + lowercase

    # Guard clause
    if total_constraints > length:
        raise ValueError('Sum of constraints cannot exceed the password length')

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Escape symbols to make it safe for Regex
    escaped_symbols = re.escape(symbols)
    constraints = [
        (nums, r'\d'),
        (lowercase, r'[a-z]'),
        (uppercase, r'[A-Z]'),
        (special_chars, fr'[{escaped_symbols}]')
    ]

    while True:
        password = ''

        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            break

    return password

def main():
    new_password = generate_password()
    print(new_password)

if __name__ == '__main__':
    main()