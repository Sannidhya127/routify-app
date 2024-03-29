import random

routine = {}


def constraints(iters):
    for i in range(int(iters)):
        task = input(f"Enter constraint {i}: ")
        durat = input(f"Enter duration for constraint {i}: ")
        priority = input(f"Enter priority for constraint {i}: ")

        routine[task] = {
            'constraint': task,
            'duration': durat,
            'priority': priority
        }




def generate_population(routine, population_size):
    population = []
    for _ in range(population_size):
        individual = random.sample(list(routine.items()), len(routine))
        population.append(dict(individual))
    return population
def fitness_function(individual):
    total_duration = 0
    total_priority = 0

    for task, details in individual.items():
        total_duration += int(details['duration'])
        total_priority += int(details['priority'])

    # Fitness is the total priority divided by the total duration
    # We multiply by 100 to scale the fitness to a more readable number
    fitness = (total_priority / total_duration) * 100

    return fitness


def selection(population):
    tournament_size = 3  # Size of the tournament
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=fitness_function, reverse=True)
    return tournament[0]  # Return the individual with the highest fitness

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child1 = list(parent1.items())[:crossover_point] + list(parent2.items())[crossover_point:]
    child2 = list(parent2.items())[:crossover_point] + list(parent1.items())[crossover_point:]
    return dict(child1), dict(child2)

def mutation(individual):
    keys = list(individual.keys())
    if len(keys) < 2:
        return individual  # Not enough keys to perform mutation
    point1, point2 = random.sample(range(len(keys)), 2)
    keys[point1], keys[point2] = keys[point2], keys[point1]
    return {key: individual[key] for key in keys}

def run_genetic_algorithm(routine, population_size, num_generations):
    # Generate the initial population
    population = generate_population(routine, population_size)

    # Run the genetic algorithm for a specified number of generations
    for _ in range(num_generations):
        new_population = []

        # Perform selection, crossover, and mutation to generate new individuals
        for _ in range(population_size // 2):
            parent1 = selection(population)
            parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutation(child1))
            new_population.append(mutation(child2))

        # Replace the old population with the new population
        population = new_population

    # Sort the final population by fitness
    population.sort(key=fitness_function, reverse=True)

    # Return the entire sorted population
    return population

while True:
    cmd = input(">>")
    if cmd == 'exit':
        exit()
    elif cmd == "new":
        print("New routine generation initiated.")
        num_e = input("Enter number of entries")
        constraints(int(num_e))
        population = run_genetic_algorithm(routine, 100, 50)
        for i, individual in enumerate(population):
            print(f"Routine {i+1}: {list(individual.keys())}")
    else:
        print("Command not found")