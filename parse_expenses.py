import datetime

def parse_expenses(expenses_string):
    """
    Parse the list of expenses and return the list of triples (value, currency, date).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string :
        2023-01-02 -34.01 USD
        2023-01-03 2.59 DKK
        2023-01-03 -2.72 EUR
    """
    # Initialize an empty list to store the parsed expenses
    expenses = []

    # Split the expenses_string into lines
    lines = expenses_string.splitlines()

    # Iterate over each line
    for line in lines:
        # Ignore lines that start with '#'
        if line.startswith("#"):
            continue

        # Split the line into date, value, and currency
        date_str, value_str, currency = line.split()

        # Convert the date string to a datetime object
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        # Convert the value string to a float
        value = float(value_str)

        # Append the parsed expense to the expenses list
        expenses.append((value, currency, date))

    # Return the list of parsed expenses
    return expenses