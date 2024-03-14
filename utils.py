import re

email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
phone_regex = r'^(\+)?1?\d{9,15}$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid(text, regex):
    """Check if the text matches the provided regex."""
    return bool(re.search(regex, text))

def print_validation_result(is_valid, input_type):
    """Print whether the input is valid or invalid."""
    result = "valid" if is_valid else "invalid"
    print(f"The {input_type} is {result}.")

if __name__ == '__main__':
    print_validation_result(is_valid('', email_regex), "email")
    print_validation_result(is_valid('', phone_regex), "phone number")
    print_validation_result(is_valid('', password_regex), "password")