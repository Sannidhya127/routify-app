from colored import fg, bg, attr
import json
import os

print(f"{fg('green_1')}Welcome To Routify!{attr(0)}")

def login(cred):
    log_dat = cred.split(' ')
    # Check if user.json exists
    if not os.path.exists('user.json'):
        # If not, create it and write default user data
        with open('user.json', 'w') as file:
            user_data = {
                'username': f'{log_dat[1]}',
                'email': f'{log_dat[2]}',
                'type' : f'{log_dat[3]}'
            }
            json.dump(user_data, file)
    else:
        # If it exists, open it and check the user data
        with open('user.json', 'r') as file:
            user_data = json.load(file)
            if 'username' not in user_data or 'email' not in user_data or 'type' not in user_data:
                # If username or email is missing, write them
                user_data['username'] = f'{log_dat[1]}'
                user_data['email'] = f'{log_dat[2]}'
                user_data['type'] = f'{log_dat[3]}'
                with open('user.json', 'w') as file:
                    json.dump(user_data, file)


if __name__ == "__main__":
    while True:
        cmd = input(f"{fg('blue')}routify> {attr(0)}")
        if cmd == 'exit':
            exit()
        elif cmd[0:5] == 'login':
            login(cmd)