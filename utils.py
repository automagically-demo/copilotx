import re

def is_valid_email(email):
    """
    Validate an email address.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    e_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
    return bool(re.search(e_regex, email))


def is_valid_phone(phone):
    """
    Validate a phone number.

    Parameters:
    phone (str): The phone number to validate.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    p_regex = r'^(\+)?1?\d{9,15}$'
    return bool(re.search(p_regex, phone))


def is_valid_password(password):
    """
    Validate a password. The password must contain at least one lowercase letter,
    one uppercase letter, one digit, and one special character. It must be at least 8 characters long.

    Parameters:
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    s_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.search(s_regex, password))