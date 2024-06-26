import os
import json
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit import Application
from prompt_toolkit.shortcuts import ProgressBar
from rich.console import Console
from collections import deque
from prompt_toolkit.layout.dimension import D
from blessed import Terminal
import random
from prompt_toolkit import Application
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout import HSplit, VSplit, Layout
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.buffer import Buffer
from tabulate import tabulate
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

def check_columns(matrix):
    # Transpose the matrix to iterate over columns
    transposed_matrix = zip(*matrix)

    for column in transposed_matrix:
        # Convert column to set and check if all elements are the same
        if len(set(column)) == 1:
            return False

    return True

def check_and_shuffle(matrix):
    # Transpose the matrix to iterate over columns
    transposed_matrix = list(zip(*matrix[1:]))  # Exclude the first row (the days)

    for i, column in enumerate(transposed_matrix):
        # If all elements in the column are the same
        if len(set(column)) == 1:
            # Shuffle the tasks in the column
            tasks = list(column)
            random.shuffle(tasks)
            # Update the tasks in the original matrix
            for j, row in enumerate(matrix[1:]):
                # Ensure that row has enough elements
                while len(row) <= i+1:
                    row.append(None)
                row[i+1] = tasks[j]  # i+1 because the first element in each row is the time slot

    return matrix
import heapq




def NewRoutine(task_priorities, slot_priorities):
    tasks = [] 
    slots = []
    days = []
    tp = {}
    sp = {}
    
    # Input tasks and priorities
    no_sub = int(input("Enter the number of tasks: "))
    for i in range(no_sub):
        task = input(f"Enter task {i+1}: ")
        task_priority = int(input(f"Enter priority for task {i+1}: "))
        tasks.append((-task_priority, task))
        if task_priority not in tp:
            tp[task] = task_priority # Store tasks as (-priority, task)
    
    original_tasks = list(tasks)  # Keep a copy of the original tasks list
    heapq.heapify(tasks)  # Turn tasks list into a heap
    print(f"Received task data: {tasks}")
    
    # Input time slots and priorities
    t_slot_n = int(input("Enter the number of time slots: "))
    for i in range(t_slot_n):
        slot = input(f"Enter time slot {i+1}: ")
        slot_priority = int(input(f"Enter priority for slot {i+1}: "))
        slots.append((-slot_priority, slot))  # Store slots as (-priority, slot)
        if slot_priority not in sp:
            sp[slot] = slot_priority
    heapq.heapify(slots)  # Turn slots list into a heap
    print(f"Received time slot data: {slots}")
    
    # Input days
    n_days = int(input("Enter the number of days: "))
    for i in range(n_days):
        day = input(f"Enter day {i+1}: ")
        days.append(day)
    print(f"Received day data: {days}")
    
    # Shuffle tasks and days to avoid repetition
    original_tasks = list(tasks)

    # Create a heap from the slots and tasks
    heapq.heapify(slots)
    heapq.heapify(tasks)

    # Shuffle the days
    random.shuffle(days)

    # Create the routine matrix
    matrix = [['0'] + days]

    # Create a queue of tasks
    task_queue = deque(original_tasks)

    # Assign tasks to days for each set of slots
    while slots:
        slot_priority, slot = heapq.heappop(slots)  # Pop slot with highest priority
        row = [slot]
        for _ in days:
            if not task_queue:  # If the task queue is empty
                task_queue = deque(original_tasks)  # Re-populate the task queue
                random.shuffle(task_queue)  # Shuffle the task queue
            task_priority, task = task_queue.popleft()  # Remove the next task from the front of the queue
            row.append(task)  # Append the task to the row
        matrix.append(row)

    # for row in matrix:
    #     print('\t'.join(str(element) for element in row))
    print(tabulate(matrix, headers="firstrow", tablefmt="grid"))
    return matrix, tp, sp





def convert_to_priority_matrix(matrix, task_priorities, slot_priorities):
    priority_matrix = []
    for i, row in enumerate(matrix):
        if i == 0:  # Skip the first row (the days)qqqqq
            continue
        priority_row = [row[0]]  # Copy the time slot
        for task in row[1:]:
            if task == 'No task':
                task_priority = 0
            else:
                task_priority = task_priorities[task]
            slot_priority = slot_priorities[row[0]]
            priority_row.append((task_priority, slot_priority))
        priority_matrix.append(priority_row)
    return priority_matrix





if __name__ == '__main__':
    # Splash Screen launched
    Screen.wrapper(splash_screen)
    term = Terminal()
    main()
    while True:
        cmd = input("routify>> ")
        if cmd == "exit":
            exit()
        elif cmd == 'new':
            nr = NewRoutine(1,2)
        else:
            print("invalid command")
        