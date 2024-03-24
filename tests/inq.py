import re
from InquirerPy import prompt

def is_valid_email(email):
    # Regular expression for validating email format
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def email_validator(email):
    if is_valid_email(email):
        return True, ""
    return False, "Invalid email format"

questions = [
    {
        "type": "input",
        "name": "email",
        "message": "Enter your email:",
        "validate": email_validator
    }
]

answers = prompt(questions)
print("Entered email:", answers["email"])
