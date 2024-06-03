"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def check_special_characters(input):
 for character in SPECIAL_CHARACTERS:
     if character == input:
         return True

def check_password_length(input):
    length_password = len(input)
    if length_password >= MIN_LENGTH and length_password <= MAX_LENGTH:
        return True

def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif check_special_characters(character):
            number_of_special += 1

    if check_password_length(password) and number_of_lower >= 1 and number_of_upper >= 1 and number_of_digit >= 1 and number_of_special >= 1:
        return True
    else:
        return False

main()