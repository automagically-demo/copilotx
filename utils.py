import re

# Regular expression for validating email addresses
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for validating phone numbers
phone_regex = r'^(\+)?1?\d{9,15}$'

# Regular expression for validating strong passwords
# A strong password is at least 8 characters long and contains at least one lowercase letter,
# one uppercase letter, one digit, and one special character
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(text):
    """Check if the text is a valid email address."""
    return bool(re.search(email_regex, text))

def is_valid_phone(text):
    """Check if the text is a valid phone number."""
    return bool(re.search(phone_regex, text))

def is_valid_password(text):
    """Check if the text is a valid password."""
    return bool(re.search(password_regex, text))

if __name__ == '__main__':
    # Test the validation functions with empty strings
    print("Email validation result:", "valid" if is_valid_email('') else "invalid")
    print("Phone validation result:", "valid" if is_valid_phone('') else "invalid")
    print("Password validation result:", "valid" if is_valid_password('') else "invalid")