import re

email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
phone_regex = r'^(\+)?1?\d{9,15}$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(text):
    """Check if the text is a valid email."""
    return bool(re.search(email_regex, text))

def is_valid_phone_number(text):
    """Check if the text is a valid phone number."""
    return bool(re.search(phone_regex, text))

def is_valid_password(text):
    """Check if the text is a valid password."""
    return bool(re.search(password_regex, text))

def print_validation_result(is_valid, input_type):
    """Print whether the input is valid or invalid."""
    result = "valid" if is_valid else "invalid"
    print(f"The {input_type} is {result}.")

if __name__ == '__main__':
    print_validation_result(is_valid_email(''), "email")
    print_validation_result(is_valid_phone_number(''), "phone number")
    print_validation_result(is_valid_password(''), "password")