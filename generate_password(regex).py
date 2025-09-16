import string
import secrets
import re

def generate_password(length=16, nums=1, special_chars=1, lowercase=1, uppercase=1):
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_chars)
            
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[^a-zA-Z0-9]'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]')
        ]
        
        if all(
            constraint <= len(re.findall(pattern,password))    for constraint, pattern in constraints    
        ):
            break;
        
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print(f'Generated new password: {new_password}')
