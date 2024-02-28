import re

email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
phone_regex = r'^(\+)?1?\d{9,15}$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(email):
    return bool(re.search(email_regex, email))

def is_valid_phone(phone):
    return bool(re.search(phone_regex, phone))

def is_valid_password(password):
    return bool(re.search(password_regex, password))

if __name__ == '__main__':
    print("Email validation:", "valid" if is_valid_email('') else "invalid")
    print("Phone validation:", "valid" if is_valid_phone('') else "invalid")
    print("Password validation:", "valid" if is_valid_password('') else "invalid")