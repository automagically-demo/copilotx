import re

# Regular expression for validating email addresses
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for validating phone numbers
phone_regex = r'^(\+)?1?\d{9,15}$'

# Regular expression for validating strong passwords
# A strong password is at least 8 characters long and contains at least one lowercase letter,
# one uppercase letter, one digit, and one special character
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid(text, regex):
    """Check if the text matches the regular expression."""
    return bool(re.search(regex, text))

if __name__ == '__main__':
    # Test the is_valid function with empty strings
    print("Email validation result:", "valid" if is_valid('', email_regex) else "invalid")
    print("Phone validation result:", "valid" if is_valid('', phone_regex) else "invalid")
    print("Password validation result:", "valid" if is_valid('', password_regex) else "invalid")