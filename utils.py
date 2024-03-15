import re

EMAIL_REGEX = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
PHONE_REGEX = r'^(\+)?1?\d{9,15}$'
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid(text, regex):
    """Check if the text matches the given regex."""
    return bool(re.search(regex, text))

def print_validation_result(is_valid, input_type):
    """Print the validation result."""
    result = "valid" if is_valid else "invalid"
    print(f"The input is {result} as per {input_type} rules.")

if __name__ == '__main__':
    print_validation_result(is_valid('', EMAIL_REGEX), "email")
    print_validation_result(is_valid('', PHONE_REGEX), "phone number")
    print_validation_result(is_valid('', PASSWORD_REGEX), "password")