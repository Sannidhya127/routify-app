import os
import json
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit import Application
from prompt_toolkit.shortcuts import ProgressBar
from rich.console import Console
from prompt_toolkit.layout.dimension import D
from prompt_toolkit import Application
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.widgets import HorizontalLine, VerticalLine
from prompt_toolkit.buffer import Buffer
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import time
import time
from yaspin import yaspin
os.system('color 1F')

# Context manager:
# with yaspin():
#     time.sleep(1)  # time consuming code

# Function decorator:
def login(name, email):
    # log_dat = cred.split(' ')
    # Check if user.json exists
    if not os.path.exists('user.json'):
        # If not, create it and write default user data
        with open('user.json', 'w') as file:
            user_data = {
                'username': name,
                'email': email,
                'logged' : True
            }
            json.dump(user_data, file)
    else:
        # If it exists, open it and check the user data
        with open('user.json', 'r') as file:
            user_data = json.load(file)
            if 'username' not in user_data or 'email' not in user_data:
                # If username or email is missing, write them
                user_data['username'] = name,   
                user_data['email'] = email,
                user_data['logged'] = True
                with open('user.json', 'w') as file:
                    json.dump(user_data, file)
# @yaspin(text="...")
def CheckLogin():
    if not os.path.exists('user.json'):
        print_formatted_text(HTML('<b>Not logged in</b>'))
        return False
    else:
        with open('user.json', 'r') as file:
            user_data = json.load(file)
            print_formatted_text(HTML(f'<b>Logged in as {user_data["username"]} with email {user_data["email"]}</b>'))

        return True

def MainWin():
    if CheckLogin():
        pass
    else:
        name = Prompt.ask("Enter your name", default="Paul Atreides")
        email = Prompt.ask("Enter your email", default="Paul Atreides")
        # name = input("Enter your name")
        # email = input("Enter your email")
        login(name, email)
    while True:
        cmd = Prompt.ask("Routify>> ")
        if cmd == 'exit':
            break
        else:
            print_formatted_text(HTML(f'<b>Command {cmd} not found</b>'))

if __name__ == '__main__':
    # large_buffer = Buffer(document='Large segment', cursor_position=0)
    # small_buffer1 = Buffer(document='Small segment 1')
    # bottom_buffer = Buffer(document='Bottom segment')
    buffer1 = Buffer() 
    # Create windows for your buffer
    large_window = Window(content=FormattedTextControl(text=MainWin()), style='bg:#000080 #ffffff')
    small_window1 = Window(content=FormattedTextControl(text='Hello world'), style='bg:#000080 #ffffff')
    bottom_window = Window(content=FormattedTextControl(text='Hello world'), style='bg:#000080 #ffffff')

    root_container = HSplit([
        # Window(content=BufferControl(buffer=buffer1)),
        large_window,
        HorizontalLine(),
        VSplit([
            small_window1,
            VerticalLine(),
            bottom_window
        ])
    ])
    layout = Layout(root_container)
    app = Application(layout=layout, full_screen=True)
    app.run()