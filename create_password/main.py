import string
import random

def generate_password(lenght=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError('Please select at least one character type!')

    password = ''.join(random.choice(chars) for _ in range(lenght))
    return password

if __name__ == "__main__":
    lenght = int(input('Password length:'))
    print("What symbols should I use?")
    use_upper = input('Capital letters (Y/n): ').strip().lower() != 'n'
    use_lower = input('Lowercase letters (Y/n): ').strip().lower() != 'n'
    use_digits = input('Digits (Y/n): ').strip().lower() != 'n'
    use_symbols = input('Special characters (Y/n): ').strip().lower() != 'n'

    try:
        pwd = generate_password(lenght, use_upper, use_lower, use_digits, use_symbols)
        print(f'Your password : {pwd}')
    except ValueError as e:
        print(e)