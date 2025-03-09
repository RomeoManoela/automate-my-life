import string
import random


def generate_password(length: int, has_special: bool, has_number: bool) -> str:
    """Generate a random password with the given length and options"""
    password: str = ''
    all_chars: str = string.ascii_lowercase + string.ascii_uppercase
    digits: str = string.digits
    punctuation: str = string.punctuation

    contain_special_chars: bool = True
    contain_numbers: bool = True

    if has_special:
        contain_special_chars = False # if has_special is True, then the password must contain special characters
        all_chars += punctuation
    if has_number:
        contain_numbers = False # if has_number is True, then the password must contain numbers
        all_chars += digits
    i: int = 0

    while i < length or not contain_special_chars or not contain_numbers:
        char: str = random.choice(all_chars)
        password += char
        if char in digits:
            contain_numbers = True
        elif char in punctuation:
            contain_special_chars = True
        i += 1

    return password


if __name__ == '__main__':
    """Run the main function"""
    n: int = int(input('Enter the minimum length of the password: '))
    special: bool = input('Do you want special characters? (y/n): ') == 'y'
    number: bool = input('Do you want numbers? (y/n): ') == 'y'
    my_password= generate_password(n, special, number)
    print(my_password)
