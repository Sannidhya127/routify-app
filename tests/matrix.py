import random

# Define the elements and their frequencies
elements = ['A', 'B', 'C', 'D']
frequencies = [3, 1, 2, 3]

# Create a flat list with the elements repeated according to their frequencies
choices = [element for element, frequency in zip(elements, frequencies) for _ in range(frequency)]

# Shuffle the list to ensure randomness
random.shuffle(choices)

# Create a 3x3 matrix from the shuffled list
I = [choices[i:i+3] for i in range(0, 9, 3)]

print(I)

# Transpose the matrix
I_transposed = list(map(list, zip(*I)))
print("")
print(I_transposed)
print("")


def generate_unique_row(choices, row_length):
    row = []
    for _ in range(row_length):
        choice = random.choice(choices)
        while choice in row:
            choice = random.choice(choices)
        row.append(choice)
    return row

# Create a 3x3 matrix with unique rows
I = [generate_unique_row(choices, 3) for _ in range(3)]
print(I)
# Create a 3x3 matrix with unique rows
I = [generate_unique_row(choices, 3) for _ in range(3)]

# Transpose the matrix to get unique columns
I_transposed = list(map(list, zip(*I)))

print(I_transposed)

print("Now printing priority tree matrix")

import heapq

# Define the elements, their credits, and the slot priorities
elements = ['A', 'B', 'C', 'D', 'E']
credits = [3, 1, 2, 3, 1, ]
slot_priorities = [1, 2, 3, 1, 2]

# Create a priority queue for the elements and their credits
element_queue = [(-credit, element) for element, credit in zip(elements, credits)]
heapq.heapify(element_queue)

# Create a priority queue for the slots and their priorities
slot_queue = [(-priority, i) for i, priority in enumerate(slot_priorities)]
heapq.heapify(slot_queue)

# Create an empty 3x3 matrix
I = [['' for _ in range(3)] for _ in range(3)]

# Assign the elements to the slots
while element_queue and slot_queue:
    _, element = heapq.heappop(element_queue)
    _, slot = heapq.heappop(slot_queue)
    row, col = divmod(slot, 3)
    I[row][col] = element

print(I)

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

NewRoutine()