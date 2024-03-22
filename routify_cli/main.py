import os
import json
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.shortcuts import ProgressBar
import time
import time
from yaspin import yaspin

# Context manager:
with yaspin():
    time.sleep(1)  # time consuming code

# Function decorator:
def login(cred):
    log_dat = cred.split(' ')
    # Check if user.json exists
    if not os.path.exists('user.json'):
        # If not, create it and write default user data
        with open('user.json', 'w') as file:
            user_data = {
                'username': f'{log_dat[1]}',
                'email': f'{log_dat[2]}',
                'logged' : True
            }
            json.dump(user_data, file)
    else:
        # If it exists, open it and check the user data
        with open('user.json', 'r') as file:
            user_data = json.load(file)
            if 'username' not in user_data or 'email' not in user_data:
                # If username or email is missing, write them
                user_data['username'] = f'{log_dat[1]}'
                user_data['email'] = f'{log_dat[2]}'
                user_data['logged'] = True
                with open('user.json', 'w') as file:
                    json.dump(user_data, file)
@yaspin(text="...")
def CheckLogin():
    if not os.path.exists('user.json'):
        print_formatted_text(HTML('<b>Not logged in</b>'))
    else:
        with open('user.json', 'r') as file:
            user_data = json.load(file)
            if 'username' not in user_data or 'email' not in user_data:
                print_formatted_text(HTML('<b>Not logged in</b>'))
            else:
                print_formatted_text(HTML(f'<b>Logged in as {user_data["username"]} with email {user_data["email"]}</b>'))

CheckLogin()