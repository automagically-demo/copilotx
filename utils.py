import re

# Regular expression for email validation
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for phone number validation
phone_regex = r'^(\+)?1?\d{9,15}$'

# Regular expression for strong password validation
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(email):
    """Check if the provided email is valid."""
    return bool(re.search(email_regex, email))

def is_valid_phone(phone):
    """Check if the provided phone number is valid."""
    return bool(re.search(phone_regex, phone))

def is_valid_password(password):
    """Check if the provided password is valid."""
    return bool(re.search(password_regex, password))

if __name__ == '__main__':
    # Test the validation functions
    print('Email:', 'valid' if is_valid_email('') else 'invalid')
    print('Phone:', 'valid' if is_valid_phone('') else 'invalid')
    print('Password:', 'valid' if is_valid_password('') else 'invalid')