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
    
    # Iterate over each line in the expenses_string
    for line in expenses_string.splitlines():
        # Ignore lines that start with '#'
        if line.startswith("#"):
            continue
        
        # Split the line into date, value, and currency
        date, value, currency = line.split(" ")
        
        # Append the parsed expense to the expenses list
        expenses.append((float(value), currency, datetime.datetime.strptime(date, "%Y-%m-%d")))
    
    # Return the list of parsed expenses
    return expenses

# Define a string of expenses data
expenses_data = '''2023-01-02 -34.01 USD
2023-01-03 2.59 DKK
2023-01-03 -2.72 EUR'''

# Parse the expenses data
expenses = parse_expenses(expenses_data)

# Print each parsed expense
for expense in expenses:
    print(f'{expense[0]} {expense[1]} {expense[2]}')