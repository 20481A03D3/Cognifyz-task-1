import re

def is_valid_email(email):
    # Define a regular expression pattern for a basic email format
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    # Use the pattern to match the email string
    match = email_pattern.match(email)

    # Return True if there is a match (valid email), otherwise False
    return bool(match)

# Example usage:
email_to_check = "example@email.com"
result = is_valid_email(email_to_check)

if result:
    print(f"{email_to_check} is a valid email address.")
else:
    print(f"{email_to_check} is not a valid email address.")
