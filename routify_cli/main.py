import os
import json
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit import Application
from prompt_toolkit.shortcuts import ProgressBar
from rich.console import Console
from prompt_toolkit.layout.dimension import D
from blessed import Terminal
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
from asciimatics.exceptions import StopApplication
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from colored import fg, bg, attr
import time
import time
from yaspin import yaspin
from asciimatics.event import KeyboardEvent

import threading
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
# from prompt_toolkit.application import StopApplication
stop_thread = False
def splash_screen(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Routify", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("Precision in Every Moment", font='Standard'),
            screen.height // 2 + 3),
        Cycle(
            screen,
            FigletText("Press 'q' twice to exit screen", font='small'),
            screen.height // 2 + 10),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 120)])
    screen.print_at('Press any key to exit.', 0, 0)
    screen.refresh()

    # Loop until a key is pressed
    while True:
        event = screen.get_event()
        if event is not None:
            if isinstance(event, KeyboardEvent):
                # Close the screen when a key is pressed
                screen.close()
                break 
        # time.sleep(2)
        # raise StopAppliqcation("Done")

def run_screen():
    global stop_thread
    try:
        Screen.wrapper(splash_screen)
    except StopApplication:
        stop_thread = True
        return

# Context manager:
# with yaspin():
#     time.sleep(1)  # time consuming code

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
                'log' : True
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
                user_data['log'] = True
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

def print_ascii_art():
    ascii_art = f"""{fg('red_1')}
                                                                          
                                                                          
                                 ______  _____  _     _ _______ _____ _______ __   __
                                |_____/ |     | |     |    |      |   |______   \_/  
                                |    \_ |_____| |_____|    |    __|__ |          |   
                                                     
    {attr(0)}"""
    print(ascii_art)


def PromptSegment(term):
    with term.location(x=0, y=0):
        print_ascii_art()
        # os.system("color ef")
        print("Type help for some help")
        while True:
            cmd = Prompt.ask(f"{fg('green_1')}Routify>> {attr(0)}")
            if cmd == "exit":
                exit()
            elif cmd == "r --login":
                CheckLogin()
            elif cmd[0::5] == 'login':
                login(cmd)
            elif cmd == "r --new":
                pass

def Other():
    with term.location(x=term.width // 2, y=0):
        print(term.center("Code Segment 2"))
    # Your code for segment 2 here
    time.sleep(2) 

def run_in_segment(func):
    with term.cbreak(), term.hidden_cursor():
        func()

def main():
    with term.fullscreen():
        with term.location():
            print(term.clear())
            # Split the console into two segments
            thread1 = threading.Thread(target=run_in_segment, args=(PromptSegment))
            thread2 = threading.Thread(target=run_in_segment, args=(Other))
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()

 
def NewRoutine():
    tasks = [] 
    slots = []
    days = []
    no_sub = int(input("Enter the number of tasks: "))
    for i in range(no_sub):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
    print(f"Recieved task data: {tasks}")
    t_slot_n = int(input("Enter the number of time slots: "))
    for i in range(t_slot_n):
        slot = input(f"Enter time slot {i+1}: ")
        slots.append(slot)
    print(f"Recieved time slot data: {slots}")
    n_days = int(input("Enter the number of days: "))
    for i in range(n_days):
        day = input(f"Enter day {i+1}: ")
        days.append(day)
    print(f"Recieved day data: {days}")

    # Create the matrix
    matrix = [['0'] + days]
    for i in range(len(slots)):
        matrix.append([slots[i]] + tasks)

    print(matrix)


if __name__ == '__main__':
    # Splash Screen launched
    Screen.wrapper(splash_screen)
    term = Terminal()
    main()
    cmd = input("routify>> ")
    if cmd == "exit":
        exit()
    elif cmd == 'new':
        NewRoutine()
 
        