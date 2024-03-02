import re

EMAIL_REGEX = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
PHONE_REGEX = r'^(\+)?1?\d{9,15}$'
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(text):
    return bool(re.search(EMAIL_REGEX, text))

def is_valid_phone(text):
    return bool(re.search(PHONE_REGEX, text))

def is_valid_password(text):
    return bool(re.search(PASSWORD_REGEX, text))

if __name__ == '__main__':
    print("Email is", "valid" if is_valid_email('') else "invalid")
    print("Phone is", "valid" if is_valid_phone('') else "invalid")
    print("Password is", "valid" if is_valid_password('') else "invalid")